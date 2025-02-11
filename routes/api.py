from fastapi import Depends, APIRouter
from model.models import Task
from repository.repository import InMemoryTaskRepository
from service.task_service import TaskService

router = APIRouter()

repository = InMemoryTaskRepository()


def get_task_service():
    task_service = TaskService(repository)
    return task_service


@router.get("/todo-service/tasks", tags=["todo"])
def get_tasks(task_service=Depends(get_task_service)) -> list[Task]:
    tasks = task_service.get_tasks()
    return tasks
