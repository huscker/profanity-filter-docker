from fastapi import Depends

from service.config import Config, ProviderTypes, get_config
from service.providers.base import FilteringProvider
from service.providers.profanity_filter import ProfanityFilterProvider


def get_provider(config: Config = Depends(get_config)) -> FilteringProvider:
    match config.provider:
        case ProviderTypes.PROFANITY_FILTER:
            return ProfanityFilterProvider()
