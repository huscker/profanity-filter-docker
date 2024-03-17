from urllib.request import Request

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_admin.app import app as admin_app
from prometheus_client import Counter

from service.core.exceptions import BusinessException
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
instrumentator.instrument(app)
instrumentator.expose(app, include_in_schema=True, should_gzip=True)


@app.get("/health/", status_code=200)
async def check_health():
    return


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        {"code": "internal_server_error", "detail": "Internal Server Error"},
        status_code=500,
    )


@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse({"code": exc.code, "detail": exc.detail}, status_code=exc.status_code)


app.mount("/admin/", admin_app)
# app.include_router(profanity_router, tags=["filter"], prefix="/api/filter")
# app.include_router(
#     forbidden_keywords_router,
#     tags=["keywords"],
#     prefix="/api/keywords",
# )
