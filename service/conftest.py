import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient
from tortoise import Tortoise

from service.config import config
from service.entrypoints.api import app


@pytest.fixture
def client() -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://test")


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def initialize_tests(event_loop):
    await Tortoise.init(config=config.TORTOISE_ORM, _create_db=False)
    await Tortoise.generate_schemas()
    yield
    for model in Tortoise.describe_models().keys():
        if model != "models.Aerich":
            table_name = Tortoise.describe_models()[model]["table"]
            await Tortoise.get_connection("default").execute_query(f"TRUNCATE TABLE {table_name} CASCADE;")
