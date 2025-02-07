from unittest.mock import Mock

import pytest

from model.models import Task
from service.exceptions import TaskNotFoundException
from service.task_service import TaskService


@pytest.fixture
def mock_repository():
    return Mock()


def test_should_find_task_by_id(mock_repository):
    mock_repository.get_task.return_value = Task(id=1, title='Test Task', status='Todo')
    service = TaskService(mock_repository)

    task = service.get_task(1)

    assert task.id == 1
    assert task.title == 'Test Task'
    assert task.status == 'Todo'


def test_should_not_find_task_by_id_when_doesnt_exist(mock_repository):
    mock_repository.get_task.return_value = None
    service = TaskService(mock_repository)

    with pytest.raises(TaskNotFoundException):
        service.get_task(1)

