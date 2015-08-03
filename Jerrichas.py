#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Requires Python 3
import os, sys
VERSION = "0.1.0"
__doc__ = """\
##### Jerricha's ParagonChat Costume Utility v.{} Info ######
Jerrichas.py will automatically replace a costume in your DB with a "costumesave" save.

Instructions:
1. Install latest Python 3 from https://www.python.org/downloads/
2. Set two global variables in this file.
    a. Set PARAGON_CHAT_DB to your ParagonChat.db location. (usually that's "%APPDATA%\Paragon Chat\Database\ParagonChat.db") (I've already set it there, so you usually don't have to change it.)
    b. Set COSTUME_FILE to your file that you created with "/costumesave myfile" in Icon.exe. Usually stored in "City of Heroes\Data"
        *NOTE*: Your costume file is NOT the same as the .costume files that are saved from the Character Creator in Icon.exe. See http://www.cohtitan.com/forum/index.php?topic=11076.0 for more info.
4. Run me with 'python Jerrichas.py' or 'c:\Python34/python.exe Jerrichas.py'
5. Please report your errors to me on the forums! This program has really shakey error handling currently!

LEGAL: GPLv3. No warrenties. Use it, share it, hack it, but don't sell it!\
""".format(VERSION)
PARAGON_CHAT_DB = os.getenv('appdata') + """\Paragon Chat\Database\ParagonChat.db"""
COSTUME_FILE = """tests/cooltrench_w_boots"""
# COSTUME_FILE = """Replace_Me"""
####################################################
###########################
### PROGRAM BEINGS HERE ###
###########################
PARAGON_CHAT_DB = PARAGON_CHAT_DB.replace(os.path.sep, '/')
COSTUME_FILE = COSTUME_FILE.replace(os.path.sep, '/')


def test_paths():
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
    try:
        costume_csv = csv.reader(open(costume_file, 'r'))
        costume = map(
            lambda row: dict(
                part=row[0],
                geom=row[1],
                tex1=row[2],
                tex2=row[3],
                fx=row[39] if not row[39]=="0" else "",
                displayname=row[4],
                region=row[42],
                bodyset=row[43],
                # name=row[],
                color1=row[5],
                # color2=row[],
                # color3=row[],
                # color4=row[],
            ),
            costume_csv
        )
    except Exception as e:
        sys.exit("Some kind of error with your costume file.\n{}".format(e))
    return list(costume)


class Database(object):
    def __init__(self, db_fp=PARAGON_CHAT_DB):
        import sqlite3
        self.conn = sqlite3.connect(db_fp)
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
        sql_script = StringIO("BEGIN;")
        for i in costumeparts:
            sql =\
                """\
DELETE FROM costumepart
    WHERE character='{character_id}'
        AND costume='{costume_id}'
        AND part='{part}' ;
REPLACE INTO costumepart (geom, tex1, tex2, fx, displayname, region, bodyset, color1, character, costume, part)
    VALUES ('{geom}', '{tex1}', '{tex2}', '{fx}', '{displayname}', '{region}', '{bodyset}', '{color1}', '{character_id}', '{costume_id}', '{part}');\
                """
            sql = sql.format(
                character_id=character_id,
                costume_id=costume_id,
                **i
            )
            sql_script.write(sql)
        try:
            self.session.executescript(sql_script.getvalue())
            self.conn.commit()
        except Exception as e:
            print(e)
            self.session.execute("ROLLBACK;")


def event_loop(db):
    while True:
        account_id = input("\n\nSelect your account id: ")
        # character_id = input("")
        # costume_id =


def main():
    print("### <3 Jerricha's ParagonChat Costume Utility v{} <3 ###".format(VERSION))
    if COSTUME_FILE == "Replace_Me":
        sys.exit(__doc__)
    test_paths()
    db = Database()
    event_loop(db)


if __name__ == '__main__':
    main()
