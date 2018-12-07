#!/usr/local/bin/python3
import pymysql
import unittest
import requests
import os
import xmlrunner
from tests.configAPI import configAPI
from tests.loggingAPI import loggingAPI
from tests.oAuthGenerator import oAuthGenerator

configlist = []

class TestOrganizationMaps(unittest.TestCase):
    
    """The setUp method initializes the variables and values that are used across the test cases"""
    def setUp(self):
        self.configlist = configAPI.configlist
        self.GET_URL = self.configlist[0]
        self.base_url = self.configlist[1]
        self.oAuth = oAuthGenerator.Auth(self,self.configlist[8],self.configlist[9],self.configlist[10],self.configlist[11])
        self.header = {'Authorization': self.oAuth, 'Content-Type': 'application/json'}
        self.parms = {'client_id': self.configlist[2], 'millennium_org_id': self.configlist[3]}
        self.db = pymysql.connect(self.configlist[4], self.configlist[5], self.configlist[6], self.configlist[7])
        self.cursor = self.db.cursor()

    """test_rest_api_error function is used to check the unauthorized verification of API 401 response"""
    def test_step_2_unauthorized(self):
        oAuth = '2'
        header1 = {'Authorization': oAuth}
        session = requests.Session()
        self.res = requests.get(self.GET_URL, headers=header1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '401')

    """test_rest_api_NotFound function is used to check the API NotFound 404 response"""
    def test_step_3_NotFound(self):
        self.GET_URL_1 = self.base_url+'/organization_map'
        self.res = requests.get(self.GET_URL_1, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong client_id 404 response"""
    def test_step_5_NotFound_client_Id(self):
        self.param1 = {'client_id': '2'}
        self.res = requests.get(self.GET_URL, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Millennium_ID 404 response"""
    def test_step_6_NotFound_Millennium_Id(self):
        self.param1 = {'millennium_org_id': '2'}
        self.res = requests.get(self.GET_URL, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Healthe_intent_org_id 404 response"""
    def test_step_7_NotFound_healthe_intent_org_id(self):
        self.param1 = {'healthe_intent_org_id': '2'}
        self.res = requests.get(self.GET_URL, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Healthe_intent_org 404 response"""
    def test_step_8_NotFound_healthe_intent_org(self):
        self.param1 = {'healthe_intent_org': '2'}
        self.res = requests.get(self.GET_URL, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_badRequest function is used to check the API badrequest 400 response"""
    def test_step_4_badRequest(self):
        GET_URL = self.base_url+'/organization_maps/1'
        data1 = {'millennium_org_id': 'test', 'client_id': 'test', 'healthe_intent_org_id': 'test',
                 'healthe_intent_org_name': 'test'}
        self.res = requests.put(GET_URL, headers=self.header, data=data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '400')

    """test_rest_api_getRequest function is used to check the API GET Request"""
    def test_step_1_getRequest(self):
        self.API_Output = {}
        self.res = requests.get(self.GET_URL, headers=self.header, params=self.parms)
        self.key_list = ['id', 'millennium_org_id', 'healthe_intent_org_id', 'healthe_intent_org_name']
        for self.iteration in self.res.json():
            for self.keys_res, self.values_res in self.iteration.items():
                if self.keys_res in self.key_list:
                    self.API_Output.setdefault(self.keys_res, []).append(self.values_res)
        loggingAPI.logger.info("The o/p from API is here")
        loggingAPI.logger.info(self.API_Output)
        # SQL DB Connection and fetching and disconnection as well
        self.query1 = "SELECT id,millennium_org_id, healthe_intent_org_id, healthe_intent_org_name FROM organization_maps WHERE client_id =" + "'" + \
                      self.configlist[2] + "'" + " and millennium_org_id =" + "'" + self.configlist[3] + "'"
        self.cursor.execute(self.query1)
        self.data = set(self.cursor.fetchall())
        self.col_names = [i[0] for i in self.cursor.description]
        self.DB_Output = {self.col_names[0]: [self.x[0] for self.x in self.data],
                          self.col_names[1]: [self.x[1] for self.x in self.data],
                          self.col_names[2]: [self.x[2] for self.x in self.data],
                          self.col_names[3]: [self.x[3] for self.x in self.data], }
        loggingAPI.logger.info("DataBase Output")
        loggingAPI.logger.info(self.DB_Output)
        self.db.close()
        loggingAPI.logger.info("Validating the response")
        # validation of the data from DB with the api
        for self.keys_val, self.value_val in self.API_Output.items():
            if self.keys_res in self.key_list:
                self.assert_list1 = self.API_Output[self.keys_res]
                self.assert_list2 = self.DB_Output[self.keys_res]
                self.assertEqual(set(self.assert_list2).issuperset(set(self.assert_list1)), True)
        loggingAPI.logger.info("validated")


"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
