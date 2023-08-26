#!/usr/bin/python3
"""
Employee Info
for a given employee ID, returns information
about his/her TODO list progress."""

import json
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()

    u = int(sys.argv[1])

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')

    todo_list = r.json()
    user_data = user_info.json()

    user_name = user_data["name"]

    tasks_done = [task for task in todo_list if task["completed"]]
    tn = len(todo_list)
    completed_n = len(tasks_done)

    file_name = '{}.csv'.format(user_data.get('id'))

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            if todo["userId"] == u:
                writer.writerow([user_data.get('id'),
                                 user_data.get('username'),
                                 todo.get('completed'),
                                 todo.get('title')])
