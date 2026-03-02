#!/usr/bin/python3
"""
This module fetches and displays an employee's TODO list progress
using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = 0
    completed_titles = []

    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1
            completed_titles.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for title in completed_titles:
        print("\t {}".format(title))
