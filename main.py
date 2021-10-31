# this script will get tweets from Nintendo and check them for any advance wars news
import os.path
import tweepy as tw
import json
import pandas as pd

access_token = "1420795318946439168-JapwbXgRHc1tB14CTzfF77hK3W7Kzo"
access_token_secret = "z7kDABBFxkSxk1vMg4XGQe7ADLYg721tp52idKJ1qOAxO"
consumer_key = "ZwWvZ8OqX23X9XOeuUtNMEOqO"
consumer_secret = "WsG21qTFJsXGxWYmwLyvkA30P9aR89NQkqmbwrwRZGcpWu6E1g"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "advance+wars -filter:retweets"
date_since = "2021-9-1"

# collect tweets
tweets = tw.Cursor(api.search_tweets, lang="en", q=search_words, since_id=date_since).items(50)

# iterate and print tweets
# tweeties = [tweet.text for tweet in tweets]
# print(tweeties)

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]

tweet_text = pd.DataFrame(users_locs,
                          columns=['user', "location", "tweet"])
# print(tweet_text)

tweet_text.to_csv("/Users/pnalzate/Documents/GitHub/AW_Alerts/AW_Tweets.csv", sep='\t')

