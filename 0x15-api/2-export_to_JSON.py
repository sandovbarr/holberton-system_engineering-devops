#!/usr/bin/python3
'''
    Records all tasks that are owned by this employee
    Format must be:
    { "USER_ID":
        [ {"task": "TASK_TITLE",
           "completed": TASK_COMPLETED_STATUS,
           "username": "USERNAME"}...
        ]
    }
    File name must be: USER_ID.json
'''
import json
import requests
from sys import argv


try:
    int(argv[1])
    id_user = argv[1]
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_user))
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={
            'userId': id_user})

    usr_nme = user_data.json()['username']
    user_tasks_json = user_tasks.json()

    user_tasks = {}
    tasks_list = []
    for task in user_tasks_json:
        del task['userId']
        del task['id']
        task['task'] = task.pop('title')
        task['completed'] = task.pop('completed')
        task['username'] = usr_nme
        tasks_list.append(task)
    user_tasks[id_user] = tasks_list

    with open(id_user + '.json', 'w') as file:
        json.dump(user_tasks, file)

except Exception:
    print('Not a valid argument')
