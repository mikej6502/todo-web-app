from repository.repository import BaseTaskRepository


class TaskService:
    def __init__(self, repository: BaseTaskRepository):
        self.repository = repository

    def get_task(self, task_id: int):
        task = self.repository.get_task(task_id)
        return task
