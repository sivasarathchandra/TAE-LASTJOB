#!/usr/bin/python3
import pymysql
import unittest
import requests
import os
import xmlrunner
from tests.configAPI import configAPI
from tests.loggingAPI import loggingAPI
from tests.oAuthGenerator import oAuthGenerator

configlist =[]

""" TestAgeCategories class tests all the cases for age categories api"""
class TestAgeCategories(unittest.TestCase):

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.configlist = configAPI.configlist
        self.GET_URL = self.configlist[0]
        self.base_url = self.configlist[1]
        self.oAuth = oAuthGenerator.Auth(self,self.configlist[7],self.configlist[8],self.configlist[9],self.configlist[10])
        self.parms = {'client_id': self.configlist[2]}
        self.header = {'Authorization': self.oAuth, 'Content-Type': 'application/json'}
        print(self.configlist[3], self.configlist[4], self.configlist[5], self.configlist[6])
        self.db = pymysql.connect(self.configlist[3], self.configlist[4], self.configlist[5], self.configlist[6])
        print(self.db)
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
        self.GET_URL_1 = self.base_url+'/age_categorie'
        self.res = requests.get(self.GET_URL_1, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_Conflicts function is used to check the API Conflicts 409 response"""
    def test_step_4_Conflicts(self):
        self.GET_URL2 = self.base_url+'/config_items'
        self.res = requests.post(self.GET_URL2, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """test_rest_api_badRequest function is used to check the API badrequest 400 response"""
    def test_step_5_badRequest(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, data=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '400')

    """test_rest_api_noContent function is used to check the API NoContent 204 response"""
    def test_step_6_noContent(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')

    """test_rest_api_invalidRecord function is used to check the API InValidRecord 404 response"""
    def test_step_7_invalidRecord(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.post(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_getRequest function is used to check the API GET Request"""
    def test_step_1_getRequest(self):
        self.API_Output = {}
        self.res = requests.get(self.GET_URL, headers=self.header)
        self.key_list = ['age_category', 'begin_age', 'end_age', 'sort_order']
        for self.iteration in self.res.json():
            for self.keys_res, self.values_res in self.iteration.items():
                if self.keys_res in self.key_list:
                    self.API_Output.setdefault(self.keys_res, []).append(self.values_res)
        loggingAPI.logger.info("API Output: %s" % self.API_Output)
        # SQL DB Connection and fetching and disconnection as well
        self.query1 = "SELECT age_category,begin_age,end_age,sort_order FROM age_categories WHERE client_id=" + "'" + \
                      self.configlist[2] + "'"
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
        loggingAPI.logger.info("Validated")

"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
