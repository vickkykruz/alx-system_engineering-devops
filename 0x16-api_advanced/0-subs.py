#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re setting
a custom User-Agent.

Requirements:

    => Prototype: def number_of_subscribers(subreddit)
    => If not a valid subreddit, return 0.
    => NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
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
        # Convert the requestData to json
        data = requestData.json()

        return data['data']['subscribers']
    elif requestData.status_code == 404:
        # return o
        return 0
    else:
        return 0
