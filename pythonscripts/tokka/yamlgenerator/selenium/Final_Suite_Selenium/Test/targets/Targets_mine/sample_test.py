import unittest
from selenium import webdriver
import xmlrunner
import logging
from loginPage import login
from ParametrizedTestCase import ParametrizedTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

global_var = globals()
global_var['div_iter'] = 1
global_var['counter'] = 0


class SampleTest(ParametrizedTestCase):

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
        self.assertEqual(self.error_msg_innovations, self.error_msg_default)

    def get_div_facility_name(self,faclity_name):
        print("entered the function")
        div_value_1 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr['
        div_value_2 = ']/td[2]'
        final_div = ''
        while global_var['div_iter']>0:
            final_div = div_value_1 + str(global_var['div_iter']) + div_value_2
            exact_div = self.driver.find_element_by_xpath(final_div).get_attribute("innerHTML")
            length = len(exact_div)
            data = exact_div[1:length-1]
            self.driver.implicitly_wait(30)
            global_var['div_iter'] = global_var['div_iter'] + 1
            print(global_var['div_iter'])
            if global_var['div_iter'] == 26:
                self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
                self.driver.implicitly_wait(30)
            if data == faclity_name:
                break
        print("returning the final div")
        global_var['div_iter'] = 1
        return final_div

    def setUp(self):
        self.facility_div = ""
        if 'percentage' in self.urlParam:
            self.default_data = [45, 35, 65]
            self.default_data_FE = [0.45, 0.35, 0.65]
            self.innovation_data = [32, 20, 50]
            self.innovation_data_FE = [0.32, 0.20, 0.50]
        else:
            self.default_data = [450000, 350000, 650000]
            self.default_data_FE = ['$ 4,500.00', '$ 3,500.00', '$ 6,500.00']
            self.innovation_data = [320000, 200000, 500000]
            self.innovation_data_FE = ['$ 3,200.00', '$ 2,000.00', '$ 5,000.00']
        self.driver = self.driverParam
        self.driver.get(self.urlParam)
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),'Changes you made may not be saved.')
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        self.last_key = self.urlParam.split('/')
        self.length_URL = len(self.last_key)
        self.facility_div = self.get_div_facility_name(self.facility_name)
        self.final_innovation_div = self.facility_div.split('2]')
        self.xpath_innovation_1 = self.final_innovation_div[0]
        print(self.xpath_innovation_1)
        self.xpath_innovation_2 = ']/input'
        self.xpath_default_1 = '//*[@id="'
        self.xpath_default_2 = '"]'
        self.list_default_targets = ['target', 'bottom_zone', 'top_zone']
        self.innovations_existing_value = []
        self.defaults_existing_value = []

    # def test_step_target_should_be_greater_than_BottomZone(self):
    #     for td_iter in range(3,5):
    #         self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #         self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_innovations.clear()
    #         self.search_field_innovations.send_keys(self.innovation_data[td_iter-2])
    #         self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter-3] + self.xpath_default_2
    #         self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #         self.search_field_default.clear()
    #         self.search_field_default.send_keys(self.default_data[td_iter-2])
    #     self.check_error()
    #     self.driver.quit()
    #
    # def test_step_target_should_be_lesser_than_TopZone(self):
    #     counter = 0
    #     for td_iter in range(3,6):
    #         if counter == 1:
    #             counter = counter +1
    #             continue
    #         elif counter == 2:
    #             if 'percentage' in self.urlParam:
    #                 logger.info("entered the counter 2 else")
    #                 self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #                 self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_innovations.clear()
    #                 self.search_field_innovations.send_keys(self.innovation_data[counter]-30)
    #                 self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
    #                 self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_default.clear()
    #                 self.search_field_default.send_keys(self.default_data[counter]-30)
    #                 counter = counter + 1
    #             else:
    #                 logger.info("entered the counter 2 else")
    #                 self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #                 self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_innovations.clear()
    #                 self.search_field_innovations.send_keys(self.innovation_data[counter] - 300000)
    #                 self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
    #                 self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_default.clear()
    #                 self.search_field_default.send_keys(self.default_data[counter] - 300000)
    #                 counter = counter + 1
    #                 time.sleep(30)
    #         else:
    #             self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #             self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #             self.search_field_innovations.clear()
    #             self.search_field_innovations.send_keys(self.innovation_data[counter])
    #             self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
    #             self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #             self.search_field_default.clear()
    #             self.search_field_default.send_keys(self.default_data[counter])
    #             counter = counter + 1
    #             time.sleep(30)
    #     self.check_error()
    #     self.driver.quit()
    #
    # def test_step_top_should_be_greater_bottom(self):
    #     counter = 0
    #     for td_iter in range(4, 6):
    #         if counter == 1:
    #             if 'percentage' in self.urlParam:
    #                 logger.info("entered the counter 2 else")
    #                 self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #                 self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_innovations.clear()
    #                 self.search_field_innovations.send_keys(self.innovation_data[counter] - 30)
    #                 self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[
    #                     counter] + self.xpath_default_2
    #                 self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_default.clear()
    #                 self.search_field_default.send_keys(self.default_data[counter] - 30)
    #                 counter = counter + 1
    #             else:
    #                 logger.info("entered the counter 2 else")
    #                 self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #                 self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_innovations.clear()
    #                 self.search_field_innovations.send_keys(self.innovation_data[counter] - 300000)
    #                 self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter+1] + self.xpath_default_2
    #                 self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #                 self.search_field_default.clear()
    #                 self.search_field_default.send_keys(self.default_data[counter] - 300000)
    #                 counter = counter + 1
    #                 time.sleep(30)
    #         else:
    #             self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
    #             self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
    #             self.search_field_innovations.clear()
    #             self.search_field_innovations.send_keys(self.innovation_data[counter])
    #             self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter+1] + self.xpath_default_2
    #             self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
    #             self.search_field_default.clear()
    #             self.search_field_default.send_keys(self.default_data[counter])
    #             counter = counter + 1
    #             time.sleep(30)
    #     self.check_error()
    #     self.driver.quit()
    #
    def test_1_list_of_Tab(self):
        final_items_list = []
        counter = 0
        final_items = " "
        html_list = self.driver.find_element_by_xpath('//*[@id="global-wrapper"]/nav/ul/li[5]/a')
        if html_list.text == 'Adjustments':
            items = html_list.find_element_by_xpath('//*[@id="global-wrapper"]/nav/ul/li[5]/ul')
            final_items = items.find_elements_by_tag_name('li')
        for item in final_items:
            counter = counter + 1
            final_items_list.append(item.text)
        self.assertEqual(counter,7)
        self.assertEqual(final_items_list, self.urlListParam)
        self.driver.quit()

    def test_2_existingvalue(self):
        for td_iter in range(3, 6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.innovations_existing_value.append(self.search_field_innovations)
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute("value")
            self.defaults_existing_value.append(self.search_field_default)
        logger.info("THe value of existing data")
        logger.info(self.innovations_existing_value)
        logger.info(self.defaults_existing_value)
        for iter in range(0,3):
            val1 = self.innovations_existing_value[iter].split(" ")
            val2 = self.defaults_existing_value[iter].split(" ")
            self.innovations_existing_value[iter] = int(val1[1].replace(',','').replace('.',''))
            self.defaults_existing_value[iter] = int(val2[1].replace(',','').replace('.',''))
        logger.info("THe value of existing data after splitting")
        logger.info(self.innovations_existing_value)
        logger.info(self.defaults_existing_value)
        for td_iter in range(3, 6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_innovations.clear()
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.clear()
            self.search_field_default.send_keys(self.default_data[td_iter - 3])
        self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
        self.driver.implicitly_wait(30)
        self.check_value_at_position()
        print("The values of existing")
        print(self.innovations_existing_value)
        print(self.defaults_existing_value)
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.clear()
        self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
        self.driver.implicitly_wait(30)
        for td_iter in range(3,4):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_innovations.clear()
            self.search_field_innovations.send_keys(self.innovations_existing_value[td_iter - 3])
        self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
        self.driver.implicitly_wait(30)
        for td_iter in range(3,6):
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[td_iter - 3] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.send_keys(self.defaults_existing_value[td_iter - 3])
        self.driver.find_element_by_xpath('//*[@id="save_config"]').click()
        self.driver.implicitly_wait(30)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))