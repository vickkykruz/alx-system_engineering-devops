#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

    => Records all tasks from all employees
    => Format must be: { "USER_ID": [ {"username": "USERNAME",
     "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
     {"username": "USERNAME", "task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS}, ... ],
     "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
     "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    => File name must be: todo_all_employees.json
"""


import json
import os
import requests


if __name__ == "__main__":

    # Create CSV file for the employee
    taskDict = {}

    # Get the Request User Url (API)
    url = "https://jsonplaceholder.typicode.com"
    userResponse = requests.get(f"{url}/users")
    userDatas = userResponse.json()

    # Get the Request Todo Url (API)
    todoResponses = requests.get(f"{url}/todos")
    todoTasks = todoResponses.json()

    # Linking the tasks keys with their values
    for user in userDatas:
        userId = user.get("id")
        taskDetails = [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")} for task in todoTasks
                       if task.get("userId") == userId]
        taskDict[userId] = taskDetails

    filename = "todo_all_employees.json"
    # Write into file
    with open(filename, 'w', newline='') as fd:
        json.dump(taskDict, fd)
