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


class RelatedProductItem(BaseModel):
    id: int
    name: str
    name_en: Optional[str] = None
    price: Decimal
    cover: Optional[str] = None
    gender: Optional[str] = None
    dynasty_style: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True


class ProductBase(BaseModel):
    name_cn: str
    name_en: str
    category_id: int
    scene_id: int
    dynasty_style: Optional[str] = None
    fabric_info: Optional[str] = None
    base_price: Decimal = Field(..., gt=0)
    deposit: Decimal = Field(..., gt=0)
    is_rental_available: bool = False


class ProductCreate(ProductBase):
    is_rental_available: bool = False
    is_customizable: bool = False

# 图片子 Schema


class ProductImage(BaseModel):
    id: int
    url: str
    is_cover: int

    class Config:
        orm_mode = True

# SKU 子 Schema


class ProductSku(BaseModel):
    id: int
    color: str
    size: str
    price: float
    stock: int

    class Config:
        orm_mode = True


class ProductResponse(ProductBase):
    id: int
    product_sn: str
    name: str
    name_cn: Optional[str] = None
    name_en: Optional[str] = None
    cover_image: Optional[str] = None
    price: float
    deposit: Optional[float] = None
    brand: Optional[str] = None
    dynasty_style: Optional[str] = None
    is_rental_available: bool
    is_customizable: bool
    category_id: int
    category_name: Optional[str] = None
    status: int
    stock: int
    category: Optional[int] = None
    shape_system: Optional[str] = None
    dynasty_style: Optional[str] = None
    gender: Optional[str] = None
    usage_scene: Optional[str] = None
    structure: Optional[str] = None
    warehouse: Optional[str] = None
    body_fit: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True


class ProductComment(BaseModel):
    id: Optional[int] = None
    product_id: Optional[int] = None
    score: Optional[int] = None
    content: Optional[str] = None
    user_id: Optional[int] = None
    username: Optional[str] = None

    class Config:
        orm_mode = True


class ProdoctDetailMain(ProductResponse):

    images: List[ProductImage] = []  # ✅ 关联图片
    skus: List[ProductSku] = []      # ✅ 关联SKU
    comments: Optional[List[ProductComment]] = None
    related_products: List[RelatedProductItem] = []


class ProductPaginationResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    page_size: int

    class Config:
        from_attributes = True  # 确保能从 SQLAlchemy 对象转换


# 前端提交评论用的模型
class CommentCreate(BaseModel):
    product_id: int  # 商品ID
    order_id: int
    content: str = Field(min_length=1, max_length=500)  # 评论内容
    score: Optional[int] = Field(None, ge=1, le=5)  # 1-5星评分

    class Config:
        orm_mode = True


# 扩展商品详情 = 包含【关联商品列表】
class ProductDetailWithRelated(ProdoctDetailMain):
    related_products: List[RelatedProductItem] = []
