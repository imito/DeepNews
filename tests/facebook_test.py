from __future__ import print_function, division, absolute_import

import requests
import os
import facebook
import json


access_token = ''
g = facebook.GraphAPI(access_token)

def pp(o):
	print(json.dump(o, indent=1)

user = ''

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
groups = graph.get_connections(profile['id'], 'groups')

pp(groups)