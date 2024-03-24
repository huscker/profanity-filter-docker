from service.providers.base import FilteringProvider, ProviderTypes
from service.providers.profanity_filter import ProfanityFilterProvider


def get_provider(
    provider_type: ProviderTypes, max_relative_distance: float, censor_whole_words: bool
) -> FilteringProvider:
    match provider_type:
        case ProviderTypes.PROFANITY_FILTER:
            return ProfanityFilterProvider(
                max_relative_distance=max_relative_distance, censor_whole_words=censor_whole_words
            )
