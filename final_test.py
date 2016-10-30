from __future__ import print_function, division, absolute_import

from twitter_miner import TwitterMiner

miner = TwitterMiner()
print(miner.cache_path)
miner.authenticate()
