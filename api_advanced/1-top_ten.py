#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python3:alu.api.advanced:v1.0.0 (by /u/blewis-bump)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        timeout=10
    )

    except:  requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))
