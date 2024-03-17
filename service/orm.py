from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from service.config import orm_config


def setup_orm(app: FastAPI):
    register_tortoise(
        app,
        config=orm_config,
        generate_schemas=True,
        add_exception_handlers=True,
    )
