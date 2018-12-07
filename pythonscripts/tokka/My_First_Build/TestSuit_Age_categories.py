import pymysql
import unittest
import requests
import os
import sys
import xmlrunner
import logging
import json

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

""" TestAgeCategories class tests all the cases for age categories api"""


class TestAgeCategories(unittest.TestCase):
    """get_value_from_config method is used to get all requirments like api and DB details for this service api"""

    def get_value_from_config(self):
        self.configlist = []
        with open("Config_Age_categories.txt", "r") as readconfigfile:
            for line in readconfigfile:
                if line.startswith('URL') or line.startswith('client_id') or line.startswith('DB1') or line.startswith(
                        'UN') or line.startswith('PWD') or line.startswith('DBN'):
                    cleanedline = line.strip()
                    split = cleanedline.split('=')
                    self.configlist.append(split[1])
            return self.configlist

    """setUp method initialize the variables and values that are used across the test cases"""

    def setUp(self):
        self.set_up_list = self.get_value_from_config()
        self.GET_URL = self.set_up_list[0]
        self.oAuth = self.Auth()
        self.parms = {'client_id': self.set_up_list[1]}
        self.header = {'Authorization': self.oAuth, 'Content-Type': 'application/json'}
        self.db = pymysql.connect(self.set_up_list[2], self.set_up_list[3], self.set_up_list[4], self.set_up_list[5])
        self.cursor = self.db.cursor()

    """Auth function is used to get the oAuth value. As of now using auth-header-1.3.jar which will be replaced oAuth generator"""

    def Auth(self):
        oAuth = ""
        os.system("java -jar auth-header-1.3.jar -k c0c11d7a-48c1-461d-8be9-56e9fb60b28f -s Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l > oAuthKey.txt")
        with open("oAuthKey.txt", "r") as oAuthFile:
            for line in oAuthFile:
                cleanedLine = line.strip()
                if cleanedLine:  # is not empty
                    # print("Recieved the token")
                    oAuth = cleanedLine
        logging.getLogger().info("returning oAuth Value")
        return oAuth

    """test_rest_api_error function is used to check the unauthorized verification of API 401 response"""

    def test_rest_api_error(self):
        oAuth = '2'
        header1 = {'Authorization': oAuth}
        session = requests.Session()
        self.res = requests.get(self.GET_URL, headers=header1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '401')

    """test_rest_api_NotFound function is used to check the API NotFound 404 response"""

    def test_rest_api_NotFound(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/age_categorie'
        self.res = requests.get(self.GET_URL_1, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_Conflicts function is used to check the API Conflicts 409 response"""

    def test_rest_api_Conflicts(self):
        self.GET_URL2 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/config_items'
        self.res = requests.post(self.GET_URL2, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '409')

    """test_rest_api_badRequest function is used to check the API badrequest 400 response"""

    def test_rest_api_badRequest(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, data=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '400')

    """test_rest_api_noContent function is used to check the API NoContent 204 response"""

    def test_rest_api_noContent(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '204')

    """test_rest_api_invalidRecord function is used to check the API InValidRecord 404 response"""

    def test_rest_api_invalidRecord(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.post(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_putRequest function is used to check the API PUT request"""

    def test_rest_api_putRequest(self):
        self.data1 = {"age_categories": "[{\"id\": 1,\"client_id\": \"DEFAULT\",\"age_category\":\"366+\",\"begin_age\": 50,\"end_age\": 100,\"sort_order\": 2}]"}
        self.res = requests.put(self.GET_URL, headers=self.header, json=self.data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '200')

    """test_rest_api_getRequest function is used to check the API GET Request"""

    def test_rest_api_getRequest(self):
        self.API_Output = {}
        self.res = requests.get(self.GET_URL, headers=self.header)
        self.key_list = ['age_category', 'begin_age', 'end_age', 'sort_order']
        print("\n")
        print("this is the response of text")
        print(self.res.text)
        self.res_json = json.loads(self.res.text)
        print(self.res_json)
        for self.iteration in self.res_json:
            print(self.iteration)
            for self.keys_res, self.values_res in self.iteration.items():
                if self.keys_res in self.key_list:
                    self.API_Output.setdefault(self.keys_res, []).append(self.values_res)
        logging.getLogger().info("API Output: %s" % self.API_Output)
        # SQL DB Connection and fetching and disconnection as well
        self.query1 = "SELECT age_category,begin_age,end_age,sort_order FROM age_categories WHERE client_id=" + "'" + \
                      self.set_up_list[1] + "'"
        self.cursor.execute(self.query1)
        self.data = set(self.cursor.fetchall())
        self.col_names = [i[0] for i in self.cursor.description]
        self.DB_Output = {self.col_names[0]: [self.x[0] for self.x in self.data],
                          self.col_names[1]: [self.x[1] for self.x in self.data],
                          self.col_names[2]: [self.x[2] for self.x in self.data],
                          self.col_names[3]: [self.x[3] for self.x in self.data], }
        logging.getLogger().info("DataBase Output")
        logging.getLogger().info(self.DB_Output)
        self.db.close()
        logging.getLogger().info("Validating the response")
        # validation of the data from DB with the api
        for self.keys_val, self.value_val in self.API_Output.items():
            if self.keys_res in self.key_list:
                self.assert_list1 = self.API_Output[self.keys_res]
                self.assert_list2 = self.DB_Output[self.keys_res]
                self.assertEqual(set(self.assert_list2).issuperset(set(self.assert_list1)), True)
        logging.getLogger().info("Validated")


"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))