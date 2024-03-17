from fastapi import FastAPI

from service.admin import setup_admin
from service.orm import setup_orm

app = FastAPI(
    docs_url="/api/docs/",
    openapi_url="/api/openapi.json/",
    redoc_url=None,
    title="Profanity filter service",
)
setup_admin(app)
setup_orm(app)


@app.get("/health/", status_code=200)
async def check_health():
    return
