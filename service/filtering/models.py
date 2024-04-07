from tortoise import fields
from tortoise.models import Model


class ProviderSettings(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True

    @classmethod
    async def get_solo(cls) -> "ProviderSettings":
        settings, _ = await cls.get_or_create()
        return settings


class ProfanityFilterProviderSettings(ProviderSettings):
    max_relative_distance = fields.FloatField(default=0.3)
    censor_whole_words = fields.BooleanField(default=True)
