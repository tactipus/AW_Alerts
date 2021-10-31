# import tweepy as tw
from config import create_api
import subprocess

# Authorization protocol
# auth = tw.OAuthHandler("API KEY", "API SECRET KEY")
# auth.set_access_token("ACCESS TOKEN", "ACCESS TOKEN SECRET")

# Providing access to API
# API = tw.API(auth)

# Taking tweet as an input
tweet = input("Dump your thoughts here: ")

# Tweeting to the linked twitter account
API = create_api()
API.update_status(status=tweet)

button = "OK"

applescript = """
    display dialog "There is an update about Advance Wars." ¬
    with title "Discord Alert" ¬
    with icon caution ¬
    buttons "{}"
    """.format(button)

subprocess.call("osascript -e '{}'".format(applescript), shell=True)
