import pandas as pd
import advertools as adv
import yagmail
from datetime import date
from config import *

# takes today's date and uses it to filter out Twitter posts that aren't from today
today = str(date.today())
# authorizes this bot to access the Twitter API
adv.twitter.set_auth_params(**auth_params)

# the Twitter handles and keywords stored in a dict that will be used to parse posts
# a pandas dataframe is set up to store the tweets that pass muster
alerts_list = {"pentestingpoet": "#AdvanceWars", "NintendoAmerica": "#AdvanceWars", "OperationWarzo1": "#AdvanceWars"}
df1 = pd.DataFrame(columns=['TwitterHandle', 'Message'])

# iterates over the alerts_list dict and finds tweets that match and adds them to the df1 dataframe
for keys, values in alerts_list.items():
    df = adv.twitter.get_user_timeline(screen_name=keys, tweet_mode="extended")
    df['tweet_created_at'] = df['tweet_created_at'].astype('string')
    df = df[df['tweet_full_text'].str.contains(values, regex=True) & df['tweet_created_at'].str.contains(today)]
    if len(df.index) > 0:
        df1 = df1.append({'TwitterHandle': keys, 'Message': df['tweet_full_text']}, ignore_index=True)

# turns the dataframe into a dict
getlist = dict(zip(df1['TwitterHandle'].tolist(), df1['Message'].tolist()))
email_message = ""

# the function that sends the email alert; uses yagmail module to send
def send_alert(email_message, method):
    if method == 1:
        body = email_message
        yag = yagmail.SMTP("paul.alzate1991@gmail.com")
        yag.send(to="maverick.alzate@gmail.com", subject="Twitter Alert", contents=body,)
    print("Email sent!")

# checks if the dataframe has tweets for that day. If so, converts dataframe into readable string object
if len(df1.index) > 0:
    for key, value in getlist.items():
        email_message += key + ": " + value + "\n"
    method = 1
    email_message = email_message.to_string()
    send_alert(email_message, method)
