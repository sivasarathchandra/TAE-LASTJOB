import json
import pprint
import codecs
import csv
from itertools import zip_longest

final_json = {}
with open('denial.json', 'r') as readfile:
    read_json = {}
    read_json = json.load(readfile)

def inner_dictitems(temp, dictionary):
    for i, v1 in dictionary.items():
        print(temp + "." + i)
        temp1 = temp + "." + i
        #print("the value of temp1 is", temp1)
        if isinstance(v1, dict):
            inner_dictitems(temp1, v1)
        elif isinstance(v1, list):
            inner_dic_pathA(temp1, v1)
        elif temp1 not in final_json.keys():
                final_json[temp1] = []
        elif isinstance(v1, str):
            final_json[temp1].append(v1)

def inner_dic_pathA(path, lst):
    for v in lst:
        if isinstance(v, dict):
            for i, v1 in v.items():
                print(path + "." + i)
                temp = path + "." + i
                #print("the value of temp is :", temp)
                if isinstance(v1, dict):
                    inner_dictitems(temp, v1)
                if isinstance(v1, list):
                    inner_dic_pathA(temp, v1)
                elif temp not in final_json.keys():
                    final_json[temp] = []
                elif isinstance(v1, str):
                    final_json[temp].append(v1)
        else:
            l = path + "." + k + "."
            print("the value of l is", l)
            print(path , "=>", v)

def dict_pathR(path, read_json):
    for k, v in read_json.items():
        if k == "recordId" and isinstance(v, dict):
            for i, v1 in enumerate(v):
                temp12 = path + k + "."+v1
                print(temp12)
                if temp12 not in final_json.keys():
                    final_json[temp12] = []
                elif isinstance(v1, str):
                    final_json[temp12].append(v1)
            else:
                print(path + k + ".",v)

def dict_pathA(path, read_json):
    for k, v in read_json.items():
        if k != "recordId":
            inner_dic_pathA(k, v)

dict_pathR("", read_json)
dict_pathA("", read_json)
#pprint.pprint(final_json)

with open("final_json2csv.json",'w')as final_json_file:
    json.dump(final_json,final_json_file)
    final_json_file.close()

lst_key_final = []
lst_value_final = []
for k,v in final_json.items():
    lst_key_final.append(k)
    lst_value_final.append(v)

#print(lst_value_final)
export_data = zip_longest(*lst_value_final, fillvalue = '')
with codecs.open("Final.csv", "w", encoding="ISO-8859-1") as f:
    dict_writer = csv.writer(f)
    dict_writer.writerow(lst_key_final)
    dict_writer.writerows(export_data)