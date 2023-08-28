#!/usr/bin/python3
"""
Task #0. Gather data from an API.
Script that using jsonplaceholder.typicode.com API,
for a given employee ID,returns information about
his/her TODO list progress.
"""
import json
import requests
import sys
import urllib

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    u = sys.argv[1]
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')

    todo_list = r.json()
    user_data = user_info.json()

    user_name = user_data["name"]

    tasks_done = [task for task in todo_list if task["completed"]]
    count_tasks = len(todo_list)
    completed_tasks = len(tasks_done)

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed_tasks, count_tasks))

    for todo in todo_list:
        if todo["completed"]:
            print("\t{}".format(todo["title"]))
