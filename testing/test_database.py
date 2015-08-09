# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3
# NOTE: Test files need to be unexecutable for Nose to run.

from .base import BaseDBTestCase
from . import fixtures
from jerrichas.database import ParagonChatDB
from nose.plugins.attrib import attr
import os

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "data/costumes")


class ParagonChatDBTestCase(BaseDBTestCase):
    """
    Tests jerrichas.database.ParagonChatDB
    """

    @attr('one')
    def test_query_replace_parts(self):
        """
        Testing jerrichas.ParagonChatDB.query_replace_parts
        """
        costume_csv = fixtures.mock_costumecsv_female()
        sql = self.db.query_replace_parts(
            costumesave=costume_csv,
            character_id=1,
            costume_id=0,
        )
        print(sql); assert False;
