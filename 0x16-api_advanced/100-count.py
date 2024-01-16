#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords (
case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    headers = {
        'User-Agent': 'CustomUserAgent',  # Add a proper User-Agent header
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error accessing subreddit: {response.status_code}")
        return

    data = response.json()

    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            title = post['data']['title'].lower()

            for word in word_list:
                word_lower = word.lower()

                if word_lower not in counts:
                    counts[word_lower] = 0

                counts[word_lower] += title.count(word_lower)

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)


def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
