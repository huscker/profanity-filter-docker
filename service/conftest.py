import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient
from tortoise import Tortoise

from service.__main__ import app
from service.config import config


@pytest.fixture
def client() -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://test")


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def initialize_tests(event_loop):
    await Tortoise.init(config=config.TORTOISE_ORM, _create_db=True)
    await Tortoise.generate_schemas()
    yield
    await Tortoise._drop_databases()
