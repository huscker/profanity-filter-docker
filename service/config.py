import logging
import os
from typing import Optional

import lazy_object_proxy
from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Config(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DATABASE: str
    POSTGRES_URL: Optional[PostgresDsn] = None

    REDIS_USER: str = ""
    REDIS_PASSWORD: str = ""
    REDIS_HOST: str
    REDIS_PORT: int = 6379
    REDIS_DATABASE: int = 0
    REDIS_URL: Optional[RedisDsn] = None

    WORDLIST_CACHE_TTL: int = 10

    TORTOISE_ORM: Optional[dict] = None

    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

    @model_validator(mode="before")
    def assemble_postgres_db_url(self) -> "Config":
        self["POSTGRES_URL"] = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self["POSTGRES_USER"],
            password=self["POSTGRES_PASSWORD"],
            host=self["POSTGRES_HOST"],
            port=int(self["POSTGRES_PORT"]),
            path=f'{self["POSTGRES_DATABASE"]}',
        )
        return self

    @model_validator(mode="before")
    def assemble_redis_postgres_db_url(self) -> "Config":
        self["REDIS_URL"] = RedisDsn.build(
            scheme="redis",
            host=self["REDIS_HOST"],
            username=self["REDIS_USER"],
            password=self["REDIS_PASSWORD"],
            port=int(self["REDIS_PORT"]),
            path=f"{self['REDIS_DATABASE']}",
        )
        return self

    @model_validator(mode="before")
    def assemble_tortoise_orm_conf(self) -> "Config":
        self["TORTOISE_ORM"] = {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": self["POSTGRES_HOST"],
                        "port": int(self["POSTGRES_PORT"]),
                        "user": self["POSTGRES_USER"],
                        "password": self["POSTGRES_PASSWORD"],
                        "database": self["POSTGRES_DATABASE"],
                    },
                },
            },
            "apps": {
                "models": {
                    "models": ["service.filtering.models", "service.word_lists.models", "aerich.models"],
                    "default_connection": "default",
                    "connection": "default",
                },
            },
            "use_tz": True,
            "timezone": "UTC",
        }
        return self

    class Config:
        env_file = ".env"
        extra = "ignore"


def get_config():
    return Config()


config: Config = lazy_object_proxy.Proxy(get_config)
orm_config: dict = lazy_object_proxy.Proxy(lambda: config.TORTOISE_ORM)
