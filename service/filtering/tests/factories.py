from factory_boy_extra.tortoise_factory import TortoiseModelFactory

from service.filtering.models import ProfanityFilterProviderSettings


class ProfanityFilterProviderSettingsFactory(TortoiseModelFactory):
    max_relative_distance = 0.3
    censor_whole_words = True

    class Meta:
        model = ProfanityFilterProviderSettings
