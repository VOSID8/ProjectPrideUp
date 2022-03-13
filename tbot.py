import tweepy
import time
CONSUMER_KEY = 'zRa8awbxC1BDio8VdqG88'
CONSUMER_SECRET = 'w3aLSX3bqenFVtL6XCKEbmgu2f7YFIxLrYbxy6hXF96Dxx'
ACCESS_KEY = '150269088487735-GujxFqFYftcFwLy9IkexH2aSOlxuaw'
ACESS_SECRET = 'xh5xHP6pMF8ackWNXYn7foYLZPt9Xn1XDA1xChb'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()
search = '#VOSID'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break