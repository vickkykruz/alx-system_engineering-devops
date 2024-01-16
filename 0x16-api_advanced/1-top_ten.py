#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ This is function that return the top ten posts """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'script for 0x16-api_adavance: by (vickkykruz)'}
    params = {'limit': 10 }

    requestData = requests.get(url,
                               headers=headers,
                               params=params,
                               allow_redirects=False)

    if requestData.status_code == 200:

        data = requestData.json()
        for title in data['data']['children']:
            print(title['data']['title'])
    else:
        print("None")
