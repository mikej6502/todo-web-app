from model.models import Task
from repository.repository import BaseTaskRepository
from service.exceptions import TaskNotFoundException


class TaskService:
    def __init__(self, repository: BaseTaskRepository):
        self.repository = repository

    def create_task(self, task: Task):
        """ Get a taskk by id, raises NotFoundException if task not found"""
        task = self.repository.create_task(task)
        return task

    def get_task(self, task_id: int) -> Task:
        """ Get a task by id, raises NotFoundException if task not found"""
        task = self.repository.get_task(task_id)
        if task is None:
            raise TaskNotFoundException(f"Task not found for id: {task_id}")
        return task

    def get_tasks(self) -> list[Task]:
        """ Get all tasks"""
        tasks = self.repository.get_tasks()
        return tasks
