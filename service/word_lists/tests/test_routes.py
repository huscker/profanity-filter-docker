import pytest

from service.test_utils import save_batch
from service.word_lists.models import Word
from service.word_lists.tests.factories import WordFactory, WordListFactory

pytestmark = [pytest.mark.asyncio]


class TestWordLists:
    async def test_list(self, client):
        word_list = WordListFactory.build()
        await word_list.save()

        response = await client.get("/api/word-list/all/")

        assert response.status_code == 200
        data = response.json()
        assert len(data["word_lists"]) == 1
        assert data["word_lists"][0]["id"] == word_list.id

    async def test_get(self, client):
        word_list = WordListFactory.build()
        await word_list.save()
        words = WordFactory.build_batch(10, word_list=word_list)
        await save_batch(words)

        response = await client.get(f"/api/word-list/{word_list.id}/")

        assert response.status_code == 200
        data = response.json()
        assert len(data["words"]) == 10

    async def test_update(self, client):
        word_list = WordListFactory.build()
        await word_list.save()

        response = await client.put(f"/api/word-list/{word_list.id}/", json={"words": ["1", "2", "3"]})

        assert response.status_code == 204
        assert await Word.filter(word_list=word_list).count() == 3
