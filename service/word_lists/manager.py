from aiocache import Cache, cached

from service.config import config
from service.word_lists.models import WordList


class WordlistManager:
    _word_lists: dict[int, list[str]]

    def __init__(self):
        self._word_lists = {}

    async def _refresh_lists(self):
        self._word_lists = {}
        word_lists = await WordList.all()
        for word_list in word_lists:
            words = await word_list.words.all().values("value")
            self._word_lists[word_list.id] = [word["value"] for word in words]

    @cached(ttl=config.WORDLIST_CACHE_TTL, cache=Cache.MEMORY)
    async def get_word_lists(self) -> dict[int, list[str]]:
        await self._refresh_lists()
        return self._word_lists

    async def get_list_by_id(self, id: int) -> list[str]:
        word_lists = await self.get_word_lists()
        return word_lists[id]
