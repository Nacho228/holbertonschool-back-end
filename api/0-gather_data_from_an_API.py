#!/usr/bin/python3
"""  for a given employee ID, returns information
about his/her TODO list progress. """

import requests
import sys

u = sys.argv[1]

r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')

todo_list = r.json()
user_info_list = user_info.json()

user_name = user_info_list["name"]

completed = [todo for todo in todo_list if todo["completed"]]
total_number = len(todo_list)
completed_n = len(completed)


print(f"Employee {user_name} is done with tasks {completed_n}/{total_number}")

for todo in todo_list:
    print("    ", todo['title'])
