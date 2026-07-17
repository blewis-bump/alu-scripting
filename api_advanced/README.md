# API advanced

Scripts that query the [Reddit API](https://www.reddit.com/dev/api/) using the
`Requests` module.

## Files

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` -> total subscribers (0 if invalid) |
| `1-top_ten.py` | `top_ten(subreddit)` -> prints the 10 hottest post titles |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` -> recursively lists all hot titles |
| `3-count.py` | `count_words(subreddit, word_list)` -> sorted keyword counts |

No authentication is required; a custom `User-Agent` is set to avoid rate limits,
and redirects are disabled so invalid subreddits are detected instead of followed.
