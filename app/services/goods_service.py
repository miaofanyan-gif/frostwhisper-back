import json
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.future import select
from sqlalchemy import update, delete, func
from redis import asyncio as aioredis
from app.models.goods import ProductMain
from typing import List
from decimal import Decimal
import logging
from app.models.goods import ProductComment, ProductRelated
from app.schemas.goods import CommentCreate, RelatedProductItem
from app.models.order import OrderMain
from fastapi import HTTPException
import os


CACHE_KEY_PREFIX = "fw:product:"


class GoodsService:
    def __init__(self, db: Session, redis: aioredis.Redis):
        self.db = db
        self.redis = redis

    def get_related_products_by_product_id(
        self,
        product_id: int
    ) -> List[ProductMain]:

        # 1. 先查询该商品的所有关联记录
        related_records = self.db.query(ProductRelated).filter(
            ProductRelated.product_id == product_id
        ).all()

        if not related_records:
            return []

        # 2. 提取所有关联商品 ID
        related_ids = [item.related_id for item in related_records]

        # 3. 查询这些商品（过滤已删除、已下架）
        related_products = self.db.query(ProductMain).filter(
            ProductMain.id.in_(related_ids),
            ProductMain.is_deleted == False,
            ProductMain.status == 1
        ).all()

        URL = os.getenv("URL")

        # 4. 转换成 Schema 并返回
        result = []
        for p in related_products:
            result.append(RelatedProductItem(
                id=p.id,
                name=p.name,
                name_en=p.name_en,
                price=Decimal(str(p.price)),
                cover=URL+p.cover,
                gender=p.gender,
                dynasty_style=p.dynasty_style
            ))

        return result

    def get_product(self, product_id: int):
        query = select(ProductMain).where(ProductMain.is_deleted == 0)
        query = query.where(ProductMain.id == product_id)
        query = query.options(
            selectinload(ProductMain.images),  # 关键：加载商品图片表
            selectinload(ProductMain.skus),  # 关键：加载商品SKU表
            selectinload(ProductMain.comments)
        )

        result = self.db.execute(query)
        items = result.scalars().first()

        if not items:
            raise HTTPException(
                status_code=404, detail="Goods does not exist!")

         # 2. 查询关联商品
        related_list = self.get_related_products_by_product_id(product_id)

        # 3. 塞入字段
        # items.related_products = related_list

        URL = os.getenv("URL")

        # 处理图片列表与封面图
        images = []
        cover_image = None
        if items.images:
            for img in items.images:
                img.url = URL + str(img.url) if img.url else None

                if getattr(img, "is_cover", 0) == 1:
                    cover_image = img.url
                    items.cover_image = cover_image

        # 3. ✅ 返回字典，让 Pydantic 自动匹配
        return {
            **items.__dict__,  # 原有商品所有字段
            "related_products": related_list  # 直接塞入关联商品列表
        }

    def list_products(self, filter_params: dict = None, keyword: str = None,
                      page: int = 1,
                      page_size: int = 10
                      ):
        # 多维度筛选实现
        query = select(ProductMain).where(ProductMain.is_deleted == 0)

        min_price = filter_params.get("min_price")
        max_price = filter_params.get("max_price")

        # 只有传了有效值才拼接
        if min_price is not None and min_price != "":
            query = query.where(ProductMain.base_price >= float(min_price))

        if max_price is not None and max_price != "":
            query = query.where(ProductMain.base_price <= float(max_price))

        # 价格区间
        if filter_params and filter_params.get("min_price") is not None:
            query = query.where(ProductMain.base_price >=
                                filter_params["min_price"])
        if filter_params and filter_params.get("max_price") is not None:
            query = query.where(ProductMain.base_price <=
                                filter_params["max_price"])

        # 形制体系
        if filter_params and filter_params.get("shape_system"):
            shapes = filter_params["shape_system"]
            query = query.where(ProductMain.shape_system.in_(shapes))
        if filter_params and filter_params.get("body_fit"):
            shapes = filter_params["body_fit"]
            query = query.where(ProductMain.body_fit.in_(shapes))
        if filter_params and filter_params.get("is_rental_available") is not None:
            is_rental_available = filter_params["is_rental_available"]
            query = query.where(
                ProductMain.is_rental_available == is_rental_available)

        # 朝代风格
        if filter_params and filter_params.get("dynasty_style"):
            dynasties = filter_params["dynasty_style"]
            query = query.where(ProductMain.dynasty_style.in_(dynasties))

        # 性别
        if filter_params and filter_params.get("gender"):
            genders = filter_params["gender"]
            query = query.where(ProductMain.gender.in_(genders))

        # 用途场景
        if filter_params and filter_params.get("usage_scene"):
            scenes = filter_params["usage_scene"]
            query = query.where(ProductMain.usage_scene.in_(scenes))

        # 款式结构
        if filter_params and filter_params.get("structure"):
            structures = filter_params["structure"]
            query = query.where(ProductMain.structure.in_(structures))

        # 仓库
        if filter_params and filter_params.get("warehouse"):
            warehouses = filter_params["warehouse"]
            query = query.where(ProductMain.warehouse.in_(warehouses))

        # 搜索功能
        if filter_params and filter_params.get("keyword"):
            query = query.filter(
                or_(
                    ProductMain.name.like(f"%{keyword}%"),
                    ProductMain.name_cn.like(f"%{keyword}%"),
                    ProductMain.name_en.like(f"%{keyword}%"),
                    ProductMain.brand.like(f"%{keyword}%"),
                    ProductMain.product_sn.like(f"%{keyword}%")
                )
            )

        # 关联图片
        query = query.options(selectinload(ProductMain.images))

        # 分页
        offset_value = (page - 1) * page_size
        paginated_query = query.order_by(ProductMain.id.desc()).offset(
            offset_value).limit(page_size)

        result = self.db.execute(paginated_query)
        items = result.scalars().all()

        # 总数
        total_count_query = select(func.count()).select_from(query.subquery())
        total = self.db.execute(total_count_query).scalar()

        # ===================== 【关键】返回数据增加所有筛选字段 =====================
        result = []
        URL = os.getenv("URL")

        for p in items:
            cover_image = None
            if p.images:
                for img in p.images:
                    if img.is_cover == 1:
                        cover_image = img.url
                        break

            result.append({
                "id": p.id,
                "product_sn": p.product_sn,
                "name": p.name,
                "name_cn": p.name_cn,
                "name_en": p.name_en,
                "brand": p.brand,
                "price": p.price,
                "deposit": p.deposit,

                # ===================== 筛选需要的字段全部加上 =====================
                "shape_system": p.shape_system,         # 形制
                "dynasty_style": p.dynasty_style,       # 朝代
                "gender": p.gender,                     # 性别
                "usage_scene": p.usage_scene,           # 场景
                "structure": p.structure,               # 结构
                "warehouse": p.warehouse,               # 仓库

                "is_rental_available": p.is_rental_available == 1,
                "is_customizable": p.is_customizable == 1,
                "cover_image": URL + str(cover_image) if cover_image else None,
                "category_id": p.category_id,
                "status": p.status,
                "create_time": p.create_time
            })

        return {
            "items": result,
            "total": total,
            "page": page,
            "page_size": page_size
        }

    def update_product(self, product_id: int, data: dict):
        # 更新数据库并同步清除缓存 [cite: 51, 79]
        self.db.execute(update(ProductMain).where(
            ProductMain.id == product_id).values(**data))
        self.db.commit()
        self.redis.delete(f"{CACHE_KEY_PREFIX}{product_id}")


# tijiao pinglun

    def create_comment(self, comment_data: CommentCreate, user_id: int):
        # 1. 检查商品是否存在
        product = self.db.query(ProductMain).filter(
            ProductMain.id == comment_data.product_id,
            ProductMain.is_deleted == 0
        ).first()

        if not product:
            raise HTTPException(status_code=404, detail="商品不存在")

        # 2. 创建评论
        new_comment = ProductComment(
            product_id=comment_data.product_id,
            user_id=user_id.id,
            username=user_id.username,
            content=comment_data.content,
            score=comment_data.score,
        )
        # gegnxin dingdanbiao
        self.db.query(OrderMain).filter(
            OrderMain.id == comment_data.order_id,  # 订单ID
            OrderMain.user_id == user_id.id        # 防止越权
        ).update({
            "is_commented": 1  # 1 = 已评论
        })
        self.db.add(new_comment)
        self.db.commit()
        self.db.refresh(new_comment)  # 刷新获取数据库生成的ID

        return new_comment
