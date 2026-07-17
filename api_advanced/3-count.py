#!/usr/bin/python3
"""Recursively query the Reddit API and count keywords in hot titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found across hot post titles."""
    if counts is None:
        counts = {}
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
        return
    data = response.json().get("data", {})
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0) + title.count(key)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    printable = sorted(
        [(k, v) for k, v in counts.items() if v > 0],
        key=lambda kv: (-kv[1], kv[0])
    )
    for key, value in printable:
        print("{}: {}".format(key, value))
