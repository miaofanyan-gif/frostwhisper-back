import uuid
from sqlalchemy import select, func, desc
import time
from redis import Redis
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, selectinload
from typing import List, Optional
from app.models.order import OrderMain, OrderItem
from app.schemas.order import OrderCreate
from app.models.ShoppingCart import ShoppingCart
from app.models.goods import ProductMain
from fastapi import HTTPException
from app.models.user import UserAddress
import os
redis_client = Redis(host='localhost', port=6379, db=2)


class OrderService:
    def __init__(self, db: Session, user_id: int):
        self.db = db
        self.user_id = user_id

    # 生成唯一订单号
    def generate_order_no(self):
        return str(uuid.uuid4().int)[:10]

    # 从购物车创建订单
    def create_order(self, data: OrderCreate):

        # 1. 查询选中的购物车商品
        cart_items = self.db.query(ShoppingCart).filter(
            ShoppingCart.id.in_(data.cart_ids),
            ShoppingCart.user_id == self.user_id,
            ShoppingCart.is_deleted == 0
        ).all()

        if not cart_items:
            raise HTTPException(
                status_code=400, detail="selected cart items not found")

        address = self.db.query(UserAddress).filter(
            UserAddress.id == data.address_id,
            UserAddress.user_id == self.user_id
        ).first()

        if not address:
            raise HTTPException(
                status_code=400, detail="shipping address not found")
        # 2. 计算金额
        total_amount = sum((item.product.price * item.quantity +
                           item.product.deposit * item.quantity) for item in cart_items)
        pay_amount = total_amount

        # 3. 创建订单主表
        order = OrderMain(
            order_no=self.generate_order_no(),
            user_id=self.user_id,
            total_amount=total_amount,
            pay_amount=pay_amount,
            # ====================== 从地址表复制字段 ======================
            consignee=address.consignee,        # 收件人
            address=address.address,      # 详细地址
            country_code=address.country_code,  # 国家代码
            state=address.state,          # 州/省
            city=address.city,            # 城市
            zip_code=address.zip_code,         # 邮编
            order_status=0,
            pay_status=0,
            # 新增字段
            is_rent=0,
            deposit=sum(item.deposit *
                        item.quantity for item in cart_items),
        )
        self.db.add(order)
        self.db.flush()
        # 4. 创建订单商品表
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                order_no=order.order_no,
                product_id=item.product_id,
                product_name=item.product.name,
                product_image=item.product.cover,
                price=item.product.price,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity,
                # 新增字段
                is_rent=item.is_rent,
                deposit=item.deposit,
                rent_date=item.rent_date

            )

            order_item.is_rent = item.is_rent or order_item.is_rent
            self.db.add(order_item)

        # 5. 删除购物车
        for item in cart_items:
            item.is_deleted = 1

        self.db.commit()
        return order

    # 获取我的订单列表
    def get_my_orders(self, page: int = 1, size: int = 10):
        query = self.db.query(OrderMain).filter(
            OrderMain.user_id == self.user_id,
            OrderMain.is_deleted == 0
        ).order_by(OrderMain.id.desc())

        total = query.count()
        order_main_list = query.offset((page - 1) * size).limit(size).all()

        return {
            "items": order_main_list,
            "total": total,
            "page": page,
            "page_size": size
        }

    # 取消订单（仅待付款可取消）
    def cancel_order(self, order_id: int):
        order = self.db.query(OrderMain).filter(
            OrderMain.id == order_id,
            OrderMain.user_id == self.user_id,
            OrderMain.order_status == 0
        ).first()

        if not order:
            raise HTTPException(status_code=400, detail="订单不可取消")

        order.order_status = 4
        self.db.commit()
        return {"message": "cancel successful"}

    def pay(self, order_id: int):
        order = self.db.query(OrderMain).filter(
            OrderMain.id == order_id,
            OrderMain.user_id == self.user_id,
            OrderMain.order_status == 0
        ).first()

        # ===================== 新增：支付前统一校验所有商品库存（不够直接失败） =====================
        order_items = self.db.query(OrderItem).filter(
            OrderItem.order_id == order_id).all()

        for item in order_items:
            product = self.db.query(ProductMain).filter(
                ProductMain.id == item.product_id).first()
            if not product:
                raise HTTPException(
                    status_code=400, detail=f"Product {item.product_id} does not exist")

            # 库存 < 购买数量 → 禁止支付
            if product.stock < item.quantity:
                raise HTTPException(
                    status_code=400, detail=f"Insufficient stock for product: {product.name}, remaining stock: {product.stock}")
        # ==========================================================================================

        # ===================== 原有逻辑不动 =====================
        order.order_status = 1
        order.pay_status = 2
        order.pay_type = 1

        # ===================== 新增：支付成功扣减库存 =====================
        for item in order_items:
            product = self.db.query(ProductMain).filter(
                ProductMain.id == item.product_id).first()
            if product:
                product.stock -= item.quantity
                if product.stock < 0:
                    product.stock = 0
        # ==========================================================

        self.db.commit()
        return {"message": "pay successful"}

    def confirm_receipt(self, order_id: int):
        order = self.db.query(OrderMain).filter(
            OrderMain.id == order_id,
            OrderMain.user_id == self.user_id,
            OrderMain.order_status == 1
        ).first()
        order.order_status = 3

        self.db.commit()
        return {"message": "confirm receipt successful"}

    def detail(self, order_id: int):
        order = self.db.query(OrderMain).filter(
            OrderMain.id == order_id
        ).first()

        URL = os.getenv("URL", "http://127.0.0.1:8000")
        for item in order.items:
            if (item.product_image):
                item.product_image = URL+item.product_image

        return order
