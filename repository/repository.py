from abc import abstractmethod

from model.models import Task
from service.exceptions import TaskNotFoundException


class BaseTaskRepository:
    @abstractmethod
    def create_task(self, task: Task) -> Task:
        """Abstract Method"""

    @abstractmethod
    def get_task(self, task_id: int) -> Task:
        """Abstract Method"""

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        """Abstract Method"""


class InMemoryTaskRepository(BaseTaskRepository):
    def __init__(self):
        self.next_id = 1
        self.tasks = {}

    def create_task(self, task: Task) -> Task:
        """Create a new task. Will set id with autogenerated value"""
        task.id = self.next_id
        self.tasks[task.id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Task | None:
        """Get a task by ID, or return None if not found"""
        if task_id not in self.tasks:
            return None
        return self.tasks[task_id]

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        return self.tasks.values()
