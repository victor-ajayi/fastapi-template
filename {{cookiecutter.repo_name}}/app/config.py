import secrets
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALGORITHM: str
    POSTGRES_URL: str
    DB_URL: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


@lru_cache
def get_settings():
    return Settings(_env_file=".env")


settings = get_settings()
