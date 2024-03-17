from tortoise import fields
from tortoise.models import Model


class ProfanityFilterSettings(Model):
    id = fields.IntField(pk=True)
    max_relative_distance = fields.FloatField(default=0.3)
    censor_whole_words = fields.BooleanField(default=True)
