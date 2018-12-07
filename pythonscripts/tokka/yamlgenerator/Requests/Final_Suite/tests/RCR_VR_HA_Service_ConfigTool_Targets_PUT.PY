#!/usr/bin/python3
import pymysql
import unittest
import requests
import os
from decimal import *
from tests.configAPI import configAPI
from tests.loggingAPI import loggingAPI
from tests.oAuthGenerator import oAuthGenerator

API_INPUT={}

""" TestAgeCategories class tests all the cases for age categories api"""
class TestTargetsPut(unittest.TestCase):

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.set_up_list = configAPI.configlist
        self.GET_URL = self.set_up_list[0]
        self.oAuth = oAuthGenerator.Auth(self, self.set_up_list[6], self.set_up_list[7], self.set_up_list[8], self.set_up_list[9])
        self.params = {'client_id': self.set_up_list[1]}
        self.header = {'Authorization': self.oAuth, 'Content-Type':'application/json'}
        self.db = pymysql.connect(self.set_up_list[2], self.set_up_list[3], self.set_up_list[4],self.set_up_list[5])
        self.cursor = self.db.cursor()

    """test_putRequest_IDExists_validParams function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are valid"""
    def test_Step1_putRequest(self):
        metric_key_list, target_list, top_zone_list, bottom_zone_list = ([] for i in range(4))
        data = {"total_ar": [1251, 5000, 1000], "total_adjustments": [1251.25, 5000.69, 1000.11],
                "total_cash": [1251, 5000, 1000], "alos": [2, 5, 1], "clean_claim_rate": [1251, 5000, 1000],
                "denial_rate_zero_pay": [0.5, 1.0, 0.1], "case_mix_index": [1251, 5000, 1000],
                "total_gross_revenue": [1251, 5000, 1000]}
        for key, value in data.items():
            metric_key_list.append(key)
            target_list.append(Decimal(value[0]).quantize(Decimal('1.0000')))
            top_zone_list.append(Decimal(value[1]).quantize(Decimal('1.0000')))
            bottom_zone_list.append(Decimal(value[2]).quantize(Decimal('1.0000')))
            data_half = [{"facility_id": "test", "target": value[0], "top_zone": value[1], "bottom_zone": value[2]}]
            data_half = str(data_half).replace("'", '"')
            data_json = {"targets": str(data_half), "client_id": "test_client1", "metric_key": key}
            loggingAPI.logger.info("The value that is sent as json to the api is : "+str(data_json))
            self.res = requests.put(self.GET_URL, headers=self.header, json=data_json)
            self.response = self.res.status_code
            self.assertEqual(str(self.response), '204')
        self.selectQuery = "select * from targets where client_id"+" "+"="+" "+"'"+"test_client1"+"'"
        self.cursor.execute(self.selectQuery)
        self.data = set(self.cursor.fetchall())
        self.col_names = [i[0] for i in self.cursor.description]
        self.DB_Output = {self.col_names[2]: [self.x[2] for self.x in self.data],
                          self.col_names[4]: [self.x[4] for self.x in self.data],
                          self.col_names[5]: [self.x[5] for self.x in self.data],
                          self.col_names[6]: [self.x[6] for self.x in self.data]}
        loggingAPI.logger.info("The data from DB is like : "+str(self.DB_Output))
        for key, value in self.DB_Output.items():
            if key == "metric_key":
                self.assertEqual(set(self.DB_Output[key]), set(metric_key_list))
            elif key == "target":
                self.assertEqual(set(self.DB_Output[key]), set(target_list))
            elif key == "top_zone":
                self.assertEqual(set(self.DB_Output[key]), set(top_zone_list))
            elif key == "bottom_zone":
                self.assertEqual(set(self.DB_Output[key]), set(bottom_zone_list))
        loggingAPI.logger.info("all the columns are now validated")

    """test_putRequest_IDExists_invalidParams_error function is used to check the API PUT request when the organization map with the given ID already exists and the give parameters are invalid"""
    def test_Step2_putRequest_error(self):
        self.data = {"targets": "[{\"facility_id\": \"test\", \"target\": 1251, \"top_zone\": 6000, \"bottom_zone\": 2000}]", "client_id": "", "metric_key": ""}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """Delete the test data that is created"""
    def tearDown(self):
        self.query = "DELETE from targets WHERE client_id = "+"'"+"test_client1"+"'"+";"
        value = self.cursor.execute(self.query)
        loggingAPI.logger.info("The value returned after deleting the data is: " + str(value))
        self.db.commit()
        self.db.close()
        loggingAPI.logger.info("Removed the test data that is created.")