#!/usr/bin/python3
"""Exports employee TODO list to CSV."""
import csv
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
    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
