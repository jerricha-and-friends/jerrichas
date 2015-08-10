# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3
from .costume_csv import CostumeCSV
from .tailor_costume import TailorCostume

class BaseCostumeSave(object):
    """
    Parent class for all costume files that Jerrichas supports.
    """
    def __init__(self, fp):
        """
        :param fp: a file
        :type fp: file
        """
        self.fp = fp

    def get_costumeparts(self):
        """
        :returns: a mapping of costumepart elements to ParagonChatDB 'costumepart' columns
        """
        self.fp.seek(0)

    def get_proportions(self):
        """
        :returns: a mapping of costume proportions to ParagonChatDB 'costume' columns.
        """
        self.fp.seek(0)
