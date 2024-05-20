#!/usr/bin/python3
"""
This script uses a REST API to fetch information about all employees' TODO list progress and exports the data to a JSON file.
"""

import json
import requests


def fetch_all_users():
    """Fetch data for all users."""
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    return response.json()


def fetch_todo_data(user_id):
    """Fetch TODO list data for a given user ID."""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    return response.json()


def main():
    users = fetch_all_users()

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos = fetch_todo_data(user_id)

        tasks_list = [{"username": username,
                       "task": todo.get('title'),
                       "completed": todo.get('completed')} for todo in todos]

        all_tasks[user_id] = tasks_list

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
