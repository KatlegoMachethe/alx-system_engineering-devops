#!/usr/bin/python3


import json
from sys import argv
import requests


if __name__ == "__main__":

    employeeId = argv[1]
    employee_credentials_url = "https://jsonplaceholder.typicode.com/users?id={}".format(employeeId)
    employee_todo_url  = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employeeId)
    
    r = requests.Session()

    employee_info = r.get(employee_credentials_url).json()[0]
    todo_list = r.get(employee_todo_url).json()
    
    tasks = []
    for task in todo_list:
        dict_of_tasks = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_info["username"]
                }
        tasks.append(dict_of_tasks)

    file_name = "{}.json".format(employeeId)
    employee_info_json = {employeeId: tasks}

    with open(file_name, 'w') as f:
        json.dump(employee_info_json, f)
