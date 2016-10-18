# ===========================================================================
# This class receive a list of mined object and return a list
# of formatted string for sending the email notification
# ===========================================================================
from __future__ import print_function, division, absolute_import

from six import add_metaclass
from abc import ABCMeta, abstractmethod


@add_metaclass(ABCMeta)
class Filter(object):
    """ Filter """

    def __init__(self):
        super(Filter, self).__init__()

    def test(self):
        pass
