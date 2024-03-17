import asyncio
from typing import Iterable

from tortoise.models import Model


async def save_batch(objects: Iterable[Model]) -> list[Model]:
    coroutines = [object.save() for object in objects]
    return await asyncio.gather(*coroutines)
