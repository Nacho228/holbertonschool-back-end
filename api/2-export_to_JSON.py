#!/usr/bin/python3
"""
Employee Info
for a given employee ID, returns information
about his/her TODO list progress."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()

    u = sys.argv[1]

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')

    todo_list = r.json()
    user_data = user_info.json()

    user_name = user_data["name"]

    tasks_done = [task for task in todo_list if task["completed"]]
    tn = len(todo_list)
    completed_n = len(tasks_done)

    file_name = '{}.json'.format(user_data.get('id'))

    with open(file_name, mode="a", encoding="utf-8") as f:
        f.write(json.dumps({u: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": todo.get("username"),
            } for todo in todo_list]}))

    tasks_done = [task for task in todo_list if task["completed"]]
    tn = len(todo_list)
    completed_n = len(tasks_done)

    file_name = '{}.json'.format(user_data.get('id'))

    with open(file_name, mode="a", encoding="utf-8") as f:
        f.write(json.dumps({u: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": todo.get("username"),
            } for todo in todo_list]}))
