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

"""TestOrganizationMaps class tests all the cases for Syndications api"""
class TestSyndication(unittest.TestCase):

    """The setUp method initializes the variables and values that are used across the test cases"""
    def setUp(self):
        self.configlist = configAPI.configlist
        self.GET_URL = self.configlist[0]
        self.base_url = self.configlist[1]
        self.oAuth = oAuthGenerator.Auth(self,self.configlist[7],self.configlist[8],self.configlist[9],self.configlist[10])
        self.param = {'client_id':self.configlist[2]}
        self.header = {'Authorization': self.oAuth, 'Content-Type':'application/json'}
        self.db = pymysql.connect(self.configlist[3], self.configlist[4], self.configlist[5],self.configlist[6])
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
        self.GET_URL_1 = self.base_url+'/syndication_field'
        self.res = requests.get(self.GET_URL_1, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an invalid client_id 404 response"""
    def test_step_5_InvalidClient_ID(self):
        param1 = {'client_id': '1'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an invalid table_name 404 response"""
    def test_step_6_Invalidtable_name(self):
        param1 = {'client_id': self.configlist[2],'table_name':'Cerner'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an null client_id 404 response"""
    def test_step_7_nullClient_ID(self):
        param1 = {'client_id': 'null'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an null table_name 404 response"""
    def test_step_8_nulltable_name(self):
        param1 = {'client_id': self.configlist[2],'table_name':'null'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an missing client_id 404 response"""
    def test_step_9_missingClient_ID(self):
        param1 = {'table_name': 'RC_F_DAILY_ENCOUNTER'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an missing table_name 404 response"""
    def test_step_10_missingtable_name(self):
        param1 = {'client_id': self.configlist[2]}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an invalid field_name 404 response"""
    def test_step_11_invalidfield_name(self):
        param1 = {'client_id': self.configlist[2],'table_name': 'RC_F_DAILY_ENCOUNTER','field_name':'Cerner'}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the API for an invalid order_number 404 response"""
    def test_step_12_invalidorder_number(self):
        param1 = {'client_id': self.configlist[2],'table_name': 'RC_F_DAILY_ENCOUNTER','order_number':100}
        self.res = requests.get(self.GET_URL, headers=self.header,params=param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_badRequest function is used to check the API badrequest 400 response"""
    def test_step_4_badRequest(self):
        data1 = {'client_id':'test'}
        self.res = requests.put(self.GET_URL, headers=self.header, json=data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_getRequest function is used to check the API GET Request"""
    def test_step_1_getRequest(self):
        self.table_keys = []
        self.cursor.execute("SELECT DISTINCT table_name FROM syndication_fields")
        self.data = list(self.cursor.fetchall())
        self.key_list=['id','client_id','table_name','field_name','order_number']
        for self.iter in self.data:
            self.table_keys.append(self.iter[0])
        for self.individaul_key in self.table_keys:
            self.parms = {'client_id': self.configlist[2],'table_name':self.individaul_key}
            self.API_Output = {}
            self.res = requests.get(self.GET_URL, headers=self.header, params=self.parms)
            for self.iteration in self.res.json():
                for self.keys_res, self.values_res in self.iteration.items():
                    if self.keys_res in self.key_list:
                        self.API_Output.setdefault(self.keys_res, []).append(self.values_res)
            loggingAPI.logger.info("the json returned for each table name:")
            loggingAPI.logger.info(self.API_Output)
            self.query1 = "SELECT * FROM syndication_fields WHERE client_id ="+"'"+self.configlist[2]+"'"+" and table_name="+"'"+self.individaul_key+"'"
            self.cursor.execute(self.query1)
            self.data = set(self.cursor.fetchall())
            self.col_names = [i[0] for i in self.cursor.description]
            self.DB_Output = {self.col_names[0]: [self.x[0] for self.x in self.data],
                              self.col_names[1]: [self.x[1] for self.x in self.data],
                              self.col_names[2]: [self.x[2] for self.x in self.data],
                              self.col_names[3]: [self.x[3] for self.x in self.data],
                              self.col_names[4]: [self.x[4] for self.x in self.data],
                              self.col_names[5]: [self.x[5] for self.x in self.data],
                              self.col_names[6]: [self.x[6] for self.x in self.data], }
            loggingAPI.logger.info("The o/p from Data base is here")
            loggingAPI.logger.info(self.DB_Output)
            loggingAPI.logger.info("Validating the response")
            # validation of the data from DB with the api
            for self.keys_val, self.value_val in self.API_Output.items():
                if self.keys_val in self.key_list:
                    self.assert_list1 = self.API_Output[self.keys_val]
                    self.assert_list2 = self.DB_Output[self.keys_val]
                    self.assertEqual(set(self.assert_list2).issuperset(set(self.assert_list1)), True)
            loggingAPI.logger.info("validated")

"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
