from fastapi import APIRouter, Depends

from service.filtering.schemas import CensorTextRequest, CensorTextResponse
from service.providers.base import FilteringProvider
from service.providers.get_provider import get_provider

router = APIRouter()


@router.post("/censor/", response_model=CensorTextResponse)
async def censor_text(
    request: CensorTextRequest, filtering_provider: FilteringProvider = Depends(get_provider)
) -> CensorTextResponse:
    censored_text = filtering_provider.censor_text(request.text)
    return CensorTextResponse(censored_text=censored_text)
