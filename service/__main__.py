import os
from urllib.request import Request

import redis
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_admin.app import app as admin_app
from prometheus_client import Counter
from tortoise.contrib.fastapi import register_tortoise

from service.config import config, orm_config
from service.monitoring import instrumentator

exceptions_by_type = Counter(
    "http_exceptions_total_by_type",
    "Count of exceptions by object type.",
    ["type"],
)


app = FastAPI(
    docs_url="/api/docs/",
    openapi_url="/api/openapi.json/",
    redoc_url=None,
    title="Profanity filter service",
)
app.mount("/admin", admin_app)
instrumentator.instrument(app)
instrumentator.expose(app, include_in_schema=True, should_gzip=True)


@app.on_event("startup")
async def startup():
    await admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        redis=redis.from_url(config.REDIS_URL.unicode_string()),
        template_folders=[os.path.join(config.BASE_DIR, "templates")],
    )


@app.get("/health/", status_code=200)
async def check_health():
    return


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        {"code": "internal_server_error", "detail": "Internal Server Error"},
        status_code=500,
    )


register_tortoise(
    app,
    config=orm_config,
    generate_schemas=True,
    add_exception_handlers=True,
)

# app.include_router(
#     filtering_router,
#     tags=["Filtering"],
#     prefix="/api/filtering",
# )
# app.include_router(word_lists_router, tags=["Word lists"], prefix="/api/word-list")
