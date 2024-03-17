from enum import StrEnum

from pydantic import BaseModel


class ProviderTypes(StrEnum):
    PROFANITY_FILTER = "PROFANITY_FILTER"


class CensorTextRequest(BaseModel):
    text: str


class CensorTextResponse(BaseModel):
    censored_text: str
