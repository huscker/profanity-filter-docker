from dataclasses import dataclass

from profanity_filter import ProfanityFilter
from profanity_filter.types_ import AnalysisType

from service.filtering.providers.base import FilteringProvider


@dataclass
class ProfanityFilterProvider(FilteringProvider):
    max_relative_distance: float
    censor_whole_words: bool
    backend = ProfanityFilter(languages=["en"], analyses=[AnalysisType.DEEP, AnalysisType.MORPHOLOGICAL])

    async def _censor_text(self, text: str) -> str:
        return self.backend.censor(text)

    async def _reload_word_list(self, words: list[str]):
        self.backend.custom_profane_word_dictionaries = {"en": words}
