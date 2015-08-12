# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3
# NOTE: Test files need to be unexecutable for Nose to run.

from ..base import BaseCostumeTestCase
from .. import fixtures
from jerrichas.costume import CostumeCSV
from nose.plugins.attrib import attr
import os

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "../data/costumes")


class CostumeCSVTestCase(BaseCostumeTestCase):
    """
    Tests jerrichas.costume.CostumeCSV
    """

    # @attr('one')
    def test_init(self):
        """
        Testing jerrichas.CostumeCSV.__init__
        """
        costume_csv = CostumeCSV(open(os.path.join(COSTUME_PATH, "jerrichamask.save.csv"), "r"))
        self.assertIsNotNone(costume_csv, "CostumeCSV successfully created")
        self.assertEqual(type(costume_csv.fp).__name__, "TextIOWrapper", "File OK")

    # @attr('one')
    def test_get_costumeparts(self):
        """
        Testing jerrichas.CostumeCSV.get_costumeparts
        """
        costume_csv = fixtures.mock_costumecsv_female()

        # Each line in a costumesave csv file corresponds to a costume part. Let `csv_part_count` be number of lines in the file, and parsed_part_count the number of lines parsed
        csv_part_count = len(costume_csv.fp.readlines())
        parsed_part_count = len(costume_csv.get_costumeparts())
        self.assertEqual(parsed_part_count, csv_part_count, "Costume part count equal to those in file.")

    # @attr('one')
    def test_get_proportions(self):
        """
        Testing jerrichas.CostumeCSV.get_costumeparts
        """
        costume_csv = fixtures.mock_costumecsv_female()

        proportions = costume_csv.get_proportions()
        self.assertGreaterEqual(len(proportions), 7, "Proportions parsed.")
