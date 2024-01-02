#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.

Requirements:

    => Records all tasks that are owned by this employee
    => Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
     "TASK_TITLE"
    => File name must be: USER_ID.csv
"""


import requests
import sys
import csv


if __name__ == "__main__":
    employeeId = sys.argv[1]

    # Check if the argument pass is an interger
    if employeeId is not int:
        pass

    # Create CSV file for the employee
    csv_filename = '{}.csv'.format(employeeId)

    # Get the Request User Url (API)
    url = "https://jsonplaceholder.typicode.com/users"
    userResponse = requests.get("{}/{}".format(url, employeeId))
    userName = userResponse.json().get("name")

    # Get the Request Todo Url (API)
    todoResponses = requests.get("{}/{}/todos".format(url, employeeId))
    todoTasks = todoResponses.json()

    # Write into file
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for task in todoTasks:
            row = [
                    employeeId, userName, task["completed"], task["title"]]
            csv_writer.writerow(row)
