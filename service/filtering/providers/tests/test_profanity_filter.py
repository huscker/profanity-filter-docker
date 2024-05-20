import pytest as pytest

from service.filtering.providers.profanity_filter import ProfanityFilterProvider
from service.test_utils import save_batch
from service.word_lists.tests.factories import WordFactory, WordListFactory

pytestmark = [pytest.mark.asyncio]


@pytest.fixture
def provider():
    return ProfanityFilterProvider(max_relative_distance=0.3, censor_whole_words=True)


class TestProfanityFilterProvider:
    async def test_ok(self, provider):
        word_list = WordListFactory.build()
        await word_list.save()
        words = WordFactory.build_batch(10, word_list=word_list)
        await save_batch(words)

        result = await provider.censor_text("Это тест", word_list.id)

        assert result == "Это тест"

    async def test_censored(self, provider):
        word_list = WordListFactory.build()
        await word_list.save()
        word = WordFactory.build(word_list=word_list, value="тест")
        await word.save()

        result = await provider.censor_text("Это тест", word_list.id)

        assert result == "Это ****"
