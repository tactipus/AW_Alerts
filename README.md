This repo is a collectino of different functions that will parse Twitter posts for keywords that will trigger an email alert system.

I'm currently working on alert_system.py, which is the bot that does the above function. This file imports from config.py, which processes the Twitter API credentials and holds them in an api variable to authorize alert_system.py to access the Twitter API.

To run the script:

1. Set up yagmail (which works with gmail). Kindly follow the instructions here to set this up

2. You will have to apply for a developer account from Twitter which should take you a couple of hours to a few days. You will need the Twitter API credentials to connect to their API.

3. 

I've added comments to alert_system.py that indicate what the selected functions do. 