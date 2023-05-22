from typing import Any
from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_URL: str | None = None

    @validator("POSTGRES_URL", pre=True)
    def build_postgres_url(cls, v: str | None, values: dict[str, Any]) -> str:
        if v:
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            path="/{}".format(values["POSTGRES_DB"]),
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
