from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
            return response
        # 捕获 FastAPI 参数校验错误（422 错误）
        except RequestValidationError as e:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "code": 422,
                    "message": "参数校验失败",
                    "data": e.errors()  # 可以保留详细错误信息
                }
            )
        # 捕获其他所有异常（500 错误）
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "code": 500,
                    "message": f"Global Error: {str(e)}",
                    "data": None
                }
            )
