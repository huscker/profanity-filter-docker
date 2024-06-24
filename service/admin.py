from fastapi import Depends
from fastapi_admin.app import app
from fastapi_admin.depends import get_resources
from fastapi_admin.resources import Link, Model
from fastapi_admin.template import templates
from starlette.requests import Request

from service.word_lists.models import WordList


@app.register
class Home(Link):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"


@app.register
class AdminResource(Model):
    label = "Admin"
    model = WordList
    icon = "fas fa-user"
    page_pre_title = "admin list"
    page_title = "admin model"
    fields = [
        "id",
    ]


@app.get("/")
async def home(
    request: Request,
    resources=Depends(get_resources),
):
    return templates.TemplateResponse(
        "dashboard.html",
        context={
            "request": request,
            "resources": resources,
            "resource_label": "Dashboard",
            "page_pre_title": "overview",
            "page_title": "Dashboard",
        },
    )
