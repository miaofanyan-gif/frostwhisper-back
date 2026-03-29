from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session


from typing import Optional, List
from datetime import datetime
import app.core.deps as deps
from app.services.shoppingcart import CartService
from app.services.user_service import UserService
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
    car_list = service.get_cart_list()
    address_list = UserService.get_user_addresses(
        db=db,
        user_id=current_user.id
    )
    res = {}
    # 组装返回数据
    res_address = [
        {
            "id": addr.id,
            "consignee": addr.consignee,
            "country_code": addr.country_code,
            "state": addr.state,
            "city": addr.city,
            "address": addr.address,
            "zip_code": addr.zip_code,
            "is_default": addr.is_default,

            "user_id": addr.user_id
        } for addr in address_list
    ]

    res["carts"] = car_list
    res["address"] = res_address
    return UnifiedResponse.success(res)


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
