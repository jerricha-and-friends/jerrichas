# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3
# NOTE: Test files need to be unexecutable for Nose to run.

from ..base import BaseCostumeTestCase
from .. import fixtures
import csv
from jerrichas.costume import utils
from nose.plugins.attrib import attr
import os

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "../data/costumes")


class UtilsTestCase(BaseCostumeTestCase):
    """
    Tests jerrichas.costume.utils
    """
    def setUp(self):
        self.db = fixtures.mock_read_only_db()

    def tearDown(self):
        self.db.session.close()

    @attr('one')
    def test_face_scales(self):
        """
        Testing if jerrichas.costume.utils can parse into
        """
        ## Grab a costume_csv file and parse it
        costume = open(os.path.join(COSTUME_PATH, "facescales.fixture.csv"), "r")
        costume = csv.reader(costume).__next__()

        ## Construct dictionary from parse logic
        # Placeholder function -- replace UTILITY_FUNCTION with own methods directly from the util module
        def UTILITY_FUNCTION(x, y, z):
            x, y, z = map(lambda i: float(i) * 1000, [x,y,z])
            return round(x+y+z)

        scales = dict(
            ## Atomic ##
            # bodytype=int(costume[7]),
            # # skincolor=int(costume[8]),  # Conversion may be required
            # bodyscale=float(costume[9]),
            # bonescale=float(costume[10]),
            # shoulderscale=float(costume[12]),
            # chestscale=float(costume[13]),
            # waistscale=float(costume[14]),
            # hipscale=float(costume[15]),
            # legscale=float(costume[16]),

            # ## Head/Face Scales (Composites) ##
            headscales=UTILITY_FUNCTION(*costume[18:20+1]),
            browscales=UTILITY_FUNCTION(*costume[21:23+1]),
            cheekscales=UTILITY_FUNCTION(*costume[24:26+1]),
            chinscales=UTILITY_FUNCTION(*costume[27:29+1]),
            craniumscales=UTILITY_FUNCTION(*costume[30:32+1]),
            jawscales=UTILITY_FUNCTION(*costume[33:35+1]),
            nosescales=UTILITY_FUNCTION(*costume[36:38+1]),
        )

        ## Compare with whats in DB
        db_scales = self.db.session.execute("SELECT * FROM costume WHERE character=1 AND costume=9;").fetchone()
        # print({k: type(v) for k, v in db_scales.items()}); assert False;  # Returns a dictionary comprehension of the type of each column value
        # db_scales = {k: str(v) for k, v in db_scales.items()} # Transform
        for k, v in scales.items():
            self.assertEqual(v, db_scales[k],
                "[{k}] does not equal ParagonChat.costume.{k}".format(k=k))
