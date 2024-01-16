#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """ This ia a function that return the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # To avoid error related to Too Many Request
    headers = {"User-Agent": "CustomUserAgent/1.0"}

    # Sent a get request to fetch the data
    requestData = requests.get(url, headers=headers)
    if requestData.status_code == 200:
        data = requestData.json()
        return data['data']['subscribers']
    else:
        return 0
