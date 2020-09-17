#!/usr/bin/python3
'''
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
'''
import json
import requests
from sys import argv


def top_ten(subreddit):
    '''
        queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit.
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    counter = 0
    if response.status_code != 404:
        for key in response.json()['data']['children']:
            print(key['data']['title'])
            counter += 1
            if counter == 10:
                break
    else:
        print (None)
