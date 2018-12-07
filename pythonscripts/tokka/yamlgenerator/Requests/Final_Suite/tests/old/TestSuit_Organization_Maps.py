import pymysql
import unittest
import requests
import os
import xmlrunner
from Tests.config_API import configAPI
from Tests.logging_API import loggingAPI
WORKSPACE = os.environ['WORKSPACE']

configlist = []


class TestOrganizationMaps(unittest.TestCase):

    def setUp(self):
        self.configlist = configAPI.configlist
        self.GET_URL = self.configlist[0]
        self.oAuth = self.Auth()
        self.header = {'Authorization': self.oAuth, 'Content-Type': 'application/json'}
        self.parms = {'client_id': self.configlist[1], 'millennium_org_id': self.configlist[2]}
        self.db = pymysql.connect(self.configlist[3], self.configlist[4], self.configlist[5], self.configlist[6])
        self.cursor = self.db.cursor()

    def Auth(self):
        self.oAuth1=""
        os.system("java -jar "+WORKSPACE+"/tests/auth-header-1.3.jar -k c0c11d7a-48c1-461d-8be9-56e9fb60b28f -s Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l > oAuthKey.txt")
        with open("oAuthKey.txt","r") as oAuthFile:
            for self.line in oAuthFile:
                self.cleanedLine = self.line.strip()
                if self.cleanedLine:  # is not empty
                    #print("Recieved the token")
                    self.oAuth1 = self.cleanedLine
        loggingAPI.logger.info("returning oAuth Value")
        return self.oAuth1

    """test_rest_api_error function is used to check the unauthorized verification of API 401 response"""

    def test_error(self):
        oAuth = '2'
        header1 = {'Authorization': oAuth}
        session = requests.Session()
        self.res = requests.get(self.GET_URL, headers=header1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '401')

    """test_rest_api_NotFound function is used to check the API NotFound 404 response"""

    def test_NotFound(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_map'
        self.res = requests.get(self.GET_URL_1, headers=self.header)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong client_id 404 response"""

    def test_NotFound_client_Id(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps'
        self.param1 = {'client_id': '2'}
        self.res = requests.get(self.GET_URL_1, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Millennium_ID 404 response"""

    def test_NotFound_Millennium_Id(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps'
        self.param1 = {'millennium_org_id': '2'}
        self.res = requests.get(self.GET_URL_1, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Healthe_intent_org_id 404 response"""

    def test_NotFound_healthe_intent_org_id(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps'
        self.param1 = {'healthe_intent_org_id': '2'}
        self.res = requests.get(self.GET_URL_1, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_NotFound function is used to check the wrong Healthe_intent_org 404 response"""

    def test_NotFound_healthe_intent_org(self):
        self.GET_URL_1 = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps'
        self.param1 = {'healthe_intent_org': '2'}
        self.res = requests.get(self.GET_URL_1, headers=self.header, params=self.param1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '404')

    """test_rest_api_badRequest function is used to check the API badrequest 400 response"""

    def test_badRequest(self):
        GET_URL = 'http://services.devhealtheintent.net/rc-dashboard-config-service/organization_maps/1'
        data1 = {'millennium_org_id': 'test', 'client_id': 'test', 'healthe_intent_org_id': 'test',
                 'healthe_intent_org_name': 'test'}
        self.res = requests.put(GET_URL, headers=self.header, data=data1)
        self.response = self.res.status_code
        self.assertEqual(str(self.response), '400')

    """test_rest_api_getRequest function is used to check the API GET Request"""

    def test_getRequest(self):
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
                      self.configlist[1] + "'" + " and millennium_org_id =" + "'" + self.configlist[2] + "'"
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