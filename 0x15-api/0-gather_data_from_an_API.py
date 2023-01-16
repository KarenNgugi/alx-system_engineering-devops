#!/usr/bin/python3


import requests
from sys import argv

if __name__ == "__main__":
  # get employee name
  emp_id = int(argv[1])
  emp_data = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
  emp_name = requests.get(emp_data).json()['name']
  
  # get total number of tasks
  emp_tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(emp_id)
  emp_tasks = requests.get(emp_tasks_url).json()
  number_tasks = len(emp_tasks)
  
  # get number of tasks completed
  tasks_completed = 0
  for task in emp_tasks:
    if task["completed"] == True:
      tasks_completed += 1
      
  # output
  print("Employee {} is done with tasks ({}/{})".format(emp_name, tasks_completed, number_tasks))
  for task in emp_tasks:
    if task["completed"] == True:
      print(task["title"])
