from ParametrizedTestCase import ParametrizedTestCase
import unittest
import xmlrunner
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
from loginPage import login

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
global_var = globals()
global_var['div_iter'] = 1

class TestOne(ParametrizedTestCase):

    def sarath(self):
        logger.info("I am done with this.")

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

    def target_should_be_lesser_than_TopZone_and_greater_than_bottom_zone(self):
        counter = 0
        for td_iter in range(3,6):
            if counter == 1:
                counter = counter +1
                continue
            elif counter == 2:
                if 'percentage' in self.urlParam:
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

    def get_div_facility_name(self,faclity_name):
        print("entered the function")
        div_value_1 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr['
        div_value_2 = ']/td[2]'
        final_div = ''
        self.page_num = 0
        while global_var['div_iter']>0:
            print(global_var['div_iter'])
            print("entered loop")
            final_div = div_value_1 + str(global_var['div_iter']) + div_value_2
            print(final_div)
            exact_div = self.driver.find_element_by_xpath(final_div).get_attribute("innerHTML")
            print("value of exact div")
            data = exact_div[1:12]
            print(data)
            self.driver.implicitly_wait(30)
            global_var['div_iter'] = global_var['div_iter'] + 1
            print(global_var['div_iter'])
            if global_var['div_iter'] == 26:
                print("entered the 26 if")
                self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
                self.page_num = self.page_num + 1
                self.driver.implicitly_wait(30)
                global_var['div_iter'] = 1
            if data == faclity_name:
                break
        return final_div

    def check_value_at_position(self):
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.assertEqual(self.search_field_default, self.search_field_innovations)

    def check_error(self):
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg_innovations = self.error.get_attribute('title')
        logger.info(self.error_msg_innovations)
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg_default = self.error.get_attribute('title')
        logger.info(self.error_msg_default)
        screenshot_name = self.last_key[self.length_URL-1]
        self.driver.save_screenshot(screenshot_name+'.jpg')
        self.assertEqual(self.error_msg_innovations, self.error_msg_default)

    def setUp(self):
        self.driver = self.domainParam
        self.driver.get(self.urlParam)
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),'Changes you made may not be saved.')
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        for i in range(0, self.page_num):
            self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
        self.driver.implicitly_wait(30)
        if self.domainParam == 'staging':
            self.driver = login.login_staging()
        elif self.domainParam == 'dev':
            self.driver = login.login_dev()
        if 'percentage' in self.urlParam:
            self.default_data = [45, 35, 65]
            self.default_data_FE = [0.45, 0.35, 0.65]
            self.innovation_data = [32, 20, 50]
            self.innovation_data_FE = [0.32, 0.20, 0.50]
        else:
            self.default_data = [450000, 350000, 650000]
            self.default_data_FE = ['$ 4,500.00','$ 3,500.00','$ 6,500.00']
            self.innovation_data = [320000, 200000, 500000]
            self.innovation_data_FE = ['$ 3,200.00', '$ 2,000.00', '$ 5,000.00']
        self.driver.implicitly_wait(30)
        self.last_key = self.urlParam.split('/')
        self.length_URL = len(self.last_key)
        self.driver.get(self.urlParam)
        self.facility_div = self.get_div_facility_name(self.facility_name)
        print("the final div that we want is here")
        print(self.facility_div)
        self.final_innovation_div = self.facility_div.split('2]')
        self.xpath_innovation_1 = self.final_innovation_div[0]
        self.xpath_innovation_2 = ']/input'
        self.xpath_default_1 = '//*[@id="'
        self.xpath_default_2 = '"]'
        self.list_default_targets = ['target','bottom_zone','top_zone']
        self.innovations_existing_value = []
        self.defaults_existing_value = []

    def test_1_list_of_Tab(self):
        counter = 0
        final_items = " "
        html_list = self.driver.find_element_by_xpath('//*[@id="global-wrapper"]/nav/ul/li[5]/a')
        if html_list.text == 'Adjustments':
            items = html_list.find_element_by_xpath('//*[@id="global-wrapper"]/nav/ul/li[5]/ul')
            final_items = items.find_elements_by_tag_name('li')
        for item in final_items:
            counter = counter + 1
        self.assertEqual(counter,7)

    # def test_get_all_errors(self):
    #     self.target_should_be_greater_than_BottomZone()
    #     self.target_should_be_lesser_than_TopZone_and_greater_than_bottom_zone()
    #
    # def test_add_get_existing_value_and_check_various_value(self):
    #
    #     for td_iter in range(3,6):
    #         self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #         self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
    #         self.innovations_existing_value.append(self.search_field_innovations)
    #         self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
    #         self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
    #         self.defaults_existing_value.append(self.search_field_default)
    #     logger.info("THe value of existing data")
    #     logger.info(self.innovations_existing_value)
    #     logger.info(self.defaults_existing_value)
    #     self.innovations_existing_value = [800000]
    #     """The below piece of code is comented as the UI is not working as intended at the facility level. Hence we commented and it is raised in JIRA"""
    #     # for td_iter in range(3,6):
    #     #     self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #     #     self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #     #     self.search_field_innovations.clear()
    #     #     self.search_field_innovations.send_keys(self.innovation_data[td_iter - 3])
    #     #     self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
    #     #     self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #     #     self.search_field_default.clear()
    #     #     self.search_field_default.send_keys(self.default_data[td_iter - 3])
    #     # self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
    #     # self.driver.implicitly_wait(30)
    #     # self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
    #     # self.driver.implicitly_wait(30)
    #     # time.sleep(25)
    #     # self.check_value_at_position()
    #     # logger.info("The value that is present at both default and facility are the same as entered!!!")
    #     self.driver.get(self.urlParam)
    #     self.driver.implicitly_wait(30)
    #     self.facility_div = self.get_div_facility_name(self.facility_name)
    #     self.final_innovation_div = self.facility_div.split('2]')
    #     self.xpath_innovation_1 = self.final_innovation_div[0]
    #     for td_iter in range(3,6):
    #         self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #         self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_innovations.clear()
    #         self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
    #         self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_default.send_keys(self.default_data[td_iter - 3])
    #     self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
    #     self.driver.implicitly_wait(30)
    #     self.check_value_at_position()
    #     logger.info("The value at facility level is overridden with the default level value!!!")
    #     for td_iter in range(3, 6):
    #         self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #         self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_innovations.clear()
    #         logger.info("reverting it back to basic now")
    #         logger.info(self.innovations_existing_value)
    #         if td_iter == 3:
    #             logger.info("i am at td_iter at 3")
    #             self.search_field_innovations.send_keys(self.innovations_existing_value[td_iter - 3])
    #             logger.info("the new value at the position")
    #             value = self.search_field_innovations.get_attribute("value")
    #             logger.info(value)
    #         self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
    #         self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_default.clear()
    #         self.search_field_default.send_keys(self.defaults_existing_value[td_iter - 3])
    #     self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
    #     logger.info("The values are back on track!!!")


if __name__=='__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))