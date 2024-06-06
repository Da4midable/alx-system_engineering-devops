#!/usr/bin/python3
"""
This script defines a function `number_of_subscribers` that queries Reddit API
to return the number of subscribers for a given subreddit. If the subreddit
is invalid, the function returns 0.

Shebang:
#!/usr/bin/python3
- The shebang line at the top of the script indicates that the script should be
  executed using the Python 3 interpreter. This allows script to be run as an
  executable without explicitly invoking the Python interpreter.

Modules:
- `requests`: A Python library used to send HTTP requests. It allows you to
  send HTTP/1.1 requests, without need to manually add query strings to your
  URLs or to form-encode your POST data.

Function:
number_of_subscribers(subreddit):
    Queries the Reddit API and returns the number of subscribers for given
    subreddit. If an invalid subreddit is provided, the function returns 0.

    Args:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the subreddit, or 0 if the subreddit
    is invalid.

    Example Usage:
    >>> number_of_subscribers('python')
    945000

    This function constructs the URL for the subreddit's "about"
    page in JSON format, sends a GET request to the Reddit API
    with a custom User-Agent header, and then processes the response. If the
    response status code is 200 (OK), it extracts and returns the number of
    subscribers from the JSON response. If the subreddit is invalid or an
    error occurs, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of subscribers for given subreddit.
    If an invalid subreddit is provided, the function returns 0.

    Args:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: number of subscribers for subreddit, or 0 if subreddit is invalid
    """
    headers = {'User-Agent': '4MidableRedditAPI/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        return data['data']['subscribers']
    except Exception as e:
        print(None)
