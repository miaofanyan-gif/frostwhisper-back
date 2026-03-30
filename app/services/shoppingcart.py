from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.ShoppingCart import ShoppingCart
from app.schemas.goods import ProductResponse
from app.models.goods import ProductMain
from app.schemas.shoppingcart import CartUpdate, CartItemResponse
import os


class CartService:
    def __init__(self, db: Session, user_id: int):
        self.db = db
        self.user_id = user_id

    # 添加商品到购物车
    def add_to_cart(self, product_id: int, quantity: int = 1):
        # 1. 检查商品是否存在
        product = self.db.query(ProductMain).filter(
            ProductMain.id == product_id,
            ProductMain.is_deleted == 0
        ).first()
        if not product:
            raise HTTPException(status_code=404, detail="goods not found")

        # 2. 检查购物车中是否已有该商品
        cart_item = self.db.query(ShoppingCart).filter(
            ShoppingCart.user_id == self.user_id,
            ShoppingCart.product_id == product_id,
            ShoppingCart.is_deleted == 0
        ).first()

        if cart_item:
            # 已有商品：累加数量
            cart_item.quantity += quantity
        else:
            # 新商品：创建购物车项
            cart_item = ShoppingCart(
                user_id=self.user_id,
                product_id=product_id,
                is_rent=product.is_rental_available,  # 是否可租赁
                deposit=product.deposit,  # 押金
                rent_date=7,
                quantity=quantity
            )
            self.db.add(cart_item)

        try:
            self.db.commit()
            self.db.refresh(cart_item)
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(
                status_code=500, detail="Failed to add to cart")
        return cart_item

    # 获取用户购物车列表（关联商品信息）
    def get_cart_list(self):
        cart_items = self.db.query(ShoppingCart).options(
            selectinload(ShoppingCart.product)  # 关键：加载关联商品
        ).filter(
            ShoppingCart.user_id == self.user_id,
            ShoppingCart.is_deleted == 0,
        ).all()

        # 转换为响应格式（包含商品信息）
        URL = os.getenv("URL")
        items = []
        for item in cart_items:
            item_dict = CartItemResponse.from_orm(item).dict()
            item_dict["product"] = {
                "id": item.product.id,
                "name": item.product.name,
                "price": item.product.price,
                "stock": item.product.stock,
                "is_rent_available": item.product.is_rental_available,
                "deposit": item.product.deposit,
                # 取第一张图
                "image": URL+item.product.images[0].url if item.product.images else None
            }
            items.append(item_dict)
        return {"total": len(items), "items": items}

    # 更新购物车项（数量/选中状态）
    def update_cart_item(self, cart_id: int, data: CartUpdate):
        cart_item = self.db.query(ShoppingCart).filter(
            ShoppingCart.id == cart_id,
            ShoppingCart.user_id == self.user_id,
            ShoppingCart.is_deleted == 0
        ).first()
        if not cart_item:
            raise HTTPException(status_code=404, detail="Cart item not found")

        if data.quantity is not None:
            cart_item.quantity = data.quantity
        if data.selected is not None:
            cart_item.selected = data.selected
        if data.rent_date is not None:
            cart_item.rent_date = data.rent_date

        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item

    # 删除购物车项（软删除）
    def delete_cart_item(self, cart_id: int):
        cart_item = self.db.query(ShoppingCart).filter(
            ShoppingCart.id == cart_id,
            ShoppingCart.user_id == self.user_id,
            ShoppingCart.is_deleted == 0
        ).first()
        if not cart_item:
            raise HTTPException(status_code=404, detail="Cart item not found")
        cart_item.is_deleted = 1
        self.db.commit()
        return {"message": "Cart item deleted"}
