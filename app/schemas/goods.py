from pydantic import BaseModel, Field, validator
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

# 模拟汇率（生产环境应从 Redis 或第三方 API 获取）
EXCHANGE_RATES = {
    "CNY": Decimal("7.2"),
    "EUR": Decimal("0.92"),
    "USD": Decimal("1.0")
}


class ProductBase(BaseModel):
    name_cn: str
    name_en: str
    category_id: int
    scene_id: int
    dynasty_style: Optional[str] = None
    fabric_info: Optional[str] = None
    base_price: Decimal = Field(..., gt=0)


class ProductCreate(ProductBase):
    is_rental_available: bool = False
    is_customizable: bool = False


class ProductResponse(ProductBase):
    id: int
    product_sn: str
    name: str
    name_cn: Optional[str] = None
    name_en: Optional[str] = None
    cover_image: Optional[str] = None
    price: float
    market_price: Optional[float] = None
    brand: Optional[str] = None
    dynasty_style: Optional[str] = None
    is_rental_available: bool
    is_customizable: bool
    category_id: int
    category_name: Optional[str] = None
    status: int
    create_time: datetime

    class Config:
        orm_mode = True


# 定义分页返回结构


class ProductPaginationResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    page_size: int

    class Config:
        from_attributes = True  # 确保能从 SQLAlchemy 对象转换
