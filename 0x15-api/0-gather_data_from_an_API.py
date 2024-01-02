#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Requirements:

    => You must use urllib or requests module
    => The script must accept an integer as a parameter, which is the employee
     ID
    => The script must display on the standard output the employee TODO list
     progress in this exact format:
    => First line: Employee EMPLOYEE_NAME is done with tasks
     (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        => EMPLOYEE_NAME: name of the employee
        => NUMBER_OF_DONE_TASKS: number of completed tasks
        => TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
         completed and non-completed tasks
    => Second and N next lines display the title of completed tasks:
        =>TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""


import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]

    # Check if the argument pass is an interger
    if employeeId is not int:
        pass

    # Get the Request User Url (API)
    url = "https://jsonplaceholder.typicode.com/users"
    userResponse = requests.get("{}/{}".format(url, employeeId))
    userName = userResponse.json().get("name")

    # Get the Request Todo Url (API)
    todoResponses = requests.get("{}/{}/todos".format(url, employeeId))
    todoTasks = todoResponses.json()

    completedTasks = [task for task in todoTasks if task.get('completed')]

    # Display the output
    print("Employee {} is done with tasks({}/{}):"
          .format(userName, len(completedTasks), len(todoTasks)))

    for completedTaskTitle in completedTasks:
        print("\t {}".format(completedTaskTitle.get("title")))
