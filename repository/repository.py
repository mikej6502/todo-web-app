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

    def get_task(self, task_id: int) -> Task | None:
        """Get a task by ID, or return None if not found"""
        if task_id not in self.tasks:
            return None
        return self.tasks[task_id]
