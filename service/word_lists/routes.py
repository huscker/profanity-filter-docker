from asyncio import gather

from fastapi import APIRouter, Body

from service.word_lists.models import Word, WordList
from service.word_lists.schemas import WordListPydantic, WordListsResponse, WordListUpdateRequest, WordListWordsResponse

router = APIRouter()


@router.get("/all/", response_model=WordListsResponse)
async def get_word_lists() -> WordListsResponse:
    word_lists = [WordListPydantic.from_tortoise_orm(wordlist) for wordlist in await WordList.all()]
    return WordListsResponse(word_lists=await gather(*word_lists))


@router.post("/", status_code=201)
async def create_word_list(name: str = Body()):
    await WordList.create(name=name)


@router.get("/{word_list_id}/", response_model=WordListWordsResponse)
async def get_word_list(word_list_id: int) -> WordListWordsResponse:
    word_list = await WordList.get(id=word_list_id)
    words = await word_list.words.all()
    return WordListWordsResponse(words=[word.value for word in words])


@router.put("/{word_list_id}/", status_code=204)
async def update_word_list(word_list_id: int, request: WordListUpdateRequest):
    word_list = await WordList.get(id=word_list_id)
    await word_list.words.all().delete()
    for word in request.words:
        new_word = Word(value=word, word_list=word_list)
        await new_word.save()
