import xmlrunner
import logging
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from loginPage import login
import time
import sys
from ParametrizedTestCase import ParametrizedTestCase
import json

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
data_dict = {}

""" TestAgeCategoriesFE class tests all the cases for age categories Front End"""
class TestAgeCategoriesFE(ParametrizedTestCase):
    """spliting the json and adding the value in respective row."""
    def splitting_json_data(self,line):
        j = 10
        self.l1 = line.split(',')
        self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
        self.xpath_1 = ']/td['
        self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
        self.xpath_3 = ']/input'
        for i in range(2, 6):
            self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
            self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
            self.search_field_UN.clear()
            self.search_field_UN.send_keys(self.l1[i - 2])

    """Default json file to extract all the case values"""
    def data_extractor(self):
        with open("Age_category_Input.json","r")as readfile:
            data_dict = json.load(readfile)
            return data_dict

    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.value = self.param
        if self.value == "staging":
            self.driver = login.login_staging()
            self.url='https://15stpdep.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category'
            self.driver.get(self.url)
            self.data_dict = self.data_extractor()
        else:
            self.driver = login.login_dev()
            self.url='https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle/config/config/age_category'
            self.driver.get(self.url)
            self.data_dict = self.data_extractor()


    # """test_same_age_category_error function is used to check the alert response on entering same same age category"""
    # def test_step4_duplicate_age_category(self):
    #     self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step4_duplicate_age_category']
    #     self.splitting_json_data(line)
    #     self.driver.implicitly_wait(30)
    #     self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
    #     self.driver.implicitly_wait(30)
    #     self.error_msg = self.eror.get_attribute('title')
    #     self.driver.save_screenshot('step4_duplicate_age_category.png')
    #     self.assertEqual(self.error_msg, 'Age Category is duplicated')
    #     logging.getLogger().info("The test case for the age category duplicate is passed!!!")
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(30)
    #     self.driver.quit()
    #
    # """test_no_age_category_error function is used to check the alert response on not entering age category"""
    # def test_step3_age_category_required(self):
    #     self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
    #     self.old_line.clear()
    #     self.old_line.send_keys(366)
    #     self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step3_age_category_required']
    #     self.splitting_json_data(line)
    #     self.driver.implicitly_wait(30)
    #     self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
    #     self.driver.implicitly_wait(30)
    #     self.error_msg = self.eror.get_attribute('title')
    #     self.driver.save_screenshot('step3_age_category_required.png')
    #     self.assertEqual(self.error_msg, 'Age Category field is required')
    #     logging.getLogger().info("The test case for the no age category is passed!!!")
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(30)
    #     self.driver.quit()
    #
    # """test_same_age_overlap_category error function is used to check the alert response on entering an overlapping age category"""
    # def test_step6_overlap_age(self):
    #     self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
    #     self.old_line.clear()
    #     self.old_line.send_keys(366)
    #     self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step6_overlap_age']
    #     self.splitting_json_data(line)
    #     self.driver.implicitly_wait(30)
    #     self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
    #     self.driver.implicitly_wait(30)
    #     self.error_msg = self.eror.get_attribute('title')
    #     self.driver.save_screenshot('step6_overlap_age.png')
    #     self.assertEqual(self.error_msg, 'There is an overlap between this age category and 0-30')
    #     logging.getLogger().info("The test case for the overlap age category is passed!!!")
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(30)
    #     self.driver.quit()
    #
    # """test_same_age_gap_category error function is used to check the alert response on entering gap in between age category"""
    # def test_step5_age_gap(self):
    #     self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
    #     self.old_line.clear()
    #     self.old_line.send_keys(366)
    #     self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step5_age_gap']
    #     self.splitting_json_data(line)
    #     self.driver.implicitly_wait(30)
    #     self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
    #     self.driver.implicitly_wait(30)
    #     self.error_msg = self.eror.get_attribute('title')
    #     self.driver.save_screenshot('step5_age_gap.png')
    #     self.assertEqual(self.error_msg, 'There is a gap between this age category and 366+')
    #     logging.getLogger().info("The test case for the age gap category is passed!!!")
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(30)
    #     self.driver.quit()
    #
    # """test_begin_age_greater_category error function is used to check the alert response if the begin age is greater"""
    # def test_step7_begin_age_less_than_end_age(self):
    #     self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
    #     self.old_line.clear()
    #     self.old_line.send_keys(366)
    #     self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step7_begin_age_less_than_end_age']
    #     self.splitting_json_data(line)
    #     self.driver.implicitly_wait(30)
    #     self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
    #     self.driver.implicitly_wait(30)
    #     self.error_msg = self.eror.get_attribute('title')
    #     self.driver.save_screenshot('step7_begin_age_less_than_end_age.png')
    #     self.assertEqual(self.error_msg, 'Begin Age should be less than End Age')
    #     logging.getLogger().info("The test case for the begin age greater than end age is passed!!!")
    #     self.driver.get(self.url)
    #     self.driver.implicitly_wait(30)
    #     self.driver.quit()
    #
    # """Deleting and adding a new row on the front end"""
    # def test_step2_negative_values_save(self):
    #     j = 9
    #     self.xpath_Prefix = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
    #     self.xpath_Suffix = ']/td[6]/div'
    #     for self.iter in range(1, 9):
    #         self.first_line_xpath = self.xpath_Prefix + str(self.iter) + self.xpath_Suffix
    #         if self.iter == 1:
    #             self.del_button = self.driver.find_element_by_xpath(self.first_line_xpath)
    #             self.actions = ActionChains(self.driver)
    #             self.actions.click(self.del_button).perform()
    #     self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.save_page).perform()
    #     time.sleep(10)
    #     self.driver.get(self.url)
    #     self.new_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[8]/td[7]/div')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.new_line).perform()
    #     line = self.data_dict['step2_negative_values_save']
    #     l1 = line.split(',')
    #     self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
    #     self.xpath_1 = ']/td['
    #     self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
    #     self.xpath_3 = ']/input'
    #     for self.iteration in range(2, 6):
    #         self.o_xpath = self.xpath_2 + str(self.iteration) + self.xpath_3
    #         self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
    #         self.search_field_UN.clear()
    #         self.search_field_UN.send_keys(l1[self.iteration - 2])
    #     self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
    #     self.actions = ActionChains(self.driver)
    #     self.actions.click(self.save_page).perform()
    #     logging.getLogger().info("Deleted and entered a new row")
    #     self.driver.save_screenshot('step2_negative_values_save.png')
    #     self.driver.implicitly_wait(30)
    #     validate = 2
    #     self.keys_validation = ["1", "Not Aged", "-9,999", "-1"]
    #     self.driver.get(self.url)
    #     for self.increment in self.keys_validation:
    #         self.xpath0 = '//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[1]/td['
    #         self.xpath1 = validate
    #         self.xpath2 = ']/input'
    #         self.xpath_validate = self.driver.find_element_by_xpath(self.xpath0 + str(self.xpath1) + self.xpath2).get_attribute("value")
    #         self.assertEqual(self.increment, self.xpath_validate)
    #         validate = validate + 1
    #     logging.getLogger().info("Data is validated after the save!!!")
    #     self.driver.implicitly_wait(30)
    #     self.driver.close()

    def test_step1_positive_values_save(self):
        j = 8
        self.xpath_Prefix = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
        self.xpath_Suffix = ']/td[6]/div'
        for self.iter in range(1, 9):
            if self.iter <3:
                self.first_line_xpath = self.xpath_Prefix + str(self.iter) + self.xpath_Suffix
                self.del_button = self.driver.find_element_by_xpath(self.first_line_xpath)
                self.actions = ActionChains(self.driver)
                self.actions.click(self.del_button).perform()
        self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.save_page).perform()
        time.sleep(10)
        self.driver.get(self.url)
        self.new_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[7]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        line = self.data_dict['step1_positive_values_save']
        for each in line:
            l1 = each.split(',')
            self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
            self.xpath_1 = ']/td['
            self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
            self.xpath_3 = ']/input'
            if j == 9:
                print("Enter the id")
                self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[8]/td[7]/div')
                self.actions = ActionChains(self.driver)
                self.actions.click(self.new_line).perform()
            for self.iteration in range(2, 6):
                self.o_xpath = self.xpath_2 + str(self.iteration) + self.xpath_3
                print(self.o_xpath)
                self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                self.search_field_UN.clear()
                self.search_field_UN.send_keys(l1[self.iteration - 2])
            j=j+1
            if j >9:
                self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
                self.actions = ActionChains(self.driver)
                self.actions.click(self.save_page).perform()
                self.driver.implicitly_wait(30)
        validate = 2
        self.keys_validation = ["1", "Not Aged", "-9,999", "0"]
        self.driver.get(self.url)
        for self.increment in self.keys_validation:
            self.xpath0 = '//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[1]/td['
            self.xpath1 = validate
            self.xpath2 = ']/input'
            self.xpath_validate = self.driver.find_element_by_xpath(
                self.xpath0 + str(self.xpath1) + self.xpath2).get_attribute("value")
            self.assertEqual(self.increment, self.xpath_validate)
            validate = validate + 1
        logging.getLogger().info("Data is validated after the save!!!")
        self.driver.save_screenshot('step1_positive_values_save.png')
        self.driver.implicitly_wait(30)
        revert_old_value = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[1]/td[5]/input')
        revert_old_value.clear()
        revert_old_value.send_keys('1-')
        revert_old_value_2 = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[2]/td[4]/input')
        revert_old_value_2.clear()
        revert_old_value_2.send_keys('0')
        self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.save_page).perform()
        self.driver.implicitly_wait(30)
        self.driver.close()

"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))