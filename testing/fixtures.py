import os

PATH = os.path.split(os.path.realpath(__file__))[0]

def mock_db():
    return os.path.join(PATH, "data/ParagonChat.db")

def mock_costumesave_female():
    return os.path.join(PATH, "data/mock_costume_female")
