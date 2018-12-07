import xmlrunner
import logging
import unittest
import os
from selenium import webdriver
from ParametrizedTestCase_Extractor_Vertica import ParametrizedTestCase
import time
import xlsxwriter
import re
import csv
from datetime import datetime
from loggingQuery import loggingQuery
import pandas as pd

global_var = globals()
global_var['counter'] = 1

class VerticaExtractorFE(ParametrizedTestCase):

    def download_folder(self,name):
        print(name)
        path = 'C:\\Users\\sc057441\\Desktop\\Local\\tokka\\'
        time.sleep(15)
        files = [x for x in os.listdir(path) if x.startswith("query-results")]
        print(files)
        workbook = xlsxwriter.Workbook(path + name + ".xlsx")
        print(workbook)
        worksheet = workbook.add_worksheet(name)
        print(worksheet)
        #format2 = workbook.add_format({'num_format': 'dd-mm-yy'})
       # r1 = re.compile('2.*-.*-.*')
        with open(path + files[0], "r") as csv_read:
            reader = csv.reader(csv_read)
            print(reader)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    # if r1.match(col) is not None:
                    #     col1 = datetime.strptime(col, "%Y-%m-%d")
                    #     col11 = col1.strftime("%d-%m-%Y")
                    #     col11 = datetime.strptime(col11, "%d-%m-%Y")
                    #     print(type(col11))
                    #     worksheet.write_datetime(r, c, col11, format2)
                    # else:
                    print(row,col)
                    worksheet.write(r, c, col)
        os.remove(path+files[0])

    def login(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "C:\\Users\\sc057441\\Desktop\\Local\\tokka"}
        chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.driver.implicitly_wait(10)
        self.driver.get("https://app.analytics.devcernerpophealth.com/queries")
        self.driver.refresh()
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="principal"]').send_keys(self.username_now)
        self.driver.find_element_by_xpath('//*[@id="invokeLogIn"]').click()
        self.driver.implicitly_wait(30)

    def setUp(self):
        self.username_now=self.username
        self.password_now=self.password
        self.query_now=self.query
        self.folder_now=self.folder_name


    def test_front_end_query1(self):
        self.login()
        self.query_place = self.driver.find_element_by_xpath('//*[@id="sql-input"]/textarea')
        self.query_place.clear()
        self.query_place.send_keys(self.query_now)
        self.driver.find_element_by_xpath('//*[@id="export-main-button"]').click()
        time.sleep(40)
        self.driver.implicitly_wait(30)
        self.download_folder(name=self.folder_now)
        print("Things are done")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
