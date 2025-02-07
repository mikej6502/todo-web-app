import pytest
from unittest.mock import Mock
from fastapi import HTTPException
from main import get_task
from model.models import Task
from service.exceptions import TaskNotFoundException


def test_should_get_task_by_id():
    mock_service = Mock()
    mock_service.get_task.return_value = Task(id=1, title='Test Task', status='Todo')

    task: Task = get_task(1, mock_service)
    assert task.id == 1


def test_should_return_http_not_found_error_when_task_doesnt_exist():
    mock_service = Mock()
    mock_service.get_task.side_effect = TaskNotFoundException('Task not found')

    with pytest.raises(HTTPException) as err:
        get_task(1, mock_service)

    assert err.value.status_code == 404
