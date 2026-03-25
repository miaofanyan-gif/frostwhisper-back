from sqlalchemy import create_engine  # 必须从顶层导入
from sqlalchemy.orm import Session, sessionmaker
from redis.asyncio import Redis, ConnectionPool
from app.config.config import settings

from typing import Optional, Generator
from fastapi import Depends, HTTPException, status, Header
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.future import select

from app.models.user import UserMain as User  # 你的数据库模型
from .token import TokenPayload  # 你的 Token Payload Schema

# MySQL 异步引擎 (使用 asyncmy 驱动) [cite: 49, 74]
engine = create_engine(settings.MYSQL_URL, pool_pre_ping=True, echo=True)
# 使用标准的 sessionmaker
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# Redis 异步连接池
redis_pool = ConnectionPool.from_url(settings.REDIS_URL, decode_responses=True)


def get_db() -> Generator[Session, None, None]:
    """数据库会话同步依赖注入"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis() -> Redis:
    """Redis 同步客户端获取"""
    # 同步 Redis 库通常直接返回实例
    return Redis(connection_pool=redis_pool)


def get_current_user(
    db: Session = Depends(get_db),
    # 从 Header 中提取 Authorization: Bearer <TOKEN>
    authorization: Optional[str] = Header(None)
) -> User:
    """
    JWT 核心校验逻辑：
    1. 提取 Token
    2. 解密并验证有效期
    3. 从数据库获取对应用户
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    token = authorization.replace("Bearer ", "").strip()

    try:
        # 解码 JWT
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        # 验证 Payload 格式
        token_data = TokenPayload(**payload)
        if token_data.sub is None:
            raise HTTPException(
                status_code=401, detail="Invalid token payload")

    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    # 根据 JWT 中的 sub (用户ID) 查询数据库
    result = db.execute(select(User).filter(User.id == token_data.sub))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
