from repository.repository import BaseTaskRepository
from service.exceptions import TaskNotFoundException


class TaskService:
    def __init__(self, repository: BaseTaskRepository):
        self.repository = repository

    def get_task(self, task_id: int):
        """ Get a taskk by id, raises NotFoundException if task not found"""
        task = self.repository.get_task(task_id)
        if task is None:
            raise TaskNotFoundException(f"Task not found for id: {task_id}")

        return task
