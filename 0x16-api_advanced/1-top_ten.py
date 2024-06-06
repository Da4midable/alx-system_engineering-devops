#!/usr/bin/python3
"""
A script to fetch and display the top ten hot post titles from given subreddit.

This script uses the Reddit API to fetch the top ten hot posts from a specified
subreddit and prints their titles. If the subreddit is invalid or an error
occurs, it prints None.

Functions:
    top_ten(subreddit): Fetches and prints the titles of the top ten hot posts
                        from the specified subreddit.

Example usage:
    python3 script.py subreddit_name
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the top ten hot posts from a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints titles of top ten hot posts or None if an error occurs.
    """
    headers = {'User-Agent': '4MidableRedditAPI/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        titles = [post['data']['title'] for post in posts]

        for title in titles:
            print(title)

    except Exception as e:
        print(None)
