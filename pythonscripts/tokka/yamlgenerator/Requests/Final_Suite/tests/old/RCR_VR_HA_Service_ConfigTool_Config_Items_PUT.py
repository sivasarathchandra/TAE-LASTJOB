import pymysql
import unittest
import requests
import os
from Tests.config_API import configAPI
from Tests.logging_API import loggingAPI
from Tests.oAuthGenerator import oAuthGenerator

#WORKSPACE = os.environ['WORKSPACE']

""" TestAgeCategories class tests all the cases for age categories api"""
class TestSuiteConfigItemsPut(unittest.TestCase):

    """This method is for getting the initial ID"""
    def compare_against_DB(self,client_name,counter):
        loggingAPI.logger.info("the value that is sent in this function is :" +client_name)
        if counter == 1:
            sel_query = "SELECT id FROM RCANALYTICS_CONFIG_SERVICE.CONFIG_ITEMS WHERE CLIENT_ID = " + "'" + client_name + "';"
            self.cursor.execute(sel_query)
            sel_results = list(self.cursor.fetchall())
            results = sel_results[0]
            self.res_list = results[0]
            return self.res_list
        else:
            sel_query = "SELECT * FROM RCANALYTICS_CONFIG_SERVICE.CONFIG_ITEMS WHERE CLIENT_ID = " + "'" + client_name + "';"
            self.cursor.execute(sel_query)
            sel_results = list(self.cursor.fetchall())
            results = sel_results[0]
            self.res_list = list(results[1:4])
            return self.res_list

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.set_up_list = configAPI.configlist
        self.GET_URL = self.set_up_list[0]
        self.oAuth = oAuthGenerator.Auth(self, self.set_up_list[6], self.set_up_list[7], self.set_up_list[8], self.set_up_list[9])
        self.parms = {'client_id': self.set_up_list[1]}
        self.header = {'Authorization': self.oAuth, 'Content-Type':'application/json'}
        self.db = pymysql.connect(self.set_up_list[2], self.set_up_list[3], self.set_up_list[4],self.set_up_list[5])
        self.cursor = self.db.cursor()

    """test_rest_api_putRequest function is used to check the API PUT request with existing ID"""
    def test_Step010_putRequest_existing_id(self):
        params = {"client_id": "test_blr", "key": "test", "value": "{\"test\":1251}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This case is to check for 409 error on empty client_id"""
    def test_Step004_putRequest_empty_clientid(self):
        params = {"client_id": "", "key": "", "value": ""}
        self.id_table = self.compare_against_DB("test_blr",1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """This case is to check for 409 error on empty key and value"""
    def test_Step003_putRequest_empty_key_value(self):
        params = {"client_id": "test_blr", "key": "", "value": ""}
        self.id_table = self.compare_against_DB(params["client_id"],1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """This case is to check for 404 error on the invalid config_ID"""
    def test_Step002_putRequest_invalid_config_id(self):
        completeURL = str(self.GET_URL) + "/0"
        params = {"client_id":"test_blr","key":"1","value":"1"}
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """This case is to create a new client in table"""
    def test_Step001_postRequest_new_id(self):
        completeURL = str(self.GET_URL)
        params = {"client_id": "test_blr", "key": "test", "value": "test"}
        self.res = requests.post(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '201')
        self.assertEqual(list(self.compare_against_DB(params["client_id"],99)), list(params.values()))

    """This case is used to check for 204 upon adding net_revenue as key and a json as value"""
    def test_Step009_putRequest_adding_net_revenue(self):
        params = {"client_id": "test_blr", "key": "\"net_revenue\"", "value": "{\"NetRevenue\":\"[\"{\"id\": 1, \"client_id\": \"test\", \"org_id\": \"Org1\", \"month\": 1, \"year\": 2014, \"net_revenue\": 1002}\"]\"}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This case is used to check for 204 upon adding pos_cash_collections as key and a json as value"""
    def test_Step005_putRequest_adding_POS_cash_collections(self):
        params = {"client_id": "test_blr", "key": "pos_cash_collection", "value": "{\"Days\": 12}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This case is used to check for 204 upon adding pos_days as key and a json as value"""
    def test_Step006_putRequest_adding_POS_days(self):
        params = {"client_id": "test_blr", "key": "pos_days", "value": "{\"Days\": 12}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This case is used to check for 204 upon adding days_in_dbfb as key and a json as value"""
    def test_Step007_putRequest_adding_days_in_dnfb(self):
        params = {"client_id": "test_blr", "key": "days_in_dnfb", "value": "{\"Range\": 1}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This case is used to check for 204 upon adding days_in_dnfc as key and a json as value"""
    def test_Step008_putRequest_adding_days_in_dnfc(self):
        params = {"client_id": "test_blr", "key": "days_in_dnfc", "value": "{\"Range\": 1}"}
        self.id_table = self.compare_against_DB(params["client_id"], 1)
        completeURL = str(self.GET_URL) + "/" + str(self.id_table)
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')
        self.assertEqual(self.compare_against_DB(params["client_id"],99), list(params.values()))

    """This is to delete all the test data"""
    def test_Step012_putRequest_remove_extra_rows(self):
        query_teardown = "Delete from  rcanalytics_config_service.config_items where client_id = 'test_blr'"
        value = self.cursor.execute(query_teardown)
        self.db.commit()
        self.db.close()
        loggingAPI.logger.info("Remove the test data.")