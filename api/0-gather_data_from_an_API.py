#!/usr/bin/python3
"""
Employee Info
for a given employee ID, returns information
about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()

    u = sys.argv[1]

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')

    todo_list = r.json()
    user_info_list = user_info.json()

    user_name = user_info_list["name"]

    tasks_done = [task for task in todo_list if task["completed"]]
    tasks_number = len(todo_list)
    n = len(tasks_done)

    print(f"Employee {user_name} is done with tasks ({n}/{tasks_done}):")

    for todo in todo_list:
        print("     ", todo['title'])
