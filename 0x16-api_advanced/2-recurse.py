#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ This is a Recivse function """
    global after
    # Reddit API endpoint for hot posts in a subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    # Define a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Make the API request
    response = requests.get(url,
                            headers=headers,
                            params=parameters,
                            allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        after_data = response.json().get("data").get("after")

        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")

        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))

        return hot_list
    elif response.status_code == 404:
        # Subreddit not found, return None
        return None
    else:
        # Handle other errors by printing the status code and returning None
        print(f"Error: {response.status_code}")
        return None
