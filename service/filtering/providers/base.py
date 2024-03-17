from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

from service.word_lists.manager import WordlistManager


class ProviderTypes(str, Enum):
    PROFANITY_FILTER = "PROFANITY_FILTER"


@dataclass
class FilteringProvider:
    manager = WordlistManager()

    @abstractmethod
    async def _censor_text(self, text: str) -> str:
        pass

    @abstractmethod
    async def _reload_word_list(self, words: list[str]):
        pass

    async def censor_text(self, text: str, word_list_id: int) -> str:
        words = await self.manager.get_list_by_id(word_list_id)
        await self._reload_word_list(words)
        return await self._censor_text(text)
