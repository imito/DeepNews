from __future__ import print_function, division, absolute_import

from twitter_miner import TwitterMiner

miner = TwitterMiner()
miner.authenticate()
print(miner.get_timeline())
