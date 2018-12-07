import requests
import pymysql
import json
import os
import pprint

tempdict = {}

def rest_api_error():
    oAuth = '2'
    header = {'Authorization': oAuth}
    session = requests.Session()
    res = requests.get(GET_URL, headers=header)
    print(res)

def rest_api_NotFound():
    header = {'Authorization': oAuth}
    res1 = requests.get(GET_URL, headers=header)
    print(res1)

def rest_api_Conflicts():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/config_items'
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    res1 = requests.post(GET_URL, headers=header)
    print(res1)

def rest_api_badRequest():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps/1'
    data1 = {'millennium_org_id':'test', 'client_id':'test', 'healthe_intent_org_id':'test','healthe_intent_org_name':'test'}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL, headers=header, data=data1)
    print(res)

def rest_api_putRequest():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps/1'
    data = {'millennium_org_id': 'test', 'client_id': 'test', 'healthe_intent_org_id': 'test', 'healthe_intent_org_name': 'test'}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL, headers=header, json=data)
    print(res)
    print("================Now checking the data that is pushed in DB===============")
    db = pymysql.connect("database.devhealtheintent.net", "rc_config_svc", "rc_config_svc","rcanalytics_config_service")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM organization_maps WHERE client_id = 'test'")
    data = set(cursor.fetchall())
    col_names = [i[0] for i in cursor.description]
    some_dict = {col_names[0]: [x[0] for x in data],
                 col_names[1]: [x[1] for x in data],
                 col_names[2]: [x[2] for x in data],
                 col_names[3]: [x[3] for x in data], }
    db.close()
    print(some_dict)

def Auth():
    os.chdir("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//Requests//")
    oauth1 = os.system("java -jar auth-header-1.3.jar -k c0c11d7a-48c1-461d-8be9-56e9fb60b28f -s Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l > oAuthKey.txt")
    with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//Requests//oAuthKey.txt","r") as oAuthFile:
        for line in oAuthFile:
            cleanedLine = line.strip()
            if cleanedLine:  # is not empty
                print("Recieved the token")
        oAuth = cleanedLine
    return oAuth


GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps'
oAuth = Auth()
header = {'Authorization' : oAuth,'Content-Type' : 'application/json'}
parms = {'client_id' : '50187c3d-b72c-4f7a-9a34-b2abe35be868'}
session = requests.Session()
res = requests.get(GET_URL, headers=header,params=parms)
for i in res.json():
    for k,v in i.items():
        if k == 'id':
            tempdict.setdefault(k,[]).append(v)
        elif k == 'millennium_org_id':
            tempdict.setdefault(k, []).append(v)
        elif k == 'healthe_intent_org_id':
            tempdict.setdefault(k, []).append(v)
        elif k == 'healthe_intent_org_name':
            tempdict.setdefault(k, []).append(v)
        elif k == 'created_atcreated_at':
            tempdict.setdefault(k, []).append(v)
        elif k == 'updated_at':
            tempdict.setdefault(k, []).append(v)
#print(tempdict)
#SQL DB Connection and fetching and disconnection as well
db = pymysql.connect("database.devhealtheintent.net","rc_config_svc","rc_config_svc","rcanalytics_config_service" )
cursor = db.cursor()
cursor.execute("SELECT id,millennium_org_id, healthe_intent_org_id, healthe_intent_org_name FROM organization_maps WHERE client_id = '50187c3d-b72c-4f7a-9a34-b2abe35be868'")
data = set(cursor.fetchall())
col_names = [i[0] for i in cursor.description]
some_dict = {col_names[0] : [x[0] for x in data ],
             col_names[1] : [x[1] for x in data],
             col_names[2]: [x[2] for x in data],
             col_names[3]: [x[3] for x in data],}
db.close()

# validation of the data from DB with the api
for k,v in tempdict.items():
    if k == 'id':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of "+ k +" are matching")
    elif k == 'millennium_org_id':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of " + k + " are matching")
    elif k == 'healthe_intent_org_id':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of " + k + " are matching")
    elif k == 'healthe_intent_org_name':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of " + k + " are matching")

print("================Now checking for mutiple http errors==============")
# checking for api errors
rest_api_error()
rest_api_NotFound()
rest_api_Conflicts()
rest_api_badRequest()
print("================Now checking for put request======================")
rest_api_putRequest()
