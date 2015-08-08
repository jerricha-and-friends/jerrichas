from jerrichas.database import ParagonChatDB
import os
import shutil
from unittest import TestCase

PATH = os.path.split(os.path.realpath(__file__))[0]

class BaseDBTestCase(TestCase):
    def setUp(self):
        # Copy .fixture db into .testing db
        db_path = os.path.join(PATH, "data/ParagonChat.db.testing")
        fixture_db = os.path.join(PATH, "data/ParagonChat.db.fixture")
        shutil.copy(fixture_db, db_path)
        self.db = ParagonChatDB(db_path)

    def tearDown(self):
        self.db.session.close()

class CostumesaveTestCase(TestCase):
    pass

class ConfigTestCase(TestCase):
    pass

class EventTestCase(TestCase):
    pass
