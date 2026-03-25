import json
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.future import select
from sqlalchemy import update, delete, func
from redis import asyncio as aioredis
from app.models.goods import ProductMain
import logging
from app.models.goods import ProductComment
from app.schemas.goods import CommentCreate
from fastapi import HTTPException


CACHE_KEY_PREFIX = "fw:product:"


class GoodsService:
    def __init__(self, db: Session, redis: aioredis.Redis):
        self.db = db
        self.redis = redis

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
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

        return items

    def list_products(self, keyword: str = None, category: int = None, scene: int = None, min_price: float = None,
                      page: int = 1,          # 默认第 1 页
                      page_size: int = 10     # 默认每页 10 条
                      ):
        # 多维度筛选实现 [cite: 15, 51]
        query = select(ProductMain).where(ProductMain.is_deleted == 0)
        if category:
            query = query.where(ProductMain.category_id == category)
        if scene:
            query = query.where(ProductMain.scene_id == scene)
        if min_price:
            query = query.where(ProductMain.base_price >= min_price)
        # 2. 🔍 搜索功能（名称/编号/品牌）
        if keyword:
            query = query.filter(
                or_(
                    ProductMain.name.like(f"%{keyword}%"),
                    ProductMain.name_cn.like(f"%{keyword}%"),
                    ProductMain.name_en.like(f"%{keyword}%"),
                    ProductMain.brand.like(f"%{keyword}%"),
                    ProductMain.product_sn.like(f"%{keyword}%")
                )
            )

        # 3. ✅ 关联查询：预加载图片（解决你之前的报错！）
        query = query.options(
            selectinload(ProductMain.images)  # 关键：加载商品图片表
        )

        offset_value = (page - 1) * page_size

        # 4. 应用分页查询
        # 建议加上 order_by 确保分页顺序稳定
        paginated_query = query.order_by(ProductMain.id.desc()).offset(
            offset_value).limit(page_size)

        # 执行查询
        result = self.db.execute(paginated_query)

        items = result.scalars().all()

        # 5. (可选) 获取总条数，用于前端显示总页数
        total_count_query = select(func.count()).select_from(query.subquery())
        total = self.db.execute(total_count_query).scalar()
        result = []
        for p in items:
            # 取封面图
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
                "market_price": p.market_price,
                "dynasty_style": p.dynasty_style,
                "is_rental_available": p.is_rental_available == 1,
                "is_customizable": p.is_customizable == 1,
                "cover_image": cover_image,
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

        self.db.add(new_comment)
        self.db.commit()
        self.db.refresh(new_comment)  # 刷新获取数据库生成的ID

        return new_comment
