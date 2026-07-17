#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu.api:v1.0 (by /u/blewis-bump)"
    }

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code == 404:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data").get("children")

    for post in posts:
        print(post.get("data").get("title"))
