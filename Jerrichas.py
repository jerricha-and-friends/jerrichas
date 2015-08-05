#!/usr/bin/env python
VERSION = "0.2.0"
__doc__ = """\
##### Jerricha's ParagonChat Costume App v.{} ######
Jerrichas.py will automatically replace a costume in your DB with a
"costumesave" save.

Instructions:
1. Open up jerrichas.config (I've JUST created it in this folder).
    a. Set COSTUME_FILE to your file that you created with "/costumesave
       myfile" in Icon.exe. Usually stored in "City of Heroes\Data" *NOTE*:
       Your costume file is NOT the same as the .costume files that are saved
       from the Character Creator in Icon.exe. See
       http://www.cohtitan.com/forum/index.php?topic=11076.0 for more info.
    b. If you have some weird installation of ParagonChat, you can set  PARAGON_CHAT_DB to your ParagonChat.db location. (usually that's
       %%(APPDATA)s\Paragon Chat\Database\ParagonChat.db") I've already set it
       there, so you usually don't have to change it.
2. BACKUP your ParagonChat.db file! Jerrichas will also *try* to make a backup
   of the DB, but you never know what happens!
3. Open up a shell prompt (Windows Key + R, type 'cmd.exe')
3. Follow the on-screen wizard. Jerrichas currently only supports batch replace of a costumesave file over a given costume.
4. Please report your errors to me on the forums
   ( http://www.cohtitan.com/forum/index.php?topic=11197.msg189486 )!

LEGAL: GPLv3. No warrenties. Use it, share it, hack it, but DO NOT sell it!
Love <3 Jerricha, Summer of 2015\
""".format(VERSION)
###########################
### PROGRAM BEINGS HERE ###
###########################
from io import StringIO
import os
import sys


def get_from_config(config_file):
    """
    Performs config validation, and returns values from config.
    If config validation fails (but not path validation), assume it's corrupt, make a new config file.
    :returns: PARAGON_CHAT_DB, COSTUME_FILE if successful
    """
    from configparser import ConfigParser
    config = ConfigParser(dict(APPDATA=os.environ['APPDATA']))
    try:
        config.read(config_file)
        PARAGON_CHAT_DB = config.get("Jerrichas", "PARAGON_CHAT_DB")
        COSTUME_FILE = config.get("Jerrichas", "COSTUME_FILE")
    except:
        default_config = """[Jerrichas]
COSTUME_FILE = Replace_Me
PARAGON_CHAT_DB = %(APPDATA)s\Paragon Chat\Database\ParagonChat.db"""

        f = open("./jerrichas.config", "w")
        f.write(default_config)
        f.close()
        print(__doc__)
        input("\nPress Enter to continue...!")
        sys.exit(1)

    return PARAGON_CHAT_DB, COSTUME_FILE


def test_paths(PARAGON_CHAT_DB, COSTUME_FILE):
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


class Costumesave(object):
    """
    Represents a file produced with the /costumesave command in Icon.exe
    """
    def __init__(self, costumesave):
        """
        :param costumesave: /costumesave file object
        :type costumesave: file
        """
        self.costumesave = costumesave

    def get_costumeparts(self):
        """
        :returns: a mapping of /costumesave elements to 
        """
        import csv
        try:
            costume_csv = csv.reader(open(self.costumesave), 'r')
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
    def __init__(self, db_path):
        import sqlite3
        try:
            self.db_path = db_path
            self.conn = sqlite3.connect(self.db_path)
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

    def replace_costume(self, character_id, costume_id, costume_file):
        costumeparts = read_costumepart(costume_file)
        sql_script = StringIO("""\
DELETE FROM costumepart
    WHERE character='{character_id}'
        AND costume='{costume_id}';""")
        for i in costumeparts:
            sql =\
                """\
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
        .format(COSTUME_FILE=None, costume_id=costume_id, name=character['name']))).lower()
    if confirm == 'y' or confirm == 'yes':
        print("Backing up your DB to 'ParagonChat.db.jerrichas'...")
        db.make_backup()
        print("Performing costume replace on 'ParagonChat.db'...")
        db.replace_costume(character_id=character_id, costume_id=costume_id)
        print("DONE! Thanks for using Jerricha's!")
    else:
        print("\n\nNothing was modified in your DB. Thanks for using Jerricha's!")


def main():
    print("### <3 Jerricha's ParagonChat Costume Utility v{} <3 ###".format(VERSION))
    PARAGON_CHAT_DB, COSTUME_FILE = get_from_config('./jerrichas.config')
    test_paths(PARAGON_CHAT_DB, COSTUME_FILE)
    costumesave = Costumesave(COSTUME_FILE)
    db = Database(PARAGON_CHAT_DB)
    # event_loop(db)


if __name__ == '__main__':
    main()
