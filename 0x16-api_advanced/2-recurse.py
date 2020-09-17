#!/usr/bin/python3
'''
    Recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit.

    If no results are found for the given subreddit,
    the function should return None.
'''
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    '''
        Recursive function that queries the Reddit API
        and returns a list containing the titles of all
        hot articles for a given subreddit.

        If no results are found for the given subreddit,
        the function should return None.
    '''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for key in response.json()['data']['children']:
            hot_list.append(key['data']['title'])
        after_page = response.json()['data']['after']
        if after_page is None:
            return hot_list
        recurse(subreddit, hot_list, after_page)
