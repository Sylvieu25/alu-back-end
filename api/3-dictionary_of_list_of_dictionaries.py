#!/usr/bin/python3
"""
Exports all employees' TODO lists to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users = requests.get("{}/users".format(base_url)).json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get todos for this user
        todos = requests.get("{}/todos".format(base_url),
                             params={"userId": user_id}).json()

        # Build list of tasks
        tasks = []
        for task in todos:
            tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add to dictionary
        all_tasks[user_id] = tasks

    # Write to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)

