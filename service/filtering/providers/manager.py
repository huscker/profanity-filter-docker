from service.filtering.models import ProfanityFilterProviderSettings
from service.filtering.providers.base import FilteringProvider, ProviderTypes
from service.filtering.providers.profanity_filter import ProfanityFilterProvider


class ProviderManager:
    _providers: dict[ProviderTypes, FilteringProvider] = {}

    async def reload_providers(self):
        for provider_type in list(ProviderTypes):
            self._providers[provider_type] = await self.get_provider(provider_type)

    async def get_provider(self, provider_type: ProviderTypes) -> FilteringProvider:
        match provider_type:
            case ProviderTypes.PROFANITY_FILTER:
                config = await ProfanityFilterProviderSettings.get_solo()
                return ProfanityFilterProvider(
                    max_relative_distance=config.max_relative_distance, censor_whole_words=config.censor_whole_words
                )


manager = ProviderManager()
