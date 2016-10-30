# ===========================================================================
# This is a web crawler periodically mining news from known sources
# ===========================================================================
from __future__ import print_function, division, absolute_import

import os
from six import add_metaclass
from abc import ABCMeta, abstractmethod

from odin import utils


@add_metaclass(ABCMeta)
class Miner(object):
    """ Miner """

    def __init__(self):
        super(Miner, self).__init__()
        self.configurations = {}
        self._is_authenticated = False

    @property
    def authenticated(self):
        return self._is_authenticated

    @property
    def cache_path(self):
        return utils.get_logpath(self.__class__.__name__,
                                 override=False)

    # ==================== abstract methods ==================== #
    @abstractmethod
    def _authenticate(self):
        pass

    @abstractmethod
    def _news(self):
        pass

    # ==================== API methods ==================== #
    def authenticate(self):
        if not self._is_authenticated:
            try:
                self._authenticate()
            except:
                raise Exception('Authentication Failed!')
            print('Authentication Success!')
            self._is_authenticated = True
        return self

    def get_timeline(self, user_name=None, user_id=None):
        raise NotImplementedError

    def get_news(self):
        return self._news()

    def reset(self):
        if os.path.exists(self.cache_path):
            os.remove(self.cache_path)
        self._is_authenticated = False
