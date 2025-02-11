from abc import abstractmethod
from model.models import Task


class BaseTaskRepository:
    @abstractmethod
    def get_tasks(self) -> list[Task]:
        """Abstract Method"""


class InMemoryTaskRepository(BaseTaskRepository):
    def __init__(self):
        self.next_id = 1
        self.tasks = {}

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        return list(self.tasks.values())
