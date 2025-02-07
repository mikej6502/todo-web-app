from pydantic import BaseModel


class TaskRequest(BaseModel):
    title: str
    status: str


class Task(TaskRequest):
    id: int
