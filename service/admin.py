import os

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from service.config import config


async def startup():
    from fastapi_admin.app import app

    import service.admin  # noqa
    import service.filtering.admin  # noqa
    import service.word_lists.admin  # noqa

    await app.configure(None, language_switch=False, template_folders=[os.path.join(config.BASE_DIR, "templates")])


def setup_admin_monkeypatches():
    from fastapi_admin import depends
    from starlette.requests import Request

    def patched(request: Request):
        return

    depends.get_current_admin = patched


def setup_admin(app: FastAPI):
    setup_admin_monkeypatches()

    from fastapi_admin.app import app as admin_app
    from fastapi_admin.depends import get_resources
    from starlette.requests import Request

    app.mount("/admin", admin_app)
    app.on_event("startup")(startup)

    @admin_app.get("/")
    async def home(
        request: Request,
        resources=Depends(get_resources),
    ):
        return RedirectResponse("/admin/wordlist/list")
