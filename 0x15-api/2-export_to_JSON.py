#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

    => Records all tasks that are owned by this employee
    => Format must be: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}
    => File name must be: USER_ID.json
"""


import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]

    # Check if the argument pass is an interger
    if employeeId is not int:
        pass

    # Create CSV file for the employee
    filename = '{}.json'.format(employeeId)

    # Get the Request User Url (API)
    url = "https://jsonplaceholder.typicode.com/users"
    userResponse = requests.get("{}/{}".format(url, employeeId))
    userName = userResponse.json().get("name")

    # Get the Request Todo Url (API)
    todoResponses = requests.get("{}/{}/todos".format(url, employeeId))
    todoTasks = todoResponses.json()

    # Linking the tasks keys with their values
    taskDetails = [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": userName}
                   for task in todoTasks
                   ]
    taskDict = {employeeId: taskDetails}

    # Write into file
    with open(filename, 'w', newline='') as fd:
        json.dump(taskDict, fd)
