#!/usr/bin/python3
"""Script that returns information about an employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    ).json()
    employee_name = user.get("name")
   todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()
    completed_tasks = [task for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
