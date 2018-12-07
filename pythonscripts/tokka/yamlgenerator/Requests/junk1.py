import requests
import pymysql
import json
import os




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

def rest_api_putRequest():
    GET_URL1 = 'http://10.182.97.227:3001/organization_maps/1'
    oAuth = Auth()
    data = {'millennium_org_id':'test', 'client_id':'test', 'healthe_intent_org_id':'test','healthe_intent_org_name':'test'}
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.put(GET_URL1, headers=header,json=data)
    print(res.text)

def rest_api_putRequestT():
    GET_URL1 = 'http://10.182.97.54:3001/targets?client_id=50187c3d-b72c-4f7a-9a34-b2abe35be868'
    oAuth = Auth()
    data = "{\"client_id\":\"50187c3d-b72c-4f7a-9a34-b2abe35be868\",\"metric_key\":\"pos_days\",\"targets\":{\"facility_id\":\"0a10c7dc-eab2-486b-bb05-199eceb6916a\",\"top_zone\":6000,\"bottom_zone\":4000}}"
    header = {'Authorization': oAuth, 'Content-Type': 'application/json'}
    session = requests.Session()
    res = requests.get(GET_URL1, headers=header, json=data)
    print(res.text)


rest_api_putRequestT()
#GET_URL = 'http://10.182.97.227:3001/targets?client_id=50187c3d-b72c-4f7a-9a34-b2abe35be868'
#oAuth = Auth()
#header = {'Authorization' : oAuth}
#rest_api_putRequest()
#session = requests.Session()
#res = requests.get(GET_URL, headers=header)
#sprint(res.text)
