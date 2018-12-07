import xmlrunner
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
import sys


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class TotalAdjustmentsFE(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=800x600")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/total_adjustments")
        self.search_field_UN = self.driver.find_element_by_xpath('//*[@id="authUsername"]')
        self.search_field_UN.clear()
        self.search_field_UN.send_keys("revcycleanalytics@gmail.com")
        self.search_field_PN = self.driver.find_element_by_id("authPassword")
        self.search_field_PN.clear()
        self.search_field_PN.send_keys("rcanalytics1")
        self.driver.find_element_by_id("login").click()
        self.driver.implicitly_wait(30)
        self.final_val = self.driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div/div/pagination/nav/span[3]/a[1]")
        self.actions = ActionChains(self.driver)
        self.actions.click(self.final_val).perform()

    def test_add_details_innovations(self):
        j = 3
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Targets//Targets_Adding.csv","r") as readfile:
            for line in readfile:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    for self.data in l1:
                        self.xpath0 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
                        self.xpath1 = ']/input'
                        self.xpath_final = self.xpath0 + str(j) + self.xpath1
                        j = j + 1
                        self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final)
                        self.search_field_innovations.clear()
                        self.search_field_innovations.send_keys(self.data)
                    self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
                    self.actions = ActionChains(self.driver)
                    self.actions.click(self.save_page).perform()

    def test_validate_revert_back(self):
        already_data = ['$ 8,002.00']
        for validate in already_data:
            self.xpath0 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
            self.xpath1 = ']/input'
            self.xpath_validate = self.driver.find_element_by_xpath(self.xpath0 + str(3) + self.xpath1).get_attribute("value")
            self.assertEqual(validate, self.xpath_validate)
        logging.getLogger().info("Data is validated after the save!!!")
        logging.getLogger().info("Now reverting back to original")
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Targets//Revert_Back.csv","r") as readfile:
            j = 3
            for line in readfile:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    for self.data in l1:
                        self.xpath0 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
                        self.xpath1 = ']/input'
                        self.xpath_final = self.xpath0 + str(j) + self.xpath1
                        j = j + 1
                        self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final)
                        self.search_field_innovations.clear()
                        self.search_field_innovations.send_keys(self.data)
                    self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
                    self.actions = ActionChains(self.driver)
                    self.actions.click(self.save_page).perform()

    def test_bottomzone_greater_than_equal_target(self):
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Targets//bottomzone_greater_than_equal_target.csv","r") as readfile:
            j = 3
            for line in readfile:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    for self.data in l1:
                        self.xpath0 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
                        self.xpath1 = ']/input'
                        self.xpath_final = self.xpath0 + str(j) + self.xpath1
                        j = j + 1
                        self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final)
                        self.search_field_innovations.clear()
                        self.search_field_innovations.send_keys(self.data)
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.error.get_attribute('title')
        print(self.error_msg)
        self.assertEqual(self.error_msg,'Target should be greater than or equal to Bottom Zone')

    def test_topzone_less_than_equal_target(self):
        with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Targets//topzone_less_than_equal_target.csv","r") as readfile:
            j = 3
            for line in readfile:
                if re.match(r"^\d+.*$", line):
                    l1 = line.split(',')
                    for self.data in l1:
                        self.xpath0 = '//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
                        self.xpath1 = ']/input'
                        self.xpath_final = self.xpath0 + str(j) + self.xpath1
                        j = j + 1
                        self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final)
                        self.search_field_innovations.clear()
                        self.search_field_innovations.send_keys(self.data)
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.error.get_attribute('title')
        print(self.error_msg)
        self.assertEqual(self.error_msg,'Target should be less than or equal to Top Zone')

    def test_default_target_set(self):
        data_default = ['$ 3500.00','$ 3000.00','$ 5000.00']
        self.default_target = self.driver.find_element_by_xpath('//*[@id="target"]')
        self.default_target.clear()
        self.default_target.send_keys(data_default[0])
        self.default_target = self.driver.find_element_by_xpath('//*[@id="bottom_zone"]')
        self.default_target.clear()
        self.default_target.send_keys(data_default[1])
        self.default_target = self.driver.find_element_by_xpath('//*[@id="top_zone"]')
        self.default_target.clear()
        self.default_target.send_keys(data_default[2])
        self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.save_page).perform()

    def test_default_validate_revert_data(self):
        data_default = ['$ 3,500.00', '$ 3,000.00', '$ 5,000.00']
        print("Validating the data now!!!")
        self.default_target = self.driver.find_element_by_xpath('//*[@id="target"]').get_attribute("value")
        self.assertEqual(data_default[0], self.default_target)
        self.default_target = self.driver.find_element_by_xpath('//*[@id="bottom_zone"]').get_attribute("value")
        self.assertEqual(data_default[1], self.default_target)
        self.default_target = self.driver.find_element_by_xpath('//*[@id="top_zone"]').get_attribute("value")
        self.assertEqual(data_default[2], self.default_target)
        logging.getLogger().info("Data is validated after the save!!!")
        logging.getLogger().info("Now reverting back to original")
        self.default_target = self.driver.find_element_by_xpath('//*[@id="target"]')
        self.default_target.clear()
        self.default_target.send_keys('')
        self.default_target = self.driver.find_element_by_xpath('//*[@id="bottom_zone"]')
        self.default_target.clear()
        self.default_target.send_keys('')
        self.default_target = self.driver.find_element_by_xpath('//*[@id="top_zone"]')
        self.default_target.clear()
        self.default_target.send_keys('')
        self.save_page = self.driver.find_element_by_xpath('//*[@id="save_config"]')
        self.actions = ActionChains(self.driver)
        self.actions.click(self.save_page).perform()

    def test_default_target_bottomzone_greater_than_equal_target(self):
        data_error = ['4500.00','5300.00']
        self.default_target = self.driver.find_element_by_xpath('//*[@id="target"]')
        self.default_target.clear()
        self.default_target.send_keys(data_error[0])
        self.default_target = self.driver.find_element_by_xpath('//*[@id="bottom_zone"]')
        self.default_target.clear()
        self.default_target.send_keys(data_error[1])
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.error.get_attribute('title')
        print(self.error_msg)
        self.assertEqual(self.error_msg, 'Target should be greater than or equal to Bottom Zone')

    def test_default_target_topzone_less_than_equal_target(self):
        data_error = ['4500.00', '1300.00']
        self.default_target = self.driver.find_element_by_xpath('//*[@id="target"]')
        self.default_target.clear()
        self.default_target.send_keys(data_error[0])
        self.default_target = self.driver.find_element_by_xpath('//*[@id="top_zone"]')
        self.default_target.clear()
        self.default_target.send_keys(data_error[1])
        self.error = self.driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div')
        self.driver.implicitly_wait(30)
        self.error_msg = self.error.get_attribute('title')
        print(self.error_msg)
        self.assertEqual(self.error_msg, 'Target should be less than or equal to Top Zone')

    def test_get_existing_value_default_facility(self):
        for td_iter in range(3, 6):
            self.xpath_final_td = self.xpath_innovation_1 + str(td_iter) + self.xpath_innovation_2
            self.search_field_innovations = self.driver.find_element_by_xpath(self.xpath_final_td).get_attribute()

            self.innovations_existing_value.append(self.search_field_innovations)
            self.xpath_final_td = self.xpath_default_1 + self.list_default_targets[counter] + self.xpath_default_2
            self.search_field_default = self.driver.find_element_by_xpath(self.xpath_final_td)
            self.search_field_default.clear()
            self.search_field_default.send_keys(self.default_data[counter])



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))