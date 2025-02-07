import json
from urllib.parse import urljoin

from fastapi.testclient import TestClient

from main import app
from model.models import TaskRequest, Task


class TodoServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = TestClient(app)

    def create_item(self, task: TaskRequest) -> (int, Task):
        url = urljoin(self.base_url, '/api/todo-service/task/')
        response = self.client.post(url, json=json.loads(task.json()))

        if response.status_code != 201:
            raise Exception(f'Unable to create task.Status Code {response.status_code}')
        created_task = Task(**response.json())

        return response.status_code, created_task
