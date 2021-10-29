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



# tweet_list = []


# class MyStreamListener(tw.Stream):
#     def __init__(self, api=None):
#         super(MyStreamListener, self).__init__()
#         self.num_tweets = 0
#         self.file = open("tweet.txt", "w")
#
#     def on_status(self, status):
#         tweet = status.json
#         self.file.write(json.dumps(tweet) + "\n")
#         tweet_list.append(status)
#         self.num_tweets += 1
#
#         if self.num_tweets < 1000:
#             return True
#         else:
#             return False
#         self.file.close()
#
#
# # create streaming object and authenticate
# l = MyStreamListener()
# l.__init__(auth)
# l(api=auth)
# stream = tw.Stream(l)
#
# # this line filters twitter streams to capture data by keywords
# stream.filter(["advance wars", "nintendo", "intelligent systems",
#                "advance", "wars", "Switch"])
#
# # read tweets stored in the file
# tweets_data_path = "copp.txt"
# tweets_data = []
# tweets_file = open(tweets_data_path, "r")
#
# # read in tweets and store on list
# for line in tweets_file:
#     tweet = json.loads(line)
#     tweets_data.append(tweet)
#
# tweets_file.close()
# print(tweets_data[0])