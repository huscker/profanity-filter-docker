from fastapi import APIRouter

from service.word_lists.models import Word, WordList
from service.word_lists.schemas import WordListsResponse, WordListUpdateRequest, WordListWordsResponse

router = APIRouter()


@router.get("/all/", response_model=WordListsResponse)
async def get_word_lists() -> WordListsResponse:
    word_lists = await WordList.all()
    return WordListsResponse(word_lists=word_lists)


@router.get("/{word_list_id}/", response_model=WordListWordsResponse)
async def get_word_list(word_list_id: int) -> WordListWordsResponse:
    word_list = await WordList.get(id=word_list_id)
    words = await word_list.words.all()
    return WordListWordsResponse(words=[word.name for word in words])


# TODO: Обернуть в транзакцию
@router.put("/{word_list_id}/", status_code=204)
async def update_word_list(word_list_id: int, request: WordListUpdateRequest):
    word_list = await WordList.get(id=word_list_id)
    await word_list.words.all().delete()
    for word in request.words:
        new_word = Word(value=word, word_list=word_list)
        await new_word.save()
