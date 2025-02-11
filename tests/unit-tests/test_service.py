from unittest.mock import Mock
import pytest
from repository.repository import InMemoryTaskRepository
from service.task_service import TaskService


@pytest.fixture
def mock_repository():
    return Mock()


def test_should_return_empty_list_of_task(mock_repository):
    in_memory_repository = InMemoryTaskRepository()
    service = TaskService(in_memory_repository)

    assert service.get_tasks() == []
