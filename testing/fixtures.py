from jerrichas.costume import CostumeCSV
import os

PATH = os.path.split(os.path.realpath(__file__))[0]
COSTUME_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "data/costumes")

def mock_db():
    return os.path.join(PATH, "data/ParagonChat.db")

def mock_db_live():
    return os.path.join(os.getenv("APPDATA"), "Paragon Chat\Database\ParagonChat.db")

def mock_costumecsv_female():
    return CostumeCSV(open(os.path.join(COSTUME_PATH, "jerrichamask.save.csv"), "r"))

def mock_costumecsv_female_cherrypicked():
    return CostumeCSV(open(os.path.join(COSTUME_PATH, "trenchcoat_cherrypicked.save.csv")))
