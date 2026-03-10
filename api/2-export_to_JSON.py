#!/usr/bin/python3
"""
Exports employee TODO list to JSON.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    # Build JSON structure
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks}

    # Write to JSON file named USER_ID.json
    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)

