from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from model.models import Task
from routes.api import get_tasks, get_task_service

web_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@web_router.get("/", tags='website')
def display_all_items(request: Request):
    tasks: list[Task] = get_tasks(get_task_service())

    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
