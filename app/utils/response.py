from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request, status
from typing import TypeVar, Generic, Optional, Any
from pydantic import BaseModel


# 定义一个泛型变量 T
T = TypeVar("T")


class UnifiedResponse(BaseModel, Generic[T]):
    """
    改写为继承 BaseModel 和 Generic，支持下标操作 [T]
    """
    code: int = 200        # 给个默认值
    message: str = "success"  # 给个默认值
    data: Optional[T] = None

    @staticmethod
    def success(data: Any = None, message: str = "Success") -> "UnifiedResponse":
        return UnifiedResponse(code=200, message=message, data=data)

    @staticmethod
    def fail(code: int = 400, message: str = "Error", data: Any = None) -> "UnifiedResponse":
        return UnifiedResponse(code=code, message=message, data=data)
