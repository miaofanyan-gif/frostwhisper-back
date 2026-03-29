from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user, get_redis
from app.models.user import UserMain
from app.schemas.order import OrderCreate, OrderResponse, OrderListResponse, OrderItemResponse
from typing import Optional, List
from datetime import datetime
import app.core.deps as deps
from app.services.order_service import OrderService
from app.utils.response import UnifiedResponse
from app.schemas.order import PaginatedResponse


router = APIRouter()


# 创建订单（从购物车）
@router.post("/create", response_model=UnifiedResponse[OrderResponse])
def create_order(
    data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return UnifiedResponse.success(service.create_order(data))

# 我的订单列表


@router.get("/my", response_model=UnifiedResponse[PaginatedResponse])
def get_my_orders(
    page: int = Query(1, ge=1),
    size: int = Query(10, le=50),
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return UnifiedResponse.success(service.get_my_orders(page, size))


@router.get("/{order_id}", response_model=UnifiedResponse[OrderResponse])
def detail(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return UnifiedResponse.success(service.detail(order_id))


@router.post("/{order_id}/pay")
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return UnifiedResponse.success(service.pay(order_id))


@router.post("/{order_id}/confirm-receipt")
def confirm_receipt(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return UnifiedResponse.success(service.confirm_receipt(order_id))


@router.post("/{order_id}/cancel")
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: UserMain = Depends(get_current_user)
):
    service = OrderService(db, current_user.id)
    return service.cancel_order(order_id)
