#!/usr/bin/python3


from sys import argv
import requests


if __name__ == "__main__":

    employeeId = argv[1]
    employee_credentials_url = "https://jsonplaceholder.typicode.com/users?id={}".format(employeeId)
    employee_todo_url  = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employeeId)
    
    r = requests.Session()
    employee_username = r.get(employee_credentials_url).json()[0]["username"]
    employee_todo_list = r.get(employee_todo_url).json()

    file_name = "{}.csv".format(employeeId)

    with open(file_name, "w") as f:
        for task in employee_todo_list:
            f.write('"{}", "{}", "{}", "{}"\n'.format(employeeId, employee_username, task["completed"], task["title"]))
