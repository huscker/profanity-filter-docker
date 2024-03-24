from tortoise import fields
from tortoise.models import Model


class ProfanityFilterSettings(Model):
    id = fields.IntField(pk=True)
    max_relative_distance = fields.FloatField(default=0.3)
    censor_whole_words = fields.BooleanField(default=True)

    @classmethod
    async def get_solo(cls) -> "ProfanityFilterSettings":
        settings, _ = await ProfanityFilterSettings.get_or_create()
        return settings
