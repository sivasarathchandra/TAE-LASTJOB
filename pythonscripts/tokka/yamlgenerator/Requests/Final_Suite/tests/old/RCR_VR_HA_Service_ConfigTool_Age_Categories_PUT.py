import pymysql
import unittest
import requests
import os
from Tests.config_API import configAPI
from Tests.logging_API import loggingAPI
from Tests.oAuthGenerator import oAuthGenerator

# WORKSPACE = os.environ['WORKSPACE']

""" TestAgeCategories class tests all the cases for age categories api"""
class TestAgeCategoriesPut(unittest.TestCase):

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.set_up_list = configAPI.configlist
        self.GET_URL = self.set_up_list[0]
        self.oAuth = oAuthGenerator.Auth(self,self.set_up_list[6],self.set_up_list[7],self.set_up_list[8],self.set_up_list[9])
        self.parms = {'client_id': self.set_up_list[1]}
        self.header = {'Authorization': self.oAuth, 'Content-Type':'application/json'}
        self.db = pymysql.connect(self.set_up_list[2], self.set_up_list[3], self.set_up_list[4],self.set_up_list[5])
        self.cursor = self.db.cursor()

    """test_rest_api_putRequest function is used to check the API PUT request"""
    def test_Step1_putRequest(self):
        age_category_list, begin_age_list, end_age_list, sort_order_list = ([] for i in range(4))
        data = {"Not Aged": [-9999, -1], "0-30": [0, 30], "31-60": [31, 60], "61-90": [61, 90], "91-120": [91, 120],"121-150": [121, 150], "151-180": [151, 180], "181-365": [181, 365], "366-380": [366, 380],"381+": [381, ""]}
        counter = 1
        for key, value in data.items():
            val = [{"client_id": "test_client1", "age_category": key, "begin_age": value[0], "end_age": value[1],"sort_order": counter}]
            for key1, value1 in val[0].items():
                if key1 == "age_category":
                    age_category_list.append(value1)
                elif key1 == "begin_age":
                    begin_age_list.append(value1)
                elif key1 == "end_age":
                    end_age_list.append(value1)
                elif key1 == "sort_order":
                    sort_order_list.append(value1)
            val = str(val).replace("'", '"')
            self.data_request = {"age_categories": val}
            counter = counter + 1
            loggingAPI.logger.info("Tis is the input given to the api : " + str(self.data_request))
            self.res = requests.put(self.GET_URL, headers=self.header, json=self.data_request)
            self.response = self.res.status_code
            self.assertEqual(str(self.response), '204')
        end_age_list = [None if v is "" else v for v in end_age_list]
        self.selectQuery = "select * from age_categories where client_id" + " " + "=" + " " + "'" + "test_client1" + "'"
        self.cursor.execute(self.selectQuery)
        self.data = set(self.cursor.fetchall())
        self.col_names = [i[0] for i in self.cursor.description]
        self.DB_Output = {self.col_names[1]: [self.x[1] for self.x in self.data],self.col_names[2]: [self.x[2] for self.x in self.data],self.col_names[3]: [self.x[3] for self.x in self.data],self.col_names[4]: [self.x[4] for self.x in self.data],self.col_names[7]: [self.x[7] for self.x in self.data], }
        loggingAPI.logger.info("DataBase Output : " + str(self.DB_Output))
        for key, value in self.DB_Output.items():
            if key == "age_category":
                self.assertEqual(set(self.DB_Output[key]), set(age_category_list))
            elif key == "begin_age":
                self.assertEqual(set(self.DB_Output[key]), set(begin_age_list))
            elif key == "end_age":
                self.assertEqual(set(self.DB_Output[key]), set(end_age_list))
            elif key == "sort_order":
                self.assertEqual(set(self.DB_Output[key]), set(sort_order_list))
        loggingAPI.logger.info("all the columns are now validated")

    """test_putRequest_error function is used to check the API PUT request error when sent a request with id as 0 it returns 409"""
    def test_Step2_putRequest_error(self):
        self.data1 = {"age_categories": "[{\"id\": 5,\"client_id\": \"\",\"age_category\":\"test1\",\"begin_age\": 151,\"end_age\": 200,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """Delete the test data that is created"""
    def tearDown(self):
        self.query_teardown = "DELETE from age_categories WHERE client_id = "+"'"+"test_client1"+"'"+";"
        value = self.cursor.execute(self.query_teardown)
        loggingAPI.logger.info("The value returned after deleting the data is: " + str(value))
        self.db.commit()
        self.db.close()
        loggingAPI.logger.info("Removed the test data that is created.")