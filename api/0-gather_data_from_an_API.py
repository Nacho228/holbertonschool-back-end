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
    user_info_list = user_info.json()

    user_name = user_info_list["name"]

    tasks_done = [task for task in todo_list if task["completed"]]
    tn = len(todo_list)
    completed_n = len(tasks_done)

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed_n, tn))

    for todo in todo_list:
        print('\t', todo['title'])
