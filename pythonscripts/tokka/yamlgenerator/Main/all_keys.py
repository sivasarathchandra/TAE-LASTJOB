import json
import pprint


final_json = {}
with open('Account_23681835.json', 'r') as readfile:
    #	print(readfile)
    read_json = {}
    read_json = json.load(readfile)
# print(read_json)

'''def adding_KeyAtLocation(temp):
    lenght = len(temp)
    for i, v in enumerate(temp):
        print(v)
        if i == 0:
            k = v
        elif i == 1:
            k1 = '[' + v + ']'
            temp = k + k1
        else:
            last = temp
            final_key = last + '[' + v + ']'
            temp = final_key
    return (final_key)
'''
def inner_dictitems(temp, dictionary):
    for i, v1 in dictionary.items():
        print(temp + "." + i)
        temp1 = temp + "." + i
        if isinstance(v1, dict):
            inner_dictitems(temp1, v1)
        elif isinstance(v1, list):
            inner_dic_pathA(temp1, v1)


def inner_dic_pathA(path, lst):
    for v in lst:
        if isinstance(v, dict):
            for i, v1 in v.items():
                print(path + "." + i)
                temp = path + "." + i
                print("the value of temp is :", temp)
                if isinstance(v1, dict):
                    inner_dictitems(temp, v1)
                if isinstance(v1, list):
                    inner_dic_pathA(temp, v1)
        else:
            l = path + "." + k + "."
            print("the value of l is", l)
            print(path + "." + k + ".", "=>", v)


def dict_pathR(path, read_json):
    for k, v in read_json.items():
        if k == "recordId":
            print(k)
            if isinstance(v, dict):
                for i, v1 in enumerate(v):
                    print(path + k + ".", v1)
            else:
                print(path + k + ".", v)


def dict_pathA(path, read_json):
    for k, v in read_json.items():
        if k != "recordId":
            inner_dic_pathA(k, v)


'''def inner_dic_pathT(path, lst):
    for v in lst:
        if isinstance(v, dict):
            for i, v1 in v.items():
                print(path + "." + i)
                temp = path + "." + i
                if isinstance(v1, dict):
                    inner_dictitems(temp, v1)
                if isinstance(v1, list):
                    inner_dic_pathT(temp, v1)
        else:
            print(path + "." + k + ".", "=>", v)


def dict_pathT(path, read_json):
    for k, v in read_json.items():
        if k == "transactions":
            inner_dic_pathT(k, v)
            break
'''

#Key_Iter = input("Enter Key from the above list ")
#if Key_Iter == "recordId":
print("entering if")
dict_pathR("", read_json)
'''    Key_Iter1 = input("Enter the string under which the new keys are going: ")
    New_Key = input("New Key: ")
    New_Value = input("New Value: ")
    newKeyCreation(Key_Iter1, New_Key, New_Value, read_json)'''
#elif Key_Iter == "accounts":
print("entering if")
dict_pathA("", read_json)
'''    Key_Iter1 = input("Enter the string under which the new keys are going: ")
    New_Key = input("New Key: ")
    New_Value = input("New Value: ")
    newKeyCreation(Key_Iter1, New_Key, New_Value, read_json)'''
#elif Key_Iter == "transactions":
print("entering if")
#dict_pathT("", read_json)
'''Key_Iter1 = input("Enter the string under which the new keys are going: ")
New_Key = input("New Key: ")
New_Value = input("New Value: ")
newKeyCreation(Key_Iter1, New_Key, New_Value, read_json)'''
