from dataclasses import dataclass

from profanity_filter import ProfanityFilter

from service.filtering.providers.base import FilteringProvider


@dataclass
class ProfanityFilterProvider(FilteringProvider):
    max_relative_distance: float
    censor_whole_words: bool
    backend = ProfanityFilter()

    async def _censor_text(self, text: str) -> str:
        return self.backend.censor(text)

    async def reload_word_list(self, words: list[str]):
        self.backend._custom_profane_word_dictionaries = {"ru": words}
