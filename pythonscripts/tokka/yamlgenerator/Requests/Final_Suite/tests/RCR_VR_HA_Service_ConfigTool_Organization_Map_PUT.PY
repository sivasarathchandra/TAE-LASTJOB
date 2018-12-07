#!/usr/bin/python3
import pymysql
import unittest
import requests
import random
from tests.configAPI import configAPI
from tests.loggingAPI import loggingAPI
from tests.oAuthGenerator import oAuthGenerator

""" TestAgeCategories class tests all the cases for age categories api"""
class TestOrganizationMapsDev(unittest.TestCase):

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.configlist = configAPI.configlist
        self.GET_URL = self.configlist[0]
        self.oAuth = oAuthGenerator.Auth(self, self.configlist[5], self.configlist[6], self.configlist[7],self.configlist[8])
        self.header = {'Authorization': self.oAuth, 'Content-Type': 'application/json'}
        self.db = pymysql.connect(self.configlist[1], self.configlist[2], self.configlist[3], self.configlist[4])
        self.cursor = self.db.cursor()

    def select_query(self, client_name):
        sel_query = "SELECT * FROM RCANALYTICS_CONFIG_SERVICE.ORGANIZATION_MAPS WHERE CLIENT_ID = " + "'" + client_name + "';"
        self.cursor.execute(sel_query)
        sel_results = list(self.cursor.fetchall())
        results = sel_results[0]
        res_list = list(results[1:5])
        return res_list

    """test_putRequest_newID_validParams function is used to check the API PUT request when we pass a new ID along with valid data"""
    def test_Step1_putRequest_newID_validParams(self):
        completeURL = str(self.GET_URL) + "/" + str(random.randint(95000,295000))
        params = {"client_id": "test_client", "millennium_org_id": "test_org_id3",
                       "healthe_intent_org_id": "test_healthe_intent_org_id",
                       "healthe_intent_org_name": "test_healthe_intent_org_name3"}
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '200')
        self.assertEqual(self.select_query('test_client'), list(params.values()))

    """test_putRequest_IDExists_invalidParams_error function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are invalid"""
    def test_Step2_putRequest_newID_invalidParams_error(self):
        completeURL = str(self.GET_URL) + "/" + str(random.randint(95000,295000))
        params = {"client_id": "test_client2", "millennium_org_id": None,
                  "healthe_intent_org_id": "test_healthe_intent_org_id2",
                  "healthe_intent_org_name": None}
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')


    """test_putRequest_IDExists_validParams function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are valid"""
    def test_Step3_putRequest_IDExists_validParams(self):
        completeURL = str(self.GET_URL) + "/59861"
        params = {"client_id": "test_client3", "millennium_org_id": "test_org_id3",
                           "healthe_intent_org_id": "test_healthe_intent_org_id3",
                           "healthe_intent_org_name": "test_healthe_intent_org_name3"}
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '200')
        self.assertEqual(self.select_query('test_client3'), list(params.values()))

    """test_putRequest_IDExists_invalidParams_error function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are invalid"""
    def test_Step4_putRequest_IDExists_invalidParams_error(self):
        completeURL = str(self.GET_URL) + "/59861"
        params = {"client_id": "test_client4", "millennium_org_id": None,
                  "healthe_intent_org_id": "test_healthe_intent_org_id4",
                  "healthe_intent_org_name": None}
        self.res = requests.put(completeURL, headers=self.header, json=params)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """Delete the test data that is created"""
    def tearDown(self):
        updt_query = "UPDATE RCANALYTICS_CONFIG_SERVICE.ORGANIZATION_MAPS \
                        SET CLIENT_ID = 'RCA_test_client_existing', \
                        MILLENNIUM_ORG_ID = 'RCA_test_millennium_org_existing', \
                        HEALTHE_INTENT_ORG_ID = 'RCA_test_healthe_intent_org_existing', \
                        HEALTHE_INTENT_ORG_NAME = 'RCA_test_healthe_intent_org_existing', \
                        UPDATED_AT = CURRENT_TIMESTAMP \
                    WHERE ID=59861;"
        del_query = "DELETE FROM ORGANIZATION_MAPS WHERE CLIENT_ID LIKE 'test_client%';"
        self.cursor.execute(updt_query)
        self.cursor.execute(del_query)
        self.db.commit()
        self.db.close()
        loggingAPI.logger.info("Removed the test data that is created.")