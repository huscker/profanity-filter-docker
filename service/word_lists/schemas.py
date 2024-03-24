from pydantic import BaseModel


class WordList(BaseModel):
    id: int
    name: str


class WordListsResponse(BaseModel):
    word_lists: list[WordList]


class WordListWordsResponse(BaseModel):
    words: list[str]


class WordListUpdateRequest(BaseModel):
    words: list[str]
