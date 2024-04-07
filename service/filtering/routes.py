from fastapi import APIRouter

from service.filtering.providers.manager import manager
from service.filtering.schemas import CensorTextRequest, CensorTextResponse

router = APIRouter()


@router.post("/censor/", response_model=CensorTextResponse)
async def censor_text(request: CensorTextRequest) -> CensorTextResponse:
    provider = manager.get_provider(request.provider)
    censored_text = provider.censor_text(request.text)
    return CensorTextResponse(censored_text=censored_text)
