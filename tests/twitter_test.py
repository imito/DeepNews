from __future__ import print_function, division, absolute_import

import os
import cPickle
import requests
import webbrowser
from twython import Twython

from odin import utils

# ===========================================================================
# Constants
# ===========================================================================
CONSUMER_KEY = os.environ['TWITTER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_SECRET']
SAVE_PATH = utils.get_logpath('twitter.log', override=False)

# ===========================================================================
# First authentication
# ===========================================================================
if not os.path.exists(SAVE_PATH):
    twitter = Twython(app_key=CONSUMER_KEY, app_secret=CONSUMER_SECRET)
    user_timeline = twitter.get_user_timeline(screen_name="NgoTrongTrung")
    auth = twitter.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    # ====== Getting the PIN using verifier URL ====== #
    webbrowser.open(auth['auth_url'])
    PIN = raw_input('We will open browser, copy the PIN code here:')
    if len(PIN) != 7:
        raise ValueError('PIN must be 7 numbers.')
    # ====== Next, authorize using given PIN ====== #
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    # Getting the FINAL authentication tokens
    final_step = twitter.get_authorized_tokens(PIN)
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    user_id = final_step['user_id']
    screen_name = final_step['screen_name']
    # ====== save everything ====== #
    cPickle.dump({'CONSUMER_KEY': CONSUMER_KEY,
                  'CONSUMER_SECRET': CONSUMER_SECRET,
                  'OAUTH_TOKEN': OAUTH_TOKEN,
                  'OAUTH_TOKEN_SECRET': OAUTH_TOKEN_SECRET,
                  'user_id': user_id,
                  'screen_name': screen_name},
                 open(SAVE_PATH, 'w'), protocol=cPickle.HIGHEST_PROTOCOL)
# ===========================================================================
# Load old authentication information
# ===========================================================================
else:
    _ = cPickle.load(open(SAVE_PATH, 'r'))
    CONSUMER_KEY = _['CONSUMER_KEY']
    CONSUMER_SECRET = _['CONSUMER_SECRET']
    OAUTH_TOKEN = _['OAUTH_TOKEN']
    OAUTH_TOKEN_SECRET = _['OAUTH_TOKEN_SECRET']
    user_id = _['user_id']
    screen_name = _['screen_name']

# ===========================================================================
# Final step
# ===========================================================================
# ====== authorized ====== #
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
timeline = twitter.get_user_timeline(screen_name=screen_name)
print(timeline)
twitter.get_user_timeline
