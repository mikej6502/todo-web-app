from urllib.parse import urljoin
from fastapi.testclient import TestClient
from main import app
from model.models import Task


class TodoServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = TestClient(app)

    def get_all_tasks(self):
        url = urljoin(self.base_url, '/api/todo-service/tasks')
        response = self.client.get(url)

        if response.status_code != 200:
            raise Exception(f'Unable to get tasks.Status Code {response.status_code}')
        tasks = response.json()
        return response.status_code, tasks
