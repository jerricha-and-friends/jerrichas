from . import fixtures
import os
from unittest import TestCase

PATH = os.path.split(os.path.realpath(__file__))[0]

class BaseDBTestCase(TestCase):
    def setUp(self):
        self.db_path = None

    def tearDown(self):
        pass

class CostumesaveTestCase(TestCase):
    pass

class ConfigTestCase(TestCase):
    pass

class EventTestCase(TestCase):
    pass
