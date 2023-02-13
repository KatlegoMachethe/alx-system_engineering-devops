#!/usr/bin/python3
"""
file: 0-gather_data_from_an_API.py
Description: This script uses the JSONPlaceholder API
            (see resources.txt for more info on the API)
            for a given employee ID and returns info about
            the employee's todo iist progress
Author: Katlego Machethe
Created: 10 February 2023
"""

from sys import argv
import requests


if __name__ == "__main__":

    r = requests.Session()

    employeeId = argv[1]
    employee_credentials_url = "https://jsonplaceholder.typicode.com/users?id={}".format(employeeId)
    employee_todo_url  = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employeeId)
    
    employee_name = r.get(employee_credentials_url).json()[0]["name"]
    employee_todo_list = r.get(employee_todo_url).json()

    total_number_of_tasks = len(employee_todo_list)
    tasks_done = []
    
    for task in employee_todo_list:
        if task["completed"] == True:
            tasks_done.append(task["title"])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(tasks_done), total_number_of_tasks))
    for task in tasks_done:
        print("\t {}".format(task))
