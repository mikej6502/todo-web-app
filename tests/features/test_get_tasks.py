from pytest_bdd import given, when, then, parsers, scenario
from test_client import TodoServiceClient


@scenario('test_get_tasks.feature', 'User gets all tasks from the list')
def test_get_tasks():
    """ Test Runner"""


client = TodoServiceClient('http://localhost:8080')
context = {}


@given('the list is empty')
def setup():
    """ set up - note list will be empty by default, perform any set up here"""
    context.clear()


@when(parsers.parse('the user gets all tasks'))
def get_tasks():
    status_code, tasks = client.get_all_tasks()
    assert status_code == 200
    context['TASKS'] = tasks


@then(parsers.parse('the list contains the no tasks'))
def verify_tasks():
    assert context['TASKS'] == []
