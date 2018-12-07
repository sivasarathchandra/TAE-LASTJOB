import pymysql
import unittest
import requests
import os
from decimal import *
from Tests.config_API import configAPI
from Tests.logging_API import loggingAPI

API_INPUT={}
# WORKSPACE = os.environ['WORKSPACE']

""" TestAgeCategories class tests all the cases for age categories api"""
class TestTargetsPut(unittest.TestCase):

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.set_up_list = configAPI.configlist
        self.GET_URL = self.set_up_list[0]
        self.oAuth = self.Auth()
        self.params = {'client_id': self.set_up_list[1]}
        self.header = {'Authorization': self.oAuth, 'Content-Type':'application/json'}
        self.db = pymysql.connect(self.set_up_list[2], self.set_up_list[3], self.set_up_list[4],self.set_up_list[5])
        self.cursor = self.db.cursor()

    """Auth function is used to get the oAuth value. As of now using auth-header-1.3.jar which will be replaced oAuth generator"""
    def Auth(self):
        oAuth=""
        os.system("java -jar tests\\auth-header-1.3.jar -k c0c11d7a-48c1-461d-8be9-56e9fb60b28f -s Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l > oAuthKey.txt")
        with open("oAuthKey.txt","r") as oAuthFile:
            for line in oAuthFile:
                cleanedLine = line.strip()
                if cleanedLine:  # is not empty
                    #print("Recieved the token")
                    oAuth = cleanedLine
        loggingAPI.logger.info("returning oAuth Value")
        return oAuth

    """test_putRequest_IDExists_validParams function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are valid"""
    def test_Step1_putRequest(self):
        key_list = ['client_id','metric_key','targets']
        self.data1 = {"targets": "[{\"facility_id\": \"test\", \"target\": 1251, \"top_zone\": 6000, \"bottom_zone\": 2000}]", "client_id": "test", "metric_key": "test"}
        print("I am here")
        print(self.data1)
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.selectQuery = "select * from targets where client_id"+" "+"="+" "+"'"+"test"+"'"
        self.cursor.execute(self.selectQuery)
        self.data = set(self.cursor.fetchall())
        self.col_names = [i[0] for i in self.cursor.description]
        self.DB_Output = {self.col_names[0]: [self.x[0] for self.x in self.data],
                          self.col_names[1]: [self.x[1] for self.x in self.data],
                          self.col_names[2]: [self.x[2] for self.x in self.data],
                          self.col_names[3]: [self.x[3] for self.x in self.data],
                          self.col_names[4]: [self.x[4] for self.x in self.data],
                          self.col_names[5]: [self.x[5] for self.x in self.data],
                          self.col_names[6]: [self.x[6] for self.x in self.data]}
        API_INPUT = self.data1
        for key_api,value_api in API_INPUT.items():
            if key_api in key_list:
                if key_api == 'targets':
                    list_value = API_INPUT[key_api]
                    final_value = list_value.replace('[{','').replace('}]','').replace(', ',',').replace('"','').replace(': ',':')
                    final_value = final_value.split(',')
                    for iters in final_value:
                        keyandvalue = iters.split(':')
                        DB_output = self.DB_Output[keyandvalue[0]]
                        if isinstance(DB_output[0],Decimal):
                            keyandvalue[1] = Decimal(keyandvalue[1]).quantize(Decimal('1.0000'))
                        self.assertEqual(DB_output[0],keyandvalue[1])
                else:
                    value = self.DB_Output[key_api]
                    self.assertEqual(value[0],API_INPUT[key_api])
        loggingAPI.logger.info(API_INPUT)
        loggingAPI.logger.info(self.DB_Output)
        #self.assertEqual(self.DB_Output, API_input)

    """test_putRequest_IDExists_invalidParams_error function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are invalid"""
    def test_Step2_putRequest_error(self):
        self.data = {"targets": "[{\"facility_id\": \"test\", \"target\": 1251, \"top_zone\": 6000, \"bottom_zone\": 2000}]", "client_id": "", "metric_key": ""}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """Delete the test data that is created"""
    def tearDown(self):
        self.query = "DELETE from targets WHERE client_id = "+"'"+"test"+"'"+";"
        value = self.cursor.execute(self.query)
        self.db.commit()
        self.db.close()
        loggingAPI.logger.info("Removed the test data that is created.")