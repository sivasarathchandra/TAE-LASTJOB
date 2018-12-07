import requests
import pymysql
import json
import os

tempdict = {}

def rest_api_error():
    oAuth = '2'
    header = {'Authorization': oAuth}
    session = requests.Session()
    res = requests.get(GET_URL, headers=header)
    print(res)

def rest_api_NotFound():
    GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categorie'
    header = {'Authorization': oAuth}
    res1 = requests.get(GET_URL_1, headers=header)
    print(res1)

def rest_api_Conflicts():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/config_items'
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    res1 = requests.post(GET_URL, headers=header)
    print(res1)

def rest_api_badRequest():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories'
    data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL, headers=header, data=data1)
    print(res)

def rest_api_noContent():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories'
    data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL, headers=header,json=data1)
    print(res)

def rest_api_invalidRecord():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories?'
    data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
    header = {'Authorization': oAuth}
    session = requests.Session()
    res = requests.post(GET_URL, headers=header,json=data1)
    print(res)

def rest_api_putRequest():
    GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories'
    data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL, headers=header, json=data1)
    print(res)

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


GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categories?client_id="50187c3d-b72c-4f7a-9a34-b2abe35be868"'
oAuth = Auth()
header = {'Authorization' : oAuth}
session = requests.Session()
res = requests.get(GET_URL, headers=header)
for i in res.json():
    for k,v in i.items():
        if k == 'age_category':
            tempdict.setdefault(k,[]).append(v)
        elif k == 'begin_age':
            tempdict.setdefault(k, []).append(v)
        elif k == 'end_age':
            tempdict.setdefault(k, []).append(v)
        elif k == 'sort_order':
            tempdict.setdefault(k, []).append(v)
# SQL DB Connection and fetching and disconnection as well
db = pymysql.connect("database.devhealtheintent.net","rc_config_svc","rc_config_svc","rcanalytics_config_service" )
cursor = db.cursor()
cursor.execute("DELETE FROM age_categories WHERE 'client_id' = 'DEFAULT'")
cursor.execute("SELECT age_category,begin_age,end_age,sort_order FROM age_categories WHERE client_id='50187c3d-b72c-4f7a-9a34-b2abe35be868'")
data = set(cursor.fetchall())
col_names = [i[0] for i in cursor.description]
some_dict = {col_names[0] : [x[0] for x in data ],
             col_names[1] : [x[1] for x in data],
             col_names[2]: [x[2] for x in data],
             col_names[3]: [x[3] for x in data],}
db.close()

# validation of the data from DB with the api
for k,v in tempdict.items():
    if k == 'age_category':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of" + k + "is matching")
        else:
            print("the values of" + k + "are not matching")
    elif k == 'begin_age':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of" + k + "is matching")
        else:
            print("the values of" + k + "are not matching")
    elif k == 'end_age':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of" + k + "is matching")
        else:
            print("the values of" + k + "are not matching")
    elif k == 'sort_order':
        l1 = tempdict[k]
        l2 = some_dict[k]
        if set(l2).issuperset(set(l1)):
            print("the values of" + k + "is matching")
        else:
            print("the values of" + k + "are not matching")

print("================Now checking for mutiple http errors==============")
# checking for api errors
rest_api_error()
rest_api_NotFound()
rest_api_Conflicts()
rest_api_badRequest()
rest_api_noContent()
rest_api_invalidRecord()
print("================Now checking for put request======================")
rest_api_putRequest()