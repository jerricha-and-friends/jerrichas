# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3
# NOTE: Test files need to be unexecutable for Nose to run.

from . import fixtures
from jerrichas.database import ParagonChatDB
from nose.plugins.attrib import attr
import os
import shutil
from unittest import TestCase

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "data/costumes")


class ParagonChatDBTestCase(TestCase):
    """
    Tests jerrichas.database.ParagonChatDB
    """
    def setUp(self):
        # Copy .fixture db into .testing db
        db_path = os.path.join(PATH, "data/ParagonChat.db.testing")
        fixture_db = os.path.join(PATH, "data/ParagonChat.db.fixture")
        shutil.copy(fixture_db, db_path)
        self.db = ParagonChatDB(db_path)

    def tearDown(self):
        self.db.session.close()

    # @attr('one')
    def test_query_replace_costume(self):
        """
        Testing jerrichas.ParagonChatDB.query_replace_costume
        """
        costume_csv = fixtures.mock_costumecsv_female()
        sql_script = self.db.query_replace_costume(
            costumesave=costume_csv,
            character_id=1,
            costume_id=0,
        )

        success = self.db._transact_query(sql_script)
        self.assertTrue(success, "Transaction was successful.")
