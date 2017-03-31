#coding: utf-8
import tushare as ts
import json
import io,os
import sqlite3


def from_json(fname="symbol.json"):
    symbol = {}
    if (os.path.exists(fname)):
        with open(fname) as json_file:
            symbol = json.load(json_file)
    return symbol


symbol = {}

try:
    symbol = from_json()
except:
    pass


conn = sqlite3.connect('db/stock.sqlite')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS StockInfo  (id TEXT PRIMARY KEY NOT NULL UNIQUE, name TEXT DEFAULT NULL)''')

for key in symbol:
    if symbol[key]:
        c.execute("INSERT INTO StockInfo (id, name)  VALUES ('%s','%s')" % (key, symbol[key]) )
    else:
        c.execute("INSERT INTO StockInfo (id, name)  VALUES ('%s',NULL)" % (key) )
    print("insert %s of company %s into database " % (key, key))
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

