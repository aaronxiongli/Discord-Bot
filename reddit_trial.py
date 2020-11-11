import praw

reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',
                     client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',
                     user_agent='Shelly', username='Shelly_Cooper69')
subreddit=input("...")
post = reddit.subreddit(subreddit)
latest=post.hot(limit=1)
for submission in latest:
  print(submission.url)
