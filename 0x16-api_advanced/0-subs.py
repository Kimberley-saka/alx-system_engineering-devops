#!/usr/bin/python3
"""
gets number of subscribers of a subreddit

"""

import requests
import sys


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
