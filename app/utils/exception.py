class ExceptionMiddleware(BaseHTTPMiddleware):
    """全局异常拦截中间件"""

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            # 记录日志 (省略logger逻辑)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=UnifiedResponse.fail(
                    500, f"Internal Server Error: {str(e)}")
            )
