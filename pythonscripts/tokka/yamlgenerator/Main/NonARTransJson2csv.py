import json
import pprint
import csv
import codecs
from itertools import zip_longest

final_json = {}

with open("final.json","r") as file_read:
    data = json.load(file_read)
    print(type(data))

def innerDict(v):
    for a,b in v.items():
        if isinstance(b, dict):
            innerDict(b)
        elif a not in final_json.keys():
            final_json[a] = []
        elif isinstance(b, str):
            final_json[a].append(b)

def breakList(data):
    if isinstance(data,list):
        for d in data:
            if isinstance(d,dict):
                for k,v in d.items():
                    if isinstance(v, list):
                        breakList(v)
                    elif isinstance(v, dict):
                        innerDict(v)
                    elif k not in final_json.keys():
                        final_json[k] = []
                    elif isinstance(v, str):
                        final_json[k].append(v)

breakList(data)
pprint.pprint(final_json)

lst_key_final = []
lst_value_final = []
for k,v in final_json.items():
    lst_key_final.append(k)
    lst_value_final.append(v)

#print(lst_value_final)
export_data = zip_longest(*lst_value_final, fillvalue = '')
with codecs.open("NonARFinal.csv", "w", encoding="ISO-8859-1") as f:
    dict_writer = csv.writer(f)
    dict_writer.writerow(lst_key_final)
    dict_writer.writerows(export_data)