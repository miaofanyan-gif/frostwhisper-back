from pydantic import BaseModel, EmailStr, Field, validator, computed_field
from typing import Optional, List
from app.models.constants import UserLayerEnum, MemberLevelEnum


class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    email: EmailStr
    phone: int
    user_tag: UserLayerEnum = UserLayerEnum.NEWBIE


class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)


class UserInfoRead(BaseModel):
    id: int
    username: str
    phone: int
    email: EmailStr
    user_tag: UserLayerEnum
    member_level: str
    points: int
    growth_value: int
    # 使用 Pydantic 的序列化转换

    @computed_field  # 必须加这个，前端才能收到 user_tag_name
    @property
    def user_tag_name(self) -> str:
        tag_map = {
            1: "Standard User",  # 或者 Regular User
            2: "Premium Member",  # 或者 Pro Member
            3: "Administrator"   # 简称 Admin
        }
        return tag_map.get(self.user_tag, f"未知标签({self.user_tag})")

    class Config:
        from_attributes = True


class AddressCreate(BaseModel):
    consignee: str
    country_code: str
    state: str
    city: str
    address: str
    zip_code: str
    is_default: bool = False

    class Config:
        from_attributes = True


class AddressOut(AddressCreate):
    id: int
    user_id: int
    # AddressCreate 里的字段会自动继承过来
