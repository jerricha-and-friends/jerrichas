# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3

import os
from unittest import TestCase

PATH = os.path.split(os.path.realpath(__file__))[0]


class BaseCostumeTestCase(TestCase):
    """
    Data serialization from various Costume formats
    """
    def setUp(self):
        pass

class ConfigTestCase(TestCase):
    pass

class EventTestCase(TestCase):
    pass
