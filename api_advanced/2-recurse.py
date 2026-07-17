#!/usr/bin/python3
"""Recursively query the Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot article titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python3:alu.api.advanced:v1.0.0 (by /u/ixhm-brix)"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
