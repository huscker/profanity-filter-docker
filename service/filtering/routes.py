from fastapi import APIRouter

from service.filtering.providers.manager import manager
from service.filtering.schemas import CensorTextRequest, CensorTextResponse

router = APIRouter()


@router.post("/censor/", response_model=CensorTextResponse)
async def censor_text(request: CensorTextRequest) -> CensorTextResponse:
    provider = await manager.get_provider(request.provider)
    censored_text = await provider.censor_text(request.text, request.word_list_id)
    return CensorTextResponse(censored_text=censored_text)
