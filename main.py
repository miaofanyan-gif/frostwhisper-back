import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import settings
from app.middleware.exception import ExceptionMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.responses import JSONResponse
# 在 main.py 中添加商品模块路由
from app.api.v1.goods import router as goods_router
from app.api.v1.users import router as users_router
from app.api.v1.order import router as order_router
from app.api.v1.shoppingcart import router as shoppingcart_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles  # 关键导入


app = FastAPI(title="Frostwhisper Hanfu API", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"]  # 允许所有请求头

)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

#


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "code": 422,
            "message": exc.errors()[0]["msg"],
            "data": exc.errors()
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "message": exc.detail,
            "data": None
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "code": 500,
            "message": f"Global Error: {str(exc)}",
            "data": None
        },
    )


# 包含用户模块路由
app.include_router(
    goods_router,
    prefix=f"{settings.API_V1_STR}/products",
    tags=["goods"]
)
# 用户模块路由：
app.include_router(
    users_router,
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"]
)
# 包含用户模块路由
app.include_router(
    order_router,
    prefix=f"{settings.API_V1_STR}/orders",
    tags=["orders"]
)

app.include_router(
    shoppingcart_router,
    prefix=f"{settings.API_V1_STR}/cart",
    tags=["shoppingcart"]
)


@app.get("/", tags=["system"])
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}", "env": settings.ENV}


@app.get("/routes")
async def get_all_routes():
    url_list = [
        {"path": route.path, "name": route.name,
            "methods": list(route.methods)}
        for route in app.routes
        if hasattr(route, "methods")
    ]
    return url_list


@app.get("/health")
async def health_check():
    """健康检查：确认服务及跨境网络状态 [cite: 97]"""
    return {"status": "online", "region": "Global"}

if __name__ == "__main__":
    # 使用 Uvicorn+Gunicorn 部署模式 [cite: 85]
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
