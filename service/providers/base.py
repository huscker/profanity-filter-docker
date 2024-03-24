from abc import abstractmethod
from dataclasses import dataclass
from enum import StrEnum


class ProviderTypes(StrEnum):
    PROFANITY_FILTER = "PROFANITY_FILTER"


@dataclass
class FilteringProvider:
    max_relative_distance: float
    censor_whole_words: bool

    @abstractmethod
    def censor_text(self, text: str) -> str:
        pass

    @abstractmethod
    def reload_word_list(self, words: list[str]):
        pass
