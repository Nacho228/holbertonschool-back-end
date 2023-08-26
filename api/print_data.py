#!/usr/bin/python3
""" Prints data of an user"""


import requests
import json
import sys


if len(sys.argv) < 2:
        exit()
    
u = sys.argv[1]

r = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}/todos')
i = requests.get(f'https://jsonplaceholder.typicode.com/users/{u}')
data = r.json()
info = i.json()
print(data, '\n', info)
