from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    """
    所有 SQLAlchemy 模型的基类
    AsyncAttrs 确保模型支持异步属性访问
    """
    pass
