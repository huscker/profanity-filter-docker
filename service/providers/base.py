from abc import abstractmethod


class FilteringProvider:
    @abstractmethod
    def censor_text(self, text: str) -> str:
        pass

    @abstractmethod
    def reload_word_list(self, words: list[str]):
        pass
