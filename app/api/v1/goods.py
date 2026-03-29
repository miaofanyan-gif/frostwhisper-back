from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.schemas.goods import ProductCreate, CommentCreate, ProductComment, ProductPaginationResponse, ProdoctDetailMain
from sqlalchemy.orm import Session
from app.services.goods_service import GoodsService

from app.utils.response import UnifiedResponse
from app.core.deps import get_db, get_current_user, get_redis
from pydantic import BaseModel


router = APIRouter(prefix="", tags=["goods"])

# 建立 Pydantic 模型


# --------------------------
# 1. 模型：和你传的 JSON 内部结构一致
# --------------------------
class ProductFilter(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 10
    shape_system: Optional[List[str]] = None
    dynasty_style: Optional[List[str]] = None
    gender: Optional[List[str]] = None
    usage_scene: Optional[List[str]] = None
    structure: Optional[List[str]] = None
    warehouse: Optional[List[str]] = None
    body_fit: Optional[List[str]] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    rent_or_buy: Optional[List[str]] = None


# --------------------------
# 2. 外层模型：对应你传的 { "params": ... }
# --------------------------


class ProductRequest(BaseModel):
    params: ProductFilter  # 关键！你传的是 params 包裹的


@router.post("/")
def get_all_products(

    # 筛选参数
    request: ProductRequest,  # 接收外层


    # 分页
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=50),

    db: Session = Depends(get_db)
):

    # 前端传来的数组
    rent_or_buy = request.params.rent_or_buy or []

    # 2. 转换成布尔值
    is_rental = "rent" in rent_or_buy

    # 3. 转成字典
    filter_params = request.params.dict()
    if rent_or_buy is not None and len(rent_or_buy) > 0:

        # 4. 把计算好的结果放入过滤参数
        filter_params["is_rental_available"] = is_rental

    # 转换规则：有 rent → True，否则 False
    service = GoodsService(db, get_redis())
    return UnifiedResponse.success(
        service.list_products(filter_params=filter_params,
                              page=request.params.page, page_size=request.params.page_size)
    )
# 提交评论


@router.post("/comment/add", response_model=UnifiedResponse[ProductComment])
def add_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
):
    service = GoodsService(db, get_redis())
    return UnifiedResponse.success(service.create_comment(comment, user_id=user_id))


@router.get("/{product_id}", response_model=UnifiedResponse[ProdoctDetailMain])
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):

    service = GoodsService(db, get_redis())
    return UnifiedResponse.success(service.get_product(product_id=product_id))

# 提交评论
