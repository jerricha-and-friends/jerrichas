#!/usr/bin/env python
import sys
sys.path.insert(0, '.')
VERSION = "0.2.1"
__doc__ = """
##### Jerricha's ParagonChat Costume App v.{} ######
Jerrichas.py will automatically replace a costume in your DB with a
"costumesave" save.
Instructions:
1. Open up jerrichas.ini in your favorite text editor (I've created it in this folder).
    a. Set COSTUME_FILE to your file that you created with "/costumesave
       myfile" in Icon.exe. Usually stored in "City of Heroes\Data" *NOTE*:
       Your costume file is NOT the same as the .costume files that are saved
       from the Character Creator in Icon.exe. Read
       https://github.com/Jerricha/jerrichas/blob/master/docs/guide-to-jerrichas.md
       for more info.
    b. If you have some weird installation of ParagonChat, you can set
       PARAGON_CHAT_DB to your ParagonChat.db location. (usually that's
       %APPDATA%\Paragon Chat\Database\ParagonChat.db") I've already set it
       there, so you usually don't have to change it.
2. BACKUP your ParagonChat.db file! Jerrichas will also *try* to make a backup
   of the DB, but you never know what happens!
3. CLOSE ParagonChat, then run Jerrichas. Follow the on-screen wizard.
4. Please report your errors to me on the forums
   ( http://www.cohtitan.com/forum/index.php?topic=11197.msg189486 )!

For more info, visit: https://github.com/Jerricha/jerrichas/

LEGAL: GPLv3. No warrenties. Use it, share it, hack it, but DO NOT sell it!
Love <3 Jerricha, Summer of 2015
""".format(VERSION)
from io import StringIO
import os

def quit_app(*msgs, exit_code=1):
    [print(i) for i in msgs]
    input("Press Enter to quit...")
    sys.exit(exit_code)

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
COSTUME_FILE = _Replace_Me_
PARAGON_CHAT_DB = %(APPDATA)s\Paragon Chat\Database\ParagonChat.db\n
### For more info and Readme, visit: https://github.com/Jerricha/jerrichas/ ###"""
        f = open("./jerrichas.ini", "w")
        f.write(default_config)
        f.close()
        quit_app(__doc__)

    quit_app(__doc__, "\nYou also forgot to set COSTUME_FILE!") if COSTUME_FILE == "_Replace_Me_" else None
    config = dict(PARAGON_CHAT_DB=PARAGON_CHAT_DB, COSTUME_FILE=COSTUME_FILE)
    return config


def test_path(config):
    for k, v in config.items():
        try:
            assert os.path.exists(v)
        except Exception:
            quit_app(
                "ERROR: {k} path is invalid.\nYou provided:\n\t{v}"
                .format(k=k, v=v))
    return True


class Costumesave(object):
    """
    Represents a file produced with the /costumesave command in Icon.exe
    """
    def __init__(self, path):
        """
        :param path: /costumesave file path
        :type path: str
        """
        self.path = path

    def get_costumeparts(self):
        """
        :returns: a mapping of /costumesave elements to ParagonChatDB 'costumepart' columns
        """
        import csv
        try:
            costume_csv = csv.reader(open(self.path, 'r'))
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
            quit_app("Some kind of error with your costume file.\n{}".format(e))
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
            quit_app("ERROR: Jerrichas terminating\nSomething went wrong with the DB.")

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def _transact_query(self, sql_script):
        """
        Executes CREATE, UPDATE and DELETE queries in a BEGIN and COMMIT block, and performs basic error handling.

        :param sql_script: Generated by a CUD-like method.
        :returns: True if success, False if not.
        """
        transaction = StringIO()
        transaction.write("BEGIN TRANSACTION;")
        transaction.write(sql_script.getvalue())
        transaction.write("COMMIT;")
        try:
            self.session.executescript(sql_script.getvalue())
            self.conn.commit()
            return True
        except Exception as e:
            self.session.execute("ROLLBACK;")
            quit_app(e, "Please report this to Jerricha!")

    def make_backup(self):
        "Backs-up yo shit."
        from shutil import copy
        backup_fp = os.path.join(os.path.split(self.db_path)[0], "ParagonChat.db.jerrichas")
        try:
            copy(self.db_path, backup_fp)
        except IOError:
            quit_app("ERROR: Jerrichas terminating\nUnable to make a backup of your DB.")
        return True

    def get_account_names(self):
        accounts = self.session.execute("SELECT id, name FROM account")
        return accounts.fetchall()

    def get_characters(self, account):
        characters = self.session.execute("SELECT id, name, origin, class, curcostume FROM character WHERE account='{}'".format(account))
        return characters.fetchall()

    def query_replace_parts(self, costumesave, character_id, costume_id):
        """
        Performs the costume replacement query against the ParagonChat db.

        Intended use for "cherry-pick mode".

        :param costumesave: a jerrichas.Costumesave object
        :param chracter_id: Character ID
        :param costume_id: Costume ID

        :returns: A StringIO of an SQLite Script.
        """
        costumeparts = costumesave.get_costumeparts()
        sql_script = StringIO()
        for i in costumeparts:
            sql = """\
DELETE FROM costumepart
    WHERE character='{character_id}'
        AND costume='{costume_id}'
        AND part='{part}';
REPLACE INTO costumepart (geom, tex1, tex2, fx, displayname, region, bodyset, color1, character, costume, part)
    VALUES ('{geom}', '{tex1}', '{tex2}', '{fx}', '{displayname}', '{region}', '{bodyset}', '{color1}', '{character_id}', '{costume_id}', '{part}');"""
            sql = sql.format(
                character_id=character_id,
                costume_id=costume_id,
                **i
            )
            sql_script.write(sql)

        return(sql_script)

    def query_replace_costume(self, costumesave, character_id, costume_id):
        """
        Writes full-costume replacement query against the ParagonChat db.

        Intended use for "batch mode".

        :param costumesave: a jerrichas.Costumesave object
        :param chracter_id: Character ID
        :param costume_id: Costume ID

        :returns: A StringIO of an SQLite Script.
        """
        costumeparts = costumesave.get_costumeparts()
        sql_script = StringIO()
        sql = """\
DELETE FROM costumepart
    WHERE character='{character_id}'
        AND costume='{costume_id}';"""\
        .format(
            character_id=character_id,
            costume_id=costume_id)
        sql_script.write(sql)

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
        return(sql_script)

def event_loop(db, costumesave):
    # Choose Mode
    while True:
        modes = [
            {'id': 1, 'alias': "batch", 'str': "Batch Mode"},
            {'id': 2, 'alias': "cherry-pick", 'str': "Cherry-Pick Mode"},
            {'id': 3, 'alias': "help", 'str': "Help Mode"},
        ]
        modep = lambda id: [m['str'] for m in modes if m['id'] == id][0]
        print("""\
=======**Mode Selection**=======
1: Batch Mode
    Jerricha's will replace an entire costume with the full costumesave file.

2: Cherry-Pick Mode (Advanced)
    You have curated your costumesave file to only include the costume part(s)
    you want. Jerricha's will intelligently replace only those parts that need
    replacing for the costume of your choosing.

3: Help
    Shows the help screen again and exits =)

( Ctrl+C to close me any time )

[Costumesave file]: {costumesave}
""".format(costumesave=costumesave.path))
        try:
            mode = int(input("Select mode [1-3]: "))
            assert mode in [m['id'] for m in modes]
            break
        except:
                print("Invalid input.")
    if mode == 3:
        quit_app(__doc__)

    # Choose Account
    accounts = db.get_account_names()
    if len(accounts) == 1:
        account_id = 1
    else:
        while True:
            print("\n===== Accounts =====")
            [print("{id}: {name}\n".format(**acc)) for acc in accounts]
            try:
                account_id = int(input("Select your account ID [1-{}]: "
                    .format(len(accounts))))
                assert account_id in [acc['id'] for acc in accounts]
                break
            except:
                print("Invalid input.")

    # Choose Character event-loop
    characters = db.get_characters(account_id)
    while True:
        print("\n============ Characters ============")
        for character in characters:
            character['class'] = character['class'].split("Class_")[-1].replace("_", " ")
            print("{id}: {name} - a {origin} {class}".format(**character))
        try:
            character_id = int(input("\n({mode})\nSelect your character ID [1-{total}]: ".format(mode=modep(mode), total=len(characters))))
            assert character_id in [char['id'] for char in characters]
            break
        except:
            print("Invalid input.")

    # Choose Costume event-loop
    character = [char for char in characters if char['id'] == character_id][0]
    while True:
        try:
            costume_id = int(input("\n({mode})\nYou have selected: {name} ({class})\nSelect costume ID to modify [0-9, current: {curcostume}]: ".format(mode=modep(mode), **character)))
            assert costume_id in range(10)
            break
        except:
            print("Invalid input.")

    # Confirm Selection
    confirm = str(input("\n({mode})\nWe're about to alter {name}'s costume #{costume_id} with data from the costumesave file '{COSTUME_FILE}'\nThis change is permanent, and *may* result in a corrupt DB file -- please make sure to backup your DB!\n(Jerricha's will also *try* to backup your DB at ParagonChat.db.jerrichas)\nDo you wish to proceed? (you must type exactly 'y' or 'yes') [ Yes / No ]: "
        .format(mode=modep(mode), COSTUME_FILE=costumesave.path, costume_id=costume_id, name=character['name']))).lower()
    if confirm == 'y' or confirm == 'yes':
        print("Backing up your DB to 'ParagonChat.db.jerrichas'...")
        db.make_backup()
        print("({})".format(modep(mode)))
        if mode == 1:
            print("\nPerforming full costume replace...")
            query = db.query_replace_costume(costumesave=costumesave, character_id=character_id, costume_id=costume_id)
            db._transact_query(query)
        elif mode == 2:
            print("\nPerforming cherry-pick costume part replace...")
            query = db.query_replace_parts(costumesave=costumesave, character_id=character_id, costume_id=costume_id)
            db._transact_query(query)
        quit_app("DONE! Thanks for using Jerricha's!", exit_code=0)
    else:
        quit_app("\n\nNothing was modified in your DB. Thanks for using Jerricha's!", exit_code=0)

def main():
    print("### <3 Jerricha's ParagonChat DB Costume Utility v{} <3 ###".format(VERSION))
    config = get_from_config('./jerrichas.ini')
    test_path(config)
    costumesave = Costumesave(config['COSTUME_FILE'])
    db = Database(config['PARAGON_CHAT_DB'])
    event_loop(db=db, costumesave=costumesave)


if __name__ == '__main__':
    main()
