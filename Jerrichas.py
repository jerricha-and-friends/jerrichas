#!/usr/bin/env python
import os, sys
VERSION = "0.1.0"
__doc__ = """\
##### Jerricha's ParagonChat Costume Utility v.{} Info ######
Jerrichas.py will automatically replace a costume in your DB with a
"costumesave" save.

Instructions:
1. Install latest Python 3 from https://www.python.org/downloads/
2. Set two global variables in this file.
    a. Set PARAGON_CHAT_DB to your ParagonChat.db location. (usually that's
       "%APPDATA%\Paragon Chat\Database\ParagonChat.db") (I've already set it
       there, so you usually don't have to change it.)
    b. Set COSTUME_FILE to your file that you created with "/costumesave
       myfile" in Icon.exe. Usually stored in "City of Heroes\Data" *NOTE*:
       Your costume file is NOT the same as the .costume files that are saved
       from the Character Creator in Icon.exe. See
       http://www.cohtitan.com/forum/index.php?topic=11076.0 for more info.
4. BACKUP your ParagonChat.db file! Jerrichas will also *try* to make a backup
   of the DB, but you never know what happens!
5. Open up a shell prompt, and run me with 'python Jerrichas.py' or
   'c:\Python34\python.exe Jerrichas.py', and follow the on-screen wizard.
6. Please report your errors to me on the forums! This program has really
   shakey error handling currently!

LEGAL: GPLv3. No warrenties. Use it, share it, hack it, but DO NOT sell it!
Love <3 Jerricha, Summer of 2015\
""".format(VERSION)
PARAGON_CHAT_DB = os.getenv('appdata') + """\Paragon Chat\Database\ParagonChat.db"""
COSTUME_FILE = """Replace_Me"""
###########################
### PROGRAM BEINGS HERE ###
###########################
PARAGON_CHAT_DB = PARAGON_CHAT_DB.replace(os.path.sep, '/')
COSTUME_FILE = COSTUME_FILE.replace(os.path.sep, '/')

from io import StringIO


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
        try:
            self.db_fp = db_fp
            self.conn = sqlite3.connect(self.db_fp)
            self.conn.row_factory = self._dict_factory
            self.session = self.conn.cursor()
        except:
            sys.exit("ERROR: Jerrichas terminating\nSomething went wrong with the DB.")

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def make_backup(self):
        "Backs-up yo shit."
        from shutil import copy
        backup_fp = os.path.join(os.path.split(PARAGON_CHAT_DB)[0], "ParagonChat.db.jerrichas")
        try:
            copy(PARAGON_CHAT_DB, backup_fp)
        except IOError:
            sys.exit("ERROR: Jerrichas terminating\nUnable to make a backup of your DB.")
        return True

    def get_accounts(self):
        accounts = self.session.execute("SELECT id, name FROM account")
        return accounts.fetchall()

    def get_characters(self, account):
        characters = self.session.execute("SELECT id, name FROM character WHERE account='{}'".format(account))
        return characters.fetchall()

    def replace_costume(self, character_id, costume_id, costume_file=COSTUME_FILE):
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


def _validate_choice(choice, lst):
    return True if len(list(filter(lambda row: choice == str(row['id']), lst))) == 1 else False


def _display_choice(table, title):
    display = StringIO("")
    display.write("====={title}=====\n".format(title=title.capitalize()))
    for row in table:
        display.write("{id}: {name}\n".format(**row))
    display.write("\n")
    return display.getvalue()


def event_loop(db):
    #To be refactored
    accounts = db.get_accounts()
    if len(accounts) == 1:
        account_id = 1
    else:
        # Choose Account sub-loop
        while True:
            print(_display_choice(accounts, "accounts"))
            try:
                account_id = str(input("Select your account ID [1-{}]: ".format(len(accounts))))
                assert _validate_choice(account_id, accounts) is True
                break
            except:
                print("Invalid input.")

    # Choose Character sub-loop
    characters = db.get_characters(account_id)
    while True:
        print(_display_choice(characters, "characters"))
        try:
            character_id = str(input("Select your character ID [1-{}]: ".format(len(characters))))
            assert _validate_choice(character_id, characters) is True
            break
        except:
            print("Invalid input.")

    # Choose Costume sub-loop
    character = db.session.execute("SELECT name, class, curcostume FROM character WHERE id='{}'".format(character_id)).fetchone()
    while True:
        try:
            costume_id = str(input("\nYou have selected: {name} ({class})\nSelect costume ID to replace [0-9, current: {curcostume}]: ".format(**character)))
            assert costume_id in [str(i) for i in range(10)]
            break
        except:
            print("Invalid input.")

    # Confirm Selection
    confirm = str(input("\nWe're about to replace {name}'s costume #{costume_id} with the /costumesave file '{COSTUME_FILE}'\nThis change is permanent, and may result in a corrupt DB file -- please make sure to backup your DB!\n(Jerricha's will also backup your DB in _backup\ParagonChat.db) \nDo you wish to proceed? (you must type exactly 'y' or 'yes') [ Yes / No ]: "
        .format(COSTUME_FILE=COSTUME_FILE, costume_id=costume_id, name=character['name']))).lower()
    if confirm == 'y' or confirm == 'yes':
        print("Backing up your DB to 'ParagonChat.db.jerrichas'...")
        db.make_backup()
        print("Performing costume replace on 'ParagonChat.db'...")
        db.replace_costume(character_id=character_id, costume_id=character_id)
        print("DONE! Thanks for using Jerricha's!")
    else:
        print("\n\nNothing was modified in your DB. Thanks for using Jerricha's!")


def main():
    print("### <3 Jerricha's ParagonChat Costume Utility v{} <3 ###".format(VERSION))
    if COSTUME_FILE == "Replace_Me":
        sys.exit(__doc__)
    test_paths()
    db = Database()
    event_loop(db)


if __name__ == '__main__':
    main()
