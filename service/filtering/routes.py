from fastapi import APIRouter

from service.filtering.models import ProfanityFilterSettings
from service.filtering.schemas import CensorTextRequest, CensorTextResponse
from service.providers.get_provider import get_provider

router = APIRouter()


@router.post("/censor/", response_model=CensorTextResponse)
async def censor_text(request: CensorTextRequest) -> CensorTextResponse:
    settings = await ProfanityFilterSettings.get_solo()
    provider = get_provider(
        request.provider,
        max_relative_distance=settings.max_relative_distance,
        censor_whole_words=settings.censor_whole_words,
    )
    censored_text = provider.censor_text(request.text)
    return CensorTextResponse(censored_text=censored_text)
