#!/usr/bin/python3
"""
Employee Info
for a given employee ID, returns information
about his/her TODO list progress."""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users')

    todo_list = r.json()
    user_data = user_info.json()

    all_employee_tasks = {}

    for user in user_data:
        user_id = user["id"]
        username = user["username"]
        user_tasks = []

        for todo in todo_list:
            if todo["userId"] == user_id:
                user_tasks.append({
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username
                })

        all_employee_tasks[str(user_id)] = user_tasks

    filename = "todo_all_employees.json"

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(all_employee_tasks, f, indent=4)