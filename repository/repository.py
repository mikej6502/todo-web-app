from abc import abstractmethod

from model.models import Task
from service.exceptions import TaskNotFoundException


class BaseTaskRepository:
    @abstractmethod
    def get_task(self, task_id: int) -> Task:
        """Abstract Method"""


class InMemoryTaskRepository(BaseTaskRepository):
    def __init__(self):
        self.next_id = 1
        self.tasks = {}
        self.tasks[1] = Task(id='1', title='Build GET API', status='Todo')
        self.next_id = 2

    def get_task(self, task_id: int) -> Task:
        """Get a task by ID, raised TaskNotFoundException if not found"""
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task not found for id: {task_id}")
        return self.tasks[task_id]
