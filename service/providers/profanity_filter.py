from service.providers.base import FilteringProvider


class ProfanityFilterProvider(FilteringProvider):
    def censor_text(self, text: str) -> str:
        pass

    def reload_word_list(self, words: list[str]):
        pass
