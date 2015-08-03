db = Database()
db.get_characters(1)

try:
    pass
except Exception, e:
    raise e

 cf = csv.reader(open('./tests/cooltrench_w_boots', "r"))