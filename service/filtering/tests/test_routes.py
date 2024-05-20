import pytest

from service.filtering.providers.base import ProviderTypes
from service.filtering.tests.factories import ProfanityFilterProviderSettingsFactory
from service.word_lists.tests.factories import WordListFactory

pytestmark = [pytest.mark.asyncio]


class TestCensorText:
    async def test_ok(self, client):
        settings = ProfanityFilterProviderSettingsFactory.build()
        await settings.save()
        word_list = WordListFactory.build()
        await word_list.save()

        response = await client.post(
            "/api/filtering/censor/",
            json={
                "text": "some text",
                "provider": ProviderTypes.PROFANITY_FILTER,
                "word_list_id": word_list.id,
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert data["censored_text"] == "some text"
