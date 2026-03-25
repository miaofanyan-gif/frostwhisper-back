from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session


from typing import Optional, List
from datetime import datetime
import app.core.deps as deps
from app.schemas.order import OrderCreateSchema, OrderStatus, OrderType
from app.services.order_service import OrderService
from app.utils.response import UnifiedResponse
from app.schemas.order import PaginatedResponse


router = APIRouter()


@router.post("/create")
def place_order(payload: OrderCreateSchema, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):

    order = OrderService.create_order(db, current_user.id, payload)

    return UnifiedResponse.success(data=order)


@router.get("/", response_model=UnifiedResponse[PaginatedResponse])
def list_orders(
    order_type: Optional[str] = None,
    status: Optional[int] = None,
    page: int = 1,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user)
):

    # 调用 Service
    result = OrderService.get_order_list(
        db,
        user_id=current_user.id,
        order_type=order_type,
        status=status,
        page=page
    )
    return UnifiedResponse.success(data=result)


@router.get("/detail/{order_id}")
def get_detail(
    order_id: str,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user)
):
    order = OrderService.get_order_detail(
        db, order_id, user_id=current_user.id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"code": 200, "data": order}


@router.put("/{order_id}/cancel")
def cancel_order(order_id: int,   db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):

    order = OrderService.get_order_detail(
        db, order_id, user_id=current_user.id)
    return UnifiedResponse.success(data=order)
