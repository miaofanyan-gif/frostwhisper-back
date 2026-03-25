from passlib.context import CryptContext
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from app.config.config import settings
import bcrypt

from jose import jwt

if not hasattr(bcrypt, "__about__"):
    bcrypt.__about__ = type("About", (), {"__version__": bcrypt.__version__})

# 配置加密环境
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
CIPHER_KEY = settings.SECRET_KEY  # 实际应存入.env
cipher_suite = Fernet(CIPHER_KEY)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def encrypt_data(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()


def decrypt_data(token: str) -> str:
    return cipher_suite.decrypt(token.encode()).decode()


def create_access_token(data: dict):
    """生成 JWT 令牌 """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str):
    """解析并校验 Token [cite: 47]"""
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except Exception:
        return None
