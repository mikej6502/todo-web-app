from model.models import Task
from repository.repository import BaseTaskRepository


class TaskService:
    def __init__(self, repository: BaseTaskRepository):
        self.repository = repository

    def get_tasks(self) -> list[Task]:
        """ Get all tasks"""
        tasks = self.repository.get_tasks()
        return tasks
