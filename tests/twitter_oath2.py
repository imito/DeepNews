from __future__ import print_function, division, absolute_import

import os
import requests
import webbrowser
from twython import Twython


from odin import utils

CONSUMER_KEY = os.environ['TWITTER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_SECRET']
SAVE_PATH = utils.get_logpath('twitter')

# print(auth)
twitter = Twython(app_key=CONSUMER_KEY, app_secret=CONSUMER_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(CONSUMER_KEY, access_token=ACCESS_TOKEN)
search_results = twitter.search(q='WebsDotCom', count=50)
print(search_results)
