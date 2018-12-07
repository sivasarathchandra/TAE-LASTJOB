import xmlrunner
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
import sys
import time

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

""" TestAgeCategoriesFE class tests all the cases for age categories Front End"""
class TestAgeCategoriesFE(unittest.TestCase):
    """setUp method initialize the variables and values that are used across the test cases"""
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=800x600")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.execute_script("window.onbeforeunload = function() {};")
        self.search_field_UN = self.driver.find_element_by_id("authUsername")
        self.search_field_UN.clear()
        self.search_field_UN.send_keys("revcycleanalytics@gmail.com")
        self.search_field_PN = self.driver.find_element_by_id("authPassword")
        self.search_field_PN.clear()
        self.search_field_PN.send_keys("rcanalytics1")
        self.driver.find_element_by_id("login").click()

    """test_same_age_category_error function is used to check the alert response on entering same same age category"""
    def test_same_age_category_error(self):
        j=10
        self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//SameAgeCategory.csv", "r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for i in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[i - 2])
                    break
        self.driver.implicitly_wait(30)
        self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.eror.get_attribute('title')
        self.assertEqual(self.error_msg, 'Age Category is duplicated')
        logging.getLogger().info("The test case for the age category duplicate is passed!!!")
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.implicitly_wait(30)
        self.driver.quit()

    """test_no_age_category_error function is used to check the alert response on not entering age category"""
    def test_no_age_category(self):
        j = 10
        self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
        self.old_line.clear()
        self.old_line.send_keys(366)
        self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//NoAgeCategory.csv", "r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for i in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[i - 2])
                    break
        self.driver.implicitly_wait(30)
        self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.eror.get_attribute('title')
        self.assertEqual(self.error_msg, 'Age Category field is required')
        logging.getLogger().info("The test case for the no age category is passed!!!")
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.implicitly_wait(30)
        self.driver.quit()

    """test_same_age_overlap_category error function is used to check the alert response on entering an overlapping age category"""
    def test_age_overlap_category(self):
        j = 10
        self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
        self.old_line.clear()
        self.old_line.send_keys(366)
        self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//AgeOverlapCategory.csv", "r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for i in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[i - 2])
                    break
        self.driver.implicitly_wait(30)
        self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.eror.get_attribute('title')
        self.assertEqual(self.error_msg, 'There is an overlap between this age category and 0-30')
        logging.getLogger().info("The test case for the overlap age category is passed!!!")
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.implicitly_wait(30)
        self.driver.quit()

    """test_same_age_gap_category error function is used to check the alert response on entering gap in between age category"""
    def test_age_gap_category(self):
        j = 10
        self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
        self.old_line.clear()
        self.old_line.send_keys(366)
        self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//AgeGapCategory.csv", "r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for i in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[i - 2])
                    break
        self.driver.implicitly_wait(30)
        self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.eror.get_attribute('title')
        self.assertEqual(self.error_msg, 'There is a gap between this age category and 366+')
        logging.getLogger().info("The test case for the age gap category is passed!!!")
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.implicitly_wait(30)
        self.driver.quit()

    """test_begin_age_greater_category error function is used to check the alert response if the begin age is greater"""
    def test_begin_age_greater_category(self):
        j = 10
        self.old_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[5]/input')
        self.old_line.clear()
        self.old_line.send_keys(366)
        self.new_line = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//BeginAgeGreater.csv", "r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for i in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(i) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[i - 2])
                    break
        self.driver.implicitly_wait(30)
        self.eror = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.eror.get_attribute('title')
        self.assertEqual(self.error_msg, 'Begin Age should be less than End Age')
        logging.getLogger().info("The test case for the begin age greater than end age is passed!!!")
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.driver.implicitly_wait(30)
        self.driver.quit()

    """Deleting and adding a new row on the front end"""
    def test_checking_save_new_row(self):
        j = 9
        self.xpath_Prefix = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
        self.xpath_Suffix = ']/td[6]/div'
        for self.iter in range(1, 9):
            self.first_line_xpath = self.xpath_Prefix + str(self.iter) + self.xpath_Suffix
            if self.iter == 1:
                self.del_button = self.driver.find_element_by_xpath(self.first_line_xpath)
                self.actions = ActionChains(self.driver)
                self.actions.click(self.del_button).perform()
        self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.save_page).perform()
        time.sleep(10)
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        self.new_line = self.driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[8]/td[7]/div')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.new_line).perform()
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Age_categories//NewLineCreation.csv","r") as read_file:
            for line in read_file:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    self.xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
                    self.xpath_1 = ']/td['
                    self.xpath_2 = self.xpath_0 + str(j) + self.xpath_1
                    self.xpath_3 = ']/input'
                    for self.iteration in range(2, 6):
                        self.o_xpath = self.xpath_2 + str(self.iteration) + self.xpath_3
                        self.search_field_UN = self.driver.find_element_by_xpath(self.o_xpath)
                        self.search_field_UN.clear()
                        self.search_field_UN.send_keys(l1[self.iteration - 2])
                    break
            self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
            self.actions = ActionChains(self.driver)
            self.actions.click(self.save_page).perform()
            logging.getLogger().info("Deleted and entered a new row")
            self.driver.implicitly_wait(30)
            self.driver.close()

    def test_validating_entered_value(self):
        validate = 2
        self.keys_validation = ["1", "Not Aged", "-9,999", "-1"]
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
        for self.increment in self.keys_validation:
            self.xpath0 = '//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[1]/td['
            self.xpath1 = validate
            self.xpath2 = ']/input'
            self.xpath_validate = self.driver.find_element_by_xpath(self.xpath0 + str(self.xpath1) + self.xpath2).get_attribute("value")
            self.assertEqual(self.increment, self.xpath_validate)
            validate = validate + 1
        logging.getLogger().info("Data is validated after the save!!!")
        self.driver.implicitly_wait(30)
        self.driver.close()

"""Initializes the main class and get the text execution .xml report to be fed to Jenkins."""
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))