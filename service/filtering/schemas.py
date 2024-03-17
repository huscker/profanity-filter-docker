from pydantic import BaseModel

from service.filtering.providers.base import ProviderTypes


class CensorTextRequest(BaseModel):
    text: str
    provider: ProviderTypes
    word_list_id: int


class CensorTextResponse(BaseModel):
    censored_text: str
