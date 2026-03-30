from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    # 基础配置
    PROJECT_NAME: str = "Frostwhisper Hanfu API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # 核心字段 (补上报错中提到的字段)
    ENV: str = "dev"
    DEFAULT_CURRENCY: str = "CNY"
    SUPPORTED_CURRENCIES: List[str] = ["CNY", "USD", "EUR", "JPY"]

    # 数据库与 Redis [cite: 264, 285]
    MYSQL_URL: str
    REDIS_URL: str

    # JWT [cite: 262, 267]
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    CORS_ORIGINS: List[str] = ["*"]

    # 关键配置：让 Pydantic 忽略 .env 中多余的字段，防止报错
    model_config = SettingsConfigDict(
        env_file=".env.prod",
        extra="ignore"  # 允许忽略 .env 中未定义的字段
    )


settings = Settings()
