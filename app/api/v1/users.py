from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import app.core.deps as deps
from app.schemas.users import UserRegister, UserInfoRead, AddressCreate, UserLogin, AddressOut
from app.services.user_service import UserService
from app.models.user import UserMain
from app.utils.response import UnifiedResponse
from app.config.config import settings
from app.core.security import create_access_token
from datetime import timedelta
router = APIRouter()


@router.post("/register", response_model=UnifiedResponse[UserInfoRead])
def register(user_in: UserRegister, db: Session = Depends(deps.get_db)):
    """用户注册：支持选择初始分层标签"""

    user = UserService.register_user(db, user_in)
    return UnifiedResponse.success(data=user)


@router.post("/login")
def login(
    login_data: UserLogin,
    db: Session = Depends(deps.get_db)
):
    """用户登录接口"""
    # 1. 验证身份
    user = UserService.authenticate(db, login_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password is incorrect",
        )

    # 2. 生成 Token (通常 sub 字段存用户 ID 或唯一标识)
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UnifiedResponse[UserInfoRead])
def get_current_user_info(
    current_user: UserMain = Depends(deps.get_current_user)
):
    """
    获取当前登录用户信息及会员状态
    """
    # 1. 基础状态防御：检查账号是否被冻结
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="have been frozen, please contact support"
        )
    current_user = UserInfoRead.model_validate(current_user)
    # 2. 逻辑增强：如果 current_user 只是基础信息，
    # 可能需要额外查询数据库获取最新的会员状态
    # current_user = await user_service.get_full_info(user_id=current_user.id)

    # 3. 数据安全：UnifiedResponse.success 内部应确保 data 经过了 UserOut 过滤
    return UnifiedResponse.success(data=current_user)


@router.post("/addaddress")
def add_address(
    addr_in: AddressCreate,
    db: Session = Depends(deps.get_db),
    user: UserMain = Depends(deps.get_current_user)
):
    """添加收货地址：敏感地址字段加密存储"""
    new_address = UserService.add_address(
        db=db,
        user_id=user.id,
        address_in=addr_in
    )
    res_data = AddressOut.model_validate(new_address).model_dump()
    return UnifiedResponse.success(data=res_data)


@router.get("/address", response_model=UnifiedResponse[List[AddressOut]])
def list_address(
    db: Session = Depends(deps.get_db),
    user: UserMain = Depends(deps.get_current_user)
):
    """添加收货地址：敏感地址字段加密存储"""
    res_data = UserService.get_user_addresses(
        db=db,
        user_id=user.id
    )
    return UnifiedResponse.success(data=res_data)


@router.get("/set-address-default/{order_id}", response_model=UnifiedResponse[AddressOut])
def reset_default_address(
    db: Session = Depends(deps.get_db),
    user: UserMain = Depends(deps.get_current_user)
):
    """添加收货地址：敏感地址字段加密存储"""
    res_data = UserService.reset_default_address(
        db=db,
        user_id=user.id
    )
    return UnifiedResponse.success(data=res_data)
