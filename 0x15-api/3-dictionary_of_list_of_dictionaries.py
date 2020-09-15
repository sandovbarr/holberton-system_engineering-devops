#!/usr/bin/python3
'''
    Records all tasks from all employees
    file output = todo_all_employees.json
'''
import json
import requests


try:
    all_users_tasks = {}
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    for user in user_data.json():
        id_user = user['id']
        usr_nme = user['username']

        user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            params={'userId': id_user})
        user_tasks_json = user_tasks.json()
        tasks_list = []

        for task in user_tasks_json:
            del task['userId']
            del task['id']
            task['username'] = usr_nme
            task['task'] = task.pop('title')
            task['completed'] = task.pop('completed')
            tasks_list.append(task)
        all_users_tasks[id_user] = tasks_list

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_users_tasks, file)

except Exception:
    print('Not a valid argument')
