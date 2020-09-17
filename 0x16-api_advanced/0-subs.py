#!/usr/bin/python3
'''
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Queries the Reddit API and returns the number of subscribers
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 404:
        return (response.json()['data']['subscribers'])
    else:
        return (0)
