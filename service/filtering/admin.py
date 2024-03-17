from fastapi_admin.app import app
from fastapi_admin.resources import Model

from service.filtering.models import ProfanityFilterProviderSettings


@app.register
class ProfanityFilterSettingsResource(Model):
    label = "Profanity filter settings"
    model = ProfanityFilterProviderSettings
    icon = "fas fa-cog"
    fields = ["max_relative_distance", "censor_whole_words"]
