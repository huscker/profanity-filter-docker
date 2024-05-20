from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import WordList

WordListPydantic = pydantic_model_creator(WordList)


class WordListsResponse(BaseModel):
    word_lists: list[WordListPydantic]


class WordListWordsResponse(BaseModel):
    words: list[str]


class WordListUpdateRequest(BaseModel):
    words: list[str]
