Feature: Get tasks from todo list

  Scenario: User gets all tasks from the list
    Given the list is empty
    When the user gets all tasks
    Then the list contains the no tasks
