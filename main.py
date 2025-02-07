from fastapi import FastAPI, Depends, HTTPException

from model.models import Task
from repository.repository import InMemoryTaskRepository
from service.exceptions import TaskNotFoundException
from service.task_service import TaskService

app = FastAPI()


def get_task_service():
    repository = InMemoryTaskRepository()
    __populate_test_data(repository)

    task_service = TaskService(repository)
    return task_service


def __populate_test_data(repository: InMemoryTaskRepository):
    task1 = Task(id=0, title='Build GET API', status='Todo')
    task2 = Task(id=0, title='Build POST API', status='Todo')

    repository.create_task(task1)
    repository.create_task(task2)


@app.get("/api/todo-service/task/{id}", tags=["todo"])
def get_task(task_id: int, task_service=Depends(get_task_service)) -> Task:
    try:
        return task_service.get_task(task_id)
    except TaskNotFoundException:
        raise HTTPException(status_code=404, detail=f"Task not found for id {task_id}")
