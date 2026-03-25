from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session


from typing import Optional, List
from datetime import datetime
import app.core.deps as deps
from app.schemas.order import OrderCreateSchema, OrderStatus, OrderType
from app.services.shoppingcart import CartService
from app.schemas.shoppingcart import CartAdd, CartItemResponse, CartListResponse, CartUpdate
from app.utils.response import UnifiedResponse
from app.schemas.order import PaginatedResponse
from app.core.deps import get_db, get_current_user, get_redis


router = APIRouter(prefix="", tags=["shoppingcart"])

# 添加商品到购物车


@router.post("/add", response_model=UnifiedResponse[CartItemResponse])
def add_cart(
    data: CartAdd,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CartService(db, current_user.id)
    return UnifiedResponse.success(service.add_to_cart(data.product_id, data.quantity))

# 获取购物车列表


@router.get("/list")
def get_cart(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CartService(db, current_user.id)
    return UnifiedResponse.success(service.get_cart_list())

# 更新购物车项


@router.patch("/{cart_id}", response_model=UnifiedResponse[CartItemResponse])
def update_cart(
    cart_id: int,
    data: CartUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CartService(db, current_user.id)
    return UnifiedResponse.success(service.update_cart_item(cart_id, data))


# 删除购物车项


@router.delete("/{cart_id}")
def delete_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CartService(db, current_user.id)
    return UnifiedResponse.success(service.delete_cart_item(cart_id))
