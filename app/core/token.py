from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    # 通常 JWT 的 sub (subject) 存放用户 ID
    sub: Optional[int] = None
