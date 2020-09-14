#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.

    You must use urllib or requests module
    The script must accept an integer as a parameter,
    which is the employee ID
    The script must display on the standard output
    the employee TODO list progress in this exact format:

    First line:
        Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks,
        which is the sum of completed and non-completed tasks

    Second and N next lines:
        display the title of completed tasks:
        Tab TASK_TITLE (with 1 tabulation + 1 space before)
'''
import requests
from sys import argv


if argv[1] and argv[1].isnumeric():
    id_user = argv[1]
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_user))
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={
            'userId': id_user})

    username = user_data.json()['name']
    user_tasks_json = user_tasks.json()

    tasks_completed = []
    total_tasks = len(user_tasks_json)
    for task in user_tasks_json:
        if task['completed']:
            tasks_completed.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'.format(username,
                                                          len(tasks_completed),
                                                          total_tasks))
    for task in tasks_completed:
        print('\t {}'.format(task))
