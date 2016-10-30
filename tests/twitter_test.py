from __future__ import print_function, division, absolute_import

import os
import requests
from twython import Twython

CONSUMER_KEY = os.environ['TWITTER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_SECRET']

# print(auth)
twitter = Twython(app_key=CONSUMER_KEY, app_secret=CONSUMER_SECRET)
user_timeline = twitter.get_user_timeline(screen_name="NgoTrongTrung")
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

oauth_verifier_url = 
auth['auth_url']
print(oauth_verifier_url)
exit()
print('Verifier ...')
oauth_verifier = requests.get(oauth_verifier_url)
print(oauth_verifier.text)
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# Getting the FINAL authentication tokens
final_step = twitter.get_authorized_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
