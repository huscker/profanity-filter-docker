import pytest as pytest

from service.filtering.providers.profanity_filter import ProfanityFilterProvider


@pytest.fixture
def provider():
    return ProfanityFilterProvider(max_relative_distance=0.3, censor_whole_words=True)


class TestProfanityFilterProvider:
    def test_ok(self, provider):
        result = await provider.censor_text("Это тест")

        assert result == "Это ****"

    def test_censored(self, provider):
        await provider.reload_word_list(["Это тест"])

        result = await provider.censor_text("Это тест")

        assert result == "Это ****"
