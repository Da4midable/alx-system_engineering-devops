#!/usr/bin/python3
"""
This script uses a REST API to fetch information about an
employee's TODO list progress and exports the data to a CSV file.
It takes an employee ID as an input and displays the progress
in a specific format.
"""

import requests
import sys
import csv


def fetch_user_data(user_id):
    """Fetch user data for a given user ID."""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    return response.json()


def fetch_todo_data(user_id):
    """Fetch TODO list data for a given user ID."""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    return response.json()


def main(user_id):
    user = fetch_user_data(user_id)
    todos = fetch_todo_data(user_id)

    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]

    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = total_tasks

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csvwriter.writerow([user_id, user.get('username'), task.get('completed'), task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(user_id)
