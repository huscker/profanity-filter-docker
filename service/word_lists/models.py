from tortoise import fields
from tortoise.models import Model


class WordList(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    words: fields.ReverseRelation["Word"]

    def __str__(self):
        return self.name


class Word(Model):
    id = fields.IntField(pk=True)
    value = fields.TextField()

    word_list: fields.ForeignKeyRelation[WordList] = fields.ForeignKeyField("models.WordList", related_name="words")

    def __str__(self):
        return self.value
