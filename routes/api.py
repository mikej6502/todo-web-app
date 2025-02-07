from fastapi import Depends, HTTPException, status, APIRouter
from model.models import Task, TaskRequest
from repository.repository import InMemoryTaskRepository
from service.exceptions import TaskNotFoundException
from service.task_service import TaskService

router = APIRouter()


def __populate_test_data(repository: InMemoryTaskRepository):
    task1 = Task(id=0, title='Build GET API', status='Todo')
    task2 = Task(id=0, title='Build POST API', status='Todo')

    repository.create_task(task1)
    repository.create_task(task2)


repository = InMemoryTaskRepository()
__populate_test_data(repository)


def get_task_service():
    task_service = TaskService(repository)
    return task_service


@router.get("/todo-service/tasks", tags=["todo"])
def get_tasks(task_service=Depends(get_task_service)) -> list[Task]:
    tasks = task_service.get_tasks()
    return tasks


@router.get("/todo-service/task/{id}", tags=["todo"])
def get_task(task_id: int, task_service=Depends(get_task_service)) -> Task:
    try:
        return task_service.get_task(task_id)
    except TaskNotFoundException:
        raise HTTPException(status_code=404, detail=f"Task not found for id {task_id}")


@router.post("/todo-service/task", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["todo"])
def post_task(task_request: TaskRequest, task_service=Depends(get_task_service)) -> Task:
    task = Task(id=0, title=task_request.title, status=task_request.status)
    return task_service.create_task(task)
