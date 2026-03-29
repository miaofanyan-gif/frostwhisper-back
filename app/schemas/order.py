# 基础 Schema

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any, List
from datetime import datetime
from decimal import Decimal
from app.schemas.goods import ProductResponse

import enum

# 1. 必须先定义枚举，或者从 constants 导入


# 订单项
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

# 创建订单请求


class OrderCreate(BaseModel):
    # receiver_name: str
    # receiver_phone: str
    # receiver_address: str
    cart_ids: List[int]  # 购物车ID列表
    address_id: int


# 订单项响应


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_image: Optional[str] = None
    price: Decimal
    quantity: int
    total_price: Decimal
    deposit: Optional[Decimal] = None
    rent_date: Optional[int] = None
    is_rent: int

    class Config:
        orm_mode = True

# 订单响应


class OrderResponse(BaseModel):
    id: int
    order_no: str
    total_amount: Decimal
    pay_amount: Decimal
    order_status: int
    pay_status: int
    create_time: datetime

    consignee: str | None = None
    address: str | None = None
    country_code: str | None = None
    state: str | None = None
    city: str | None = None
    zip_code: str | None = None

    is_commented: int
    deposit: Optional[Decimal] = None
    is_rent: int
    items: List[OrderItemResponse] = []

    class Config:
        orm_mode = True

# 统一分页响应


class OrderResponse(BaseModel):
    id: int
    order_no: str
    total_amount: float
    pay_amount: float
    order_status: int
    create_time: datetime
    consignee: str | None = None
    address: str | None = None
    country_code: str | None = None
    state: str | None = None
    city: str | None = None
    zip_code: str | None = None
    items: List[OrderItemResponse] = []
    deposit: Optional[Decimal] = None
    is_rent: int
    is_commented: int

    class Config:
        orm_mode = True


class OrderListResponse(BaseModel):
    total: int
    items: List[OrderResponse]


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    price: Optional[float] = None
    quantity: Optional[int] = None
    total_amount: float
    currency: Optional[str] = None
    consignee: str | None = None
    address: str | None = None
    country_code: str | None = None
    state: str | None = None
    city: str | None = None
    zip_code: str | None = None
    is_commented: int
    deposit: Optional[Decimal] = None
    rent_date: Optional[int] = None
    is_rent: int

    class Config:
        orm_mode = True


class PaginatedResponse(BaseModel):
    items: List[OrderResponse]  # 订单列表
    total: int             # 总条数
    page: int              # 当前页码
    page_size: int         # 每页条数
