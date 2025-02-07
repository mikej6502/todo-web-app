import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from starlette import status

from model.models import Task, TaskRequest
from repository.repository import InMemoryTaskRepository
from service.exceptions import TaskNotFoundException
from service.task_service import TaskService

app = FastAPI()


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


@app.get("/api/todo-service/task/{id}", tags=["todo"])
def get_task(task_id: int, task_service=Depends(get_task_service)) -> Task:
    try:
        return task_service.get_task(task_id)
    except TaskNotFoundException:
        raise HTTPException(status_code=404, detail=f"Task not found for id {task_id}")


@app.post("/api/todo-service/task/{id}", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["todo"])
def post_task(task_request: TaskRequest, task_service=Depends(get_task_service)) -> Task:
    task = Task(id=0, title=task_request.title, status=task_request.status)
    return task_service.create_task(task)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
