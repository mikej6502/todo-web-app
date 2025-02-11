from routes.api import get_task_service


def test_should_create_task_service():
    service = get_task_service()
    assert service
