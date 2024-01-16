#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ This is function that return the top ten posts """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    requestData = requests.get(url, headers=headers)

    if requestData.status_code == 200:

        data = requestData.json()
        for title in data['data']['children']:
            print(title['data']['title'])
    else:
        print("None")
