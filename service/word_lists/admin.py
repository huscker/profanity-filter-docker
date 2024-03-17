from fastapi_admin.app import app
from fastapi_admin.resources import Model

from service.word_lists.models import Word, WordList


@app.register
class WordListResource(Model):
    label = "Word lists"
    model = WordList
    icon = "fas fa-folder"
    fields = [
        "id",
        "name",
    ]


@app.register
class WordResource(Model):
    label = "Words"
    model = Word
    icon = "fas fa-cube"
    fields = ["id", ""]
