#!/usr/bin/python3
"""
Script that returns information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_url = "{}/users/{}".format(base_url, employee_id)
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Get employee todos
    todos_url = "{}/todos".format(base_url)
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed") is True]

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

