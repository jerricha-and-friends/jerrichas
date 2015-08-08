from .base import BaseCostumeTestCase
from jerrichas.costume import CostumeCSV
from nose.plugins.attrib import attr
import os

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "data/costumes")

class CostumeCSVTestCase(BaseCostumeTestCase):
    """
    Used to test CRUD transactions against the ParagonChat database.
    """

    @attr('one')
    def test_setup(self):
        """
        Testing if nose is working!
        """
        self.assertTrue(True)
        return True
