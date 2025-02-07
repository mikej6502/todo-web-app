from pytest_bdd import given, when, then, parsers, scenario

from model.models import TaskRequest
from test_client import TodoServiceClient


@scenario('add_task.feature', 'User adds a new task to the list')
def test_add_task():
    """ Test Runner"""


client = TodoServiceClient('http://localhost:8080')
context = {}


@given('the list is empty')
def setup():
    """ set up - note list will be empty by default, perform any set up here"""
    context.clear()


@when(parsers.parse('the user adds a new task {title}'))
def add_item(title: str):
    status_code, task = client.create_item(TaskRequest(title=title, status='Todo'))
    assert status_code == 201
    context['CREATED_ITEM'] = task


@then(parsers.parse('the list contains the new task with a status of {status}'))
def verify_task(status: str):
    assert context['CREATED_ITEM'].status == status
