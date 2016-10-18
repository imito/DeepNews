# ===========================================================================
# This is a web crawler periodically mining news from known sources
# ===========================================================================
from __future__ import print_function, division, absolute_import

from six import add_metaclass
from abc import ABCMeta, abstractmethod


@add_metaclass(ABCMeta)
class Miner(object):
    """ Miner """

    def __init__(self):
        super(Miner, self).__init__()

    def authenticate(self):
        pass
