#!/usr/bin/python3
"""
fgbvd
"""
import json
import requests
from sys import argv


def get_info(url):
    """
    sfgbgvfds
    """
    data = requests.get(url)
    return data.json()


def get_user_todos(user_id):
    """
    Get the TODO list for a given user ID
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def main():
    """
    fgbjfnd
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in get_user_todos(user["id"])
        ] for user in users
    }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
