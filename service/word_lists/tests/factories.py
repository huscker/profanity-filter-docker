import factory
from factory.fuzzy import FuzzyText
from factory_boy_extra.tortoise_factory import TortoiseModelFactory

from service.word_lists.models import Word, WordList


class WordListFactory(TortoiseModelFactory):
    name = FuzzyText(length=10)

    class Meta:
        model = WordList


class WordFactory(TortoiseModelFactory):
    value = FuzzyText(length=10)
    word_list = factory.SubFactory(WordListFactory)

    class Meta:
        model = Word
