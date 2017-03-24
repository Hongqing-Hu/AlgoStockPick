#coding: utf-8
import tushare as ts
import json
import io,os




def from_json(fname="symbol.json"):
    symbol = {}
    if (os.path.exists(fname)):
        with open(fname) as json_file:
            symbol = json.load(json_file)
    return symbol


def to_json(symbol, fname="symbol.json"):
    # Write JSON file
    with open(fname, 'w', encoding='utf8') as outfile:
        outfile.write(json.dumps(symbol))
    


symbol = {}

try:
    symbol = from_json()
except:
    pass
    

try:
    i = 0
    for stockClass in [600,601,603, 0,2,300]:
        for stockID in range(0,999):
            id = "%06d" % (stockClass * 1000 + stockID)
            if id not in symbol:
                i= i + 1
                try :            
                    ts.get_k_data(id)
                    symbol[id] = 1
                    print("write %s" % (id) )
                except IndexError as err:
                    symbol[id] = None
                    print("%s doesn't exist" % id )
            if (i == 50): # save to database every 50 symbol
                i = 0
                print("write into files")
                to_json(symbol)
except: 
    to_json(symbol)

to_json(symbol)

