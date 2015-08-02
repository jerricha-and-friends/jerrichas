#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Requires Python 3
VERSION = "0.1.0"
##### Jerricha's ParagonChat Costume Utility ######
# Jerrichas.py will automatically replace a costume in your DB with a "costumesave" save.
# Instructions:
# 1. Install Python3
#   1a. (NB: I tried to make this 2-3 compatible, but Python2's
#     sqlite lib doesn't support WAL)
# 2. Set PARAGON_CHAT_DB to your ParagonChat.db location. (usually that's %APPDATA%\Paragon Chat\Database\ParagonChat.db). Make sure to CLOSE the ParagonChat program completely.
#       a. You usually won't have to change this variable,
#          unless you're on a Mac or have a funky Windows setup!
# 3. Set COSTUME_FILE to your file that you created with "/costumesave myfile" in Icon.exe. Note this file generated with "costumesave" is NOT the same as the .costume want to set it to the full Windows path, eg, "c:\Program Files\City of Heroes\Data\my_super_costume" but you can also use relative paths.
# 4. RUN me with 'python ParagonChatCostumeUtil.py' or 'c:\Python34/python.exe ParagonChatCostumeUtil.py'
## LEGAL: GPLv3. No warrenties. Use it, share it, hack it, but don't sell it!
####
####CHANGELOG####
### Aug-02-2015
# * Wrote all the things and published
import os
PARAGON_CHAT_DB = os.getenv('appdata') + """\Paragon Chat\Database\ParagonChat.db"""
# PARAGON_CHAT_DB = """tests\ParagonChat2.db"""
COSTUME_FILE = """tests\cooltrench_w_boots"""
###########################
### PROGRAM BEINGS HERE ###
###########################
PARAGON_CHAT_DB = PARAGON_CHAT_DB.replace(os.path.sep, '/')
COSTUME_FILE = COSTUME_FILE.replace(os.path.sep, '/')


def test_paths():
    import sys
    try:
        assert os.path.exists(PARAGON_CHAT_DB) is True
    except Exception:
        sys.exit("ERROR: PARAGON_CHAT_DB path is invalid.\nYou provided:\n\t{}"
            .format(PARAGON_CHAT_DB.replace('/', os.path.sep)))

    try:
        assert os.path.exists(COSTUME_FILE) is True
    except Exception:
        sys.exit("ERROR: COSTUME_FILE path is invalid.\nYou provided:\n\t{}"
            .format(COSTUME_FILE.replace('/', os.path.sep)))

    return True


def read_costumepart(costume_file=COSTUME_FILE):
    import csv
    costume_csv = csv.reader(open(costume_file, 'r'))
    costume = map(
        lambda row: dict(
            part=row[0],
            geom=row[1],
            tex1=row[2],
            tex2=row[3],
            fx=row[39],
        ),
        costume_csv
    )
    return list(costume)

class Database(object):
    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect(PARAGON_CHAT_DB)
        self.conn.row_factory = self._dict_factory
        self.session = self.conn.cursor()

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_accounts(self):
        accounts = self.session.execute("SELECT id, name FROM account")
        return accounts.fetchall()

    def get_characters(self, account):
        characters = self.session.execute("SELECT id, name, class, curcostume FROM character WHERE account='{}'".format(account))
        return characters.fetchall()

    def replace_costume(self, character_id, costume_id, costume_file=COSTUME_FILE):
        from io import StringIO
        costumeparts = read_costumepart(costume_file)
        sql_script = StringIO()
        # try:
        #     db.session.execute("BEGIN TRANSACTION")
        for i in costumeparts:
            sql =\
"""\
DELETE FROM costumepart
    WHERE character='{character_id}'
        AND costume='{costume_id}'
        AND part='{part}' ;
REPLACE INTO costumepart (geom, tex1, tex2, fx, character, costume, part)
    VALUES ('{geom}', '{tex1}', '{tex2}', '{fx}', '{character_id}', '{costume_id}', '{part}');
"""
# """\
# UPDATE costumepart
#     SET geom='{geom}',
#         text1='{tex1}',
#         text2='{tex2}',
#         fx='{fx}'
#     WHERE character='{character_id}'
#         AND costume='{costume_id}'
#         AND part='{part}'
# """
            sql = sql.format(
                character_id=character_id,
                costume_id=costume_id,
                **i
            )
            sql_script.write(sql)
        print(sql_script.getvalue())
                # print(sql)
        #         db.session.executescript(sql)
        #     db.session.execute("COMMIT TRANSACTION")
        # except Exception as e:
        #     print(e)
        #     db.session.execute("ROLLBACK")

def event_loop():
    input()
    pass

def main():
    print(u"### Jerricha's ParagonChat Costume Utility v{} ###".format(VERSION))
    test_paths()
    # event_loop()
    # if test_paths() == True:
    #     pass
    # else:
    #     print("Error with path: ")
    # print PARAGON_CHAT_DB


if __name__ == '__main__':
    main()
