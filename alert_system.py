import pandas as pd
import advertools as adv
import yagmail
from datetime import date
from config import *

today = str(date.today())
adv.twitter.set_auth_params(**auth_params)

alerts_list = {"pentestingpoet": "#AdvanceWars"}
df1 = pd.DataFrame(columns=['TwitterHandle', 'Message'])

for keys, values in alerts_list.items():
    df = adv.twitter.get_user_timeline(screen_name=keys, tweet_mode="extended")
    df['tweet_created_at'] = df['tweet_created_at'].astype('string')
    df = df[df['tweet_full_text'].str.contains(values, regex=True) & df['tweet_created_at'].str.contains(today)]
    if len(df.index) > 0:
        df1 = df1.append({'TwitterHandle': keys, 'Message': df['tweet_full_text']}, ignore_index=True)

getlist = dict(zip(df1['TwitterHandle'].tolist(), df1['Message'].tolist()))
emailmessage = ""


def send_alert(emailmessage, method):
    if method == 1:
        body = emailmessage
        yag = yagmail.SMTP("paul.alzate1991@gmail.com")
        yag.send(to="maverick.alzate@gmail.com", subject="Twitter Alert", contents=body,)
    print("Email sent!")


if len(df1.index) > 0:
    for key, value in getlist.items():
        emailmessage += key + ": " + value + "\n"
    method = 1
    emailmessage = emailmessage.to_string()
    send_alert(emailmessage, method)
