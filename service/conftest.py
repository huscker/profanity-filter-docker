import pytest
from httpx import AsyncClient

from service.__main__ import app


@pytest.fixture
def client() -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://test")
