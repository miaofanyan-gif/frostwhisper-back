from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.schemas.goods import ProductCreate, ProductPaginationResponse
from sqlalchemy.orm import Session
from app.services.goods_service import GoodsService

from app.utils.response import UnifiedResponse
from app.core.deps import get_db, get_current_user, get_redis

router = APIRouter(prefix="", tags=["Goods"])


@router.get("/")
def get_all_products(
    category: Optional[int] = Query(None, description="品类ID"),
    scene: Optional[int] = Query(None, description="场景ID"),
    db: Session = Depends(get_db)
):

    service = GoodsService(db,  get_redis())
    return UnifiedResponse.success(service.list_products(category=category, scene=scene))


@router.get("/{product_id}")
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):

    service = GoodsService(db, get_redis())
    return UnifiedResponse.success(service.get_product(product_id=product_id))
