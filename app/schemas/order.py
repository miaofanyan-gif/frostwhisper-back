# 基础 Schema

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any, List
from datetime import datetime
from decimal import Decimal
from app.schemas.goods import ProductResponse

import enum

# 1. 必须先定义枚举，或者从 constants 导入


class OrderType(str, enum.Enum):
    PURCHASE = "Purchase"
    RENTAL = "Rental"
    CUSTOM = "Custom"


class OrderStatus(int, enum.Enum):
    PENDING = 0
    PAID = 1
    SHIPPED = 3
    COMPLETED = 4
    CANCELLED = 5

# 2. 然后再在 Schema 中引用


class OrderBase(BaseModel):
    order_type: OrderType
    total_amount: Decimal = Field(..., max_digits=12, decimal_places=2)
    currency: str = "USD"
    shipping_address: Optional[str] = None


class OrderCreateSchema(OrderBase):
    idempotency_key: str  # 幂等性校验用
    user_id: int
    price: Decimal = Field(..., gt=0)
    deposit: Optional[Decimal] = None  # 租赁订单的押金
    rental_days: Optional[int] = None  # 租赁订单的租期
    custom_requirements: Optional[str] = None  # 定制订单的需求描述
    payment_id: Optional[str] = None  # 模拟支付ID
    # 差异化字段存入 extra_info
    extra_info: Optional[Dict[str, Any]] = Field(
        default=None,
        description="租赁订单存 {'days': 7, 'deposit': 100}，定制存 {'size': 'L'}"
    )


class OrderResponse(OrderBase):
    id: int
    order_sn: str
    order_status: int
    create_time: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    order_type: OrderType
    total_amount: Decimal
    currency: str = "USD"
    shipping_address: Optional[str] = None

# 创建订单时的输入校验


class OrderCreate(OrderBase):
    item_id: int
    idempotency_key: str  # 幂等性校验 Key

    # 租赁订单特有
    rental_days: Optional[int] = None
    deposit: Optional[Decimal] = None

    # 定制订单特有
    custom_requirements: Optional[str] = None


class OrderItemBase(BaseModel):
    product_id: Optional[int] = None
    product_name: str
    price: Optional[float] = None
    quantity: Optional[int] = None
    total_amount: float
    currency: str

    class Config:
        orm_mode = True


class OrderItemVO(OrderItemBase):
    id: int
    order_id: int
    order_sn: str
    combo_id: Optional[int] = None
    create_time: datetime
    product: Optional[ProductResponse] = None  # 嵌套商品

    # 返回给前端的订单详情


class OrderRead(OrderBase):
    id: int
    user_id: int
    total_amount: Decimal
    currency: str
    order_type: str
    order_status: int
    shipping_address: Optional[str] = None
    create_time: datetime
    update_time: datetime
    deposit: Optional[Decimal] = None  # 租赁订单的押金
    rental_days: Optional[int] = None  # 租赁订单的租期
    custom_requirements: Optional[str] = None  # 定制订单的需求描述
    payment_id: Optional[str] = None  # 模拟支付ID

    order_items: List[OrderItemVO] = []  # ✅ 关键：嵌套订单项

    # 允许从 SQLAlchemy 对象直接转换
    model_config = ConfigDict(from_attributes=True)
    # 差异化字段存入 extra_info
    extra_info: Optional[Dict[str, Any]] = Field(
        default=None,
        description="租赁订单存 {'days': 7, 'deposit': 100}，定制存 {'size': 'L'}"
    )


class PaginatedResponse(BaseModel):
    items: List[OrderRead]  # 订单列表
    total: int             # 总条数
    page: int              # 当前页码
    page_size: int         # 每页条数
