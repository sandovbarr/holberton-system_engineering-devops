#!/usr/bin/python3
'''
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
'''
import csv
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

    with open(id_user + '.csv', 'w') as file:
        writer = csv.writer(
            file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        for task in user_tasks_json:
            status = task['completed']
            task_tit = task['title']
            writer.writerow([id_user, usr_nme, status, task_tit])

except Exception:
    print('Not a valid argument')
