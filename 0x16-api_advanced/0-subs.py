#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of total subscribers"""
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
                                    
    response_data = response.json()
    return response_data.get('data', {}).get('subscribers', 0)
