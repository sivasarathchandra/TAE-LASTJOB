from selenium import webdriver
from ParametrizedTestCase import ParametrizedTestCase
import unittest
import xmlrunner
import logging
import sys
from selenium.webdriver.common.action_chains import ActionChains
import time

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class TestOne(ParametrizedTestCase):

    def target_should_be_lesser_than_TopZone(self):
        counter = 0
        for td_iter in range(3,6):
            if counter == 1:
                counter = counter +1
                continue
            elif counter == 2:
                if 'percentage' in self.param:
                    logger.info("entered the counter 2 else")
                    self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
                    self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
                    self.search_field_innovations.clear()
                    self.search_field_innovations.send_keys(self.innovation_data[counter]-30)
                    self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
                    self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
                    self.search_field_default.clear()
                    self.search_field_default.send_keys(self.default_data[counter]-30)
                    counter = counter + 1
                else:
                    logger.info("entered the counter 2 else")
                    self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
                    self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
                    self.search_field_innovations.clear()
                    self.search_field_innovations.send_keys(self.innovation_data[counter] - 300000)
                    self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
                    self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
                    self.search_field_default.clear()
                    self.search_field_default.send_keys(self.default_data[counter] - 300000)
                    counter = counter + 1
            else:
                self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
                self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
                self.search_field_innovations.clear()
                self.search_field_innovations.send_keys(self.innovation_data[counter])
                self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
                self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
                self.search_field_default.clear()
                self.search_field_default.send_keys(self.default_data[counter])
                counter = counter + 1
        self.check_error()

    def target_should_be_greater_than_BottomZone(self):
        counter = 1
        for td_iter in range(3,5):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_innovations.clear()
            self.search_field_innovations.send_keys(self.innovation_data[counter])
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter-1] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.clear()
            self.search_field_default.send_keys(self.default_data[counter])
            counter = counter + 1
        self.check_error()

    def update_value_at_facility_default_not_Overridding(self):
        counter = 0
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_innovations.clear()
            self.search_field_innovations.send_keys(self.innovation_data[counter])
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.clear()
            self.search_field_default.send_keys(self.default_data[counter])
            counter = counter + 1
        iter = 0
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.assertEqual(self.search_field_innovations,self.innovation_data[iter])
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[iter] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.assertEqual(self.search_field_default, self.default_data[iter])
            iter = iter + 1

    def get_existing_value_default_facility(self):
        counter = 0
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.innovations_existing_value.append(self.search_field_innovations)
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.defaults_existing_value.append(self.search_field_innovations)
            counter = counter + 1
        logger.info(self.innovations_existing_value)
        logger.info(self.defaults_existing_value)

    def check_error(self):
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg_innovations = self.error.get_attribute('title')
        logger.info(self.error_msg_innovations)
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg_default = self.error.get_attribute('title')
        logger.info(self.error_msg_default)
        self.assertEqual(self.error_msg_innovations, self.error_msg_default)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.param)
        if 'percentage' in self.param:
            self.default_data = [45, 35, 65]
            self.innovation_data = [32, 20, 50]
        else:
            self.default_data = [450000, 350000, 650000]
            self.innovation_data = [320000, 200000, 500000]
        self.search_field_UN = self.driver.find_element_by_xpath('//*[@id="principal"]')
        self.search_field_UN.clear()
        self.search_field_UN.send_keys("RCADMIN")
        # self.search_field_PN = self.driver.find_element_by_id("authPassword")
        # self.search_field_PN.clear()
        # self.search_field_PN.send_keys("rcanalytics1")
        self.driver.find_element_by_xpath('//*[@id="invokeLogIn"]').click()
        self.driver.implicitly_wait(30)
        self.final_val = self.driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div/div/pagination/nav/span[3]/a[1]")
        self.actions = ActionChains(self.driver)
        self.actions.click(self.final_val).perform()
        self.xpath_innovation_1 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[6]/td['
        self.xpath_innovation_2 = ']/input'
        self.xpath_default_1 = '//*[@id="'
        self.xpath_default_2 = '"]'
        self.list_default_targets = ['target','bottom_zone','top_zone']
        self.innovations_existing_value = []
        self.defaults_existing_value = []

    def test_error(self):
        self.target_should_be_greater_than_BottomZone()
        self.target_should_be_lesser_than_TopZone()




if __name__=='__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))