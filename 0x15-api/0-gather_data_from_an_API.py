#!/usr/bin/python3
"""
Use this REST API to return employee information:
https://jsonplaceholder.typicode.com/
"""

import requests
from sys import argv

if __name__ == "__main__":
    # get employee name
    original_url = "https://jsonplaceholder.typicode.com/users"
    emp_id = argv[1]
    emp_data = "{}/{}".format(original_url, emp_id)
    emp_name = requests.get(emp_data).json()['name']

    # get total number of tasks
    emp_tasks_url = "{}/{}/todos".format(original_url, emp_id)
    emp_tasks = requests.get(emp_tasks_url).json()
    number_tasks = len(emp_tasks)

    # get number of tasks completed
    tasks_completed = 0
    for task in emp_tasks:
        if task["completed"]:
            tasks_completed += 1

    # output
    print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                           tasks_completed,
                                                           number_tasks))
    for task in emp_tasks:
        if task["completed"]:
            print("\t", task["title"])
