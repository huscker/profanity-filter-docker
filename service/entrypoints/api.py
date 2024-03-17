from urllib.request import Request

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from service.filtering.routes import router as filtering_router
from service.monitoring import setup_monitoring
from service.orm import setup_orm
from service.word_lists.routes import router as word_lists_router

app = FastAPI(
    docs_url="/api/docs/",
    openapi_url="/api/openapi.json/",
    redoc_url=None,
    title="Profanity filter service",
)
setup_monitoring(app)
setup_orm(app)


@app.get("/health/", status_code=200)
async def check_health():
    return


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        {"code": "internal_server_error", "detail": "Internal Server Error"},
        status_code=500,
    )


app.include_router(
    filtering_router,
    tags=["Filtering"],
    prefix="/api/filtering",
)
app.include_router(word_lists_router, tags=["Word lists"], prefix="/api/word-list")
