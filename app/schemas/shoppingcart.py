from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, List
from app.schemas.goods import ProductResponse


# 1. 添加购物车请求模型


class CartAdd(BaseModel):
    product_id: int = Field(..., gt=0, description="商品ID必须大于0")
    quantity: int = Field(1, gt=0, description="商品数量必须大于0")

    class Config:
        orm_mode = True

# 2. 更新购物车数量/选中状态请求模型


class CartUpdate(BaseModel):
    quantity: Optional[int] = Field(None, gt=0, description="更新数量")
    rent_date: Optional[int] = Field(None, gt=0, description="租赁天数")
    selected: Optional[int] = Field(None, ge=0, le=1, description="0=未选中，1=选中")

    class Config:
        orm_mode = True

# 3. 购物车响应模型（包含关联商品信息）


class CartItemResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    selected: int
    is_rent: int
    deposit: Optional[float] = None
    rent_date: Optional[int] = None
    create_time: datetime
    update_time: datetime
    product: Optional[ProductResponse] = None  # 接受 ORM 对象

    class Config:
        from_attributes = True  # 确保能从 SQLAlchemy 对象转换
        orm_mode = True  # 关键：允许从 ORM 对象创建


class CartListResponse(BaseModel):
    total: int
    items: List[CartItemResponse]

    class Config:
        from_attributes = True  # 确保能从 SQLAlchemy 对象转换
        orm_mode = True  # 同样开启 ORM 模式
