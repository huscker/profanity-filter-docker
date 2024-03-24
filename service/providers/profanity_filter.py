from profanity_filter import ProfanityFilter

from service.providers.base import FilteringProvider


class ProfanityFilterProvider(FilteringProvider):
    backend = ProfanityFilter()

    def censor_text(self, text: str) -> str:
        return self.backend.censor(text)

    def reload_word_list(self, words: list[str]):
        self.backend.custom_profane_word_dictionaries
