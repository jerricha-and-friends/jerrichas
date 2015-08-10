def main():
    import os
    # Batch mode
    # PARAGON_CHAT_DB = os.path.join(os.getenv("APPDATA"), "Paragon Chat\Database\ParagonChat.db")
    PARAGON_CHAT_DB = "testing\data\ParagonChat.db"
    db = Database(PARAGON_CHAT_DB)
    COSTUME_FILE = "testing\data\mock_costume_female"
    costumesave = Costumesave(COSTUME_FILE)
    sql_script = db.query_replace_costume(costumesave, 3, 0)
    db._transact_query(sql_script)

    # Cherry-pick mode
    import os
    PARAGON_CHAT_DB = "testing\data\ParagonChat.db"
    # PARAGON_CHAT_DB = os.path.join(os.getenv("APPDATA"), "Paragon Chat\Database\ParagonChat.db")
    db = Database(PARAGON_CHAT_DB)
    COSTUME_FILE = "testing\data\mock_part_mom_trenchcoat"
    costumesave = Costumesave(COSTUME_FILE)
    sql_script = db.query_replace_parts(costumesave, 1, 0)
    # print(sql_script.getvalue())
    db._transact_query(sql_script)

if __name__ == '__main__':
    main()
