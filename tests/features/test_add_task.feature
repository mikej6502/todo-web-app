Feature: Add task to todo list

  Scenario: User adds a new task to the list
    Given the list is empty
    When the user adds a new task Buy groceries
    Then the list contains the new task with a status of Todo
