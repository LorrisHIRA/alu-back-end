#!/usr/bin/python3
"""
Gather data from an API for a given employee ID
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = []

    for task in todos:
        if task.get("completed") is True:
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title"))) 