import pytest
import pytest_asyncio

from service.word_lists.models import WordList
from service.word_lists.tests.factories import WordListFactory

pytestmark = [pytest.mark.asyncio]


@pytest_asyncio.fixture
async def filled_wordlist(event_loop) -> WordList:
    word_list = WordListFactory.build()
    await word_list.save()
    # words = WordFactory.build_batch(1, word_list=word_list)
    # await save_batch(words)
    # return word_list


class TestWordLists:
    async def test_list(self, filled_wordlist, client, event_loop):
        response = await client.get("/api/word-list/all/")

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == filled_wordlist.id

    # async def test_get(self, filled_wordlist, client):
    #     response = await client.get(f"/api/word-list/{filled_wordlist.id}/")
    #
    #     assert response.status_code == 200
    #     data = response.json()
    #     assert len(data) == 1
    #     assert data[0]["id"] == filled_wordlist.id
    #
    # async def test_update(self, filled_wordlist, client):
    #     response = await client.put(f"/api/word-list/{filled_wordlist.id}/")
    #
    #     assert response.status_code == 200
    #     data = response.json()
    #     assert len(data) == 1
    #     assert data[0]["id"] == filled_wordlist.id
