from pydantic import BaseModel, ConfigDict
from typing import Optional

# 基础模型：定义字段类型


class AddressBase(BaseModel):
    consignee: str
    country_code: str = "US"
    state: Optional[str] = None
    city: str
    address: str
    zip_code: Optional[str] = None
    is_default: bool = False

# 用于创建地址的输入模型


class AddressCreate(AddressBase):
    pass

# 用于 API 返回的输出模型 (含 ID)


class AddressRead(AddressBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
