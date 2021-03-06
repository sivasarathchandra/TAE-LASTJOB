import xmlrunner
import unittest
from ParametrizedTestCase import ParametrizedTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from GetPutValues import GetPutValues
from logging_FE import loggingFE
from ErrorValidationClass import ErrorValidationClass

"""This is the test class where all the testcases resides in."""
class AdjustmentsFE(ParametrizedTestCase):

    facility_existing_values = []
    default_existing_values = []
    pageNum = 0

    """The setup is used to initialize all the variables used."""
    def setUp(self):
        self.driver = self.driverParam
        self.driver.get(self.urlParam)
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Changes you made may not be saved.')
            alert = self.driver.switch_to.alert
            alert.accept()
            loggingFE.logger.info("alert accepted")
        except TimeoutException:
            loggingFE.logger.info("no alert")
        self.driver.implicitly_wait(30)
        self.last_key = self.urlParam.split('/')
        self.length_URL = len(self.last_key)
        self.urlName = self.last_key[self.length_URL - 1]
        self.defaultsXpath = ['//*[@id="target"]', '//*[@id="bottom_zone"]', '//*[@id="top_zone"]']
        if 'dev' in self.urlParam:
            self.click_xpath = '//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]'
        else:
            self.click_xpath = '//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]'

    """This testcase will check the number of sub-tabs under the main tab."""
    def test_1_validate_tabs(self):
        loggingFE.logger.info("Checking for the number of sub-tabs below the main code")
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
        self.assertEqual(counter, 7)
        self.assertEqual(final_items_list, self.urlListParam)
        self.driver.save_screenshot(self.urlName + "_step_1_validate_tabs.jpg")

    """This testcase will fetch the existing values and store them in class level variables."""
    def test_2_fetch_existing_values(self):
        loggingFE.logger.info("extracting the data from the current page for the first time")
        facility_return_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        AdjustmentsFE.facility_existing_values = facility_return_values[0]
        AdjustmentsFE.pageNum = facility_return_values[1]
        AdjustmentsFE.default_existing_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        print('Test 2 print')
        print(AdjustmentsFE.facility_existing_values)
        print(AdjustmentsFE.pageNum)
        print(AdjustmentsFE.default_existing_values)
        self.driver.save_screenshot(self.urlName + "_step_2_fetch_existing_values.jpg")

    """This testcase will check for an error when the target less than bottom zone"""
    def test_3_target_less_than_bottom_zone(self):
        test_result = ErrorValidationClass.target_less_than_bottom_zone(self, driver=self.driver, facilityName=self.facility_name, clickXpath=self.click_xpath, pageNum=AdjustmentsFE.pageNum, defaultsXpath=self.defaultsXpath)
        self.assertEqual(test_result, 1)
        self.driver.save_screenshot(self.urlName+"_step_3_target_less_than_bottom_zone.jpg")

    """This testcase will check for an error when the target is greater than top zone"""
    def test_4_target_greater_than_top_zone(self):
        test_result = ErrorValidationClass.target_greater_than_top_zone(self, driver=self.driver, facilityName=self.facility_name, clickXpath=self.click_xpath, pageNum=AdjustmentsFE.pageNum, defaultsXpath=self.defaultsXpath)
        self.assertEqual(test_result, 1)
        self.driver.save_screenshot(self.urlName + "_step_4_target_greater_than_top_zone.jpg")

    """This testcase will check for an error when the bottom zone is greater than top zone"""
    def test_5_bottom_zone_greater_than_top_zone(self):
        test_result = ErrorValidationClass.bottom_zone_greater_than_top_zone(self, driver=self.driver, facilityName=self.facility_name, clickXpath=self.click_xpath, pageNum=AdjustmentsFE.pageNum, defaultsXpath=self.defaultsXpath)
        self.assertEqual(test_result, 1)
        self.driver.save_screenshot(self.urlName + "_step_5_bottom_zone_greater_than_top_zone.jpg")

    """This testcase will validate if the valid values entered at the facility level is saved correctly.
    This case will fail as the setup on the page is not working as intended."""
    def test_6_only_facility_values(self):
        facility_data = [500000, 200000, 900000]
        default_data = ['', '', '']
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        facility_return_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        facility_new_values = facility_return_values[0]
        formatted_facility_data = []
        for incr in facility_data:
            if '$' in facility_new_values[0]:
                formatted_facility_data.append('$ {:,.2f}'.format(incr/100) )
            else:
                formatted_facility_data.append(incr/10000)
        self.assertEqual(formatted_facility_data, facility_new_values)
        self.driver.save_screenshot(self.urlName + "_step_6_only_facility_values.jpg")

    """This testcase will validate if the facility values added in the previous testcase is overridden when the default values are added."""
    def test_7_both_facility_and_default_values(self):
        loggingFE.logger.info("Checking if the facility values are over ridden with the default level value.")
        default_data = [300025, 200069, 500036]
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        facility_return_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        facility_new_values = facility_return_values[0]
        default_new_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.assertNotEqual(facility_new_values, default_new_values)
        self.driver.save_screenshot(self.urlName + "_step_7_both_facility_and_default_values.jpg")

    """This testcase will validate if the facility values is overridden with the default values when the facility values is saved as blank."""
    def test_8_only_default_values(self):
        loggingFE.logger.info("checking for the facility to get overridden with the default numbers.")
        facility_data = ['', '', '']
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        facility_return_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        facility_new_values = facility_return_values[0]
        default_new_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.assertEqual(facility_new_values, default_new_values)
        self.driver.save_screenshot(self.urlName + "_step_8_only_default_values.jpg")

    """This testcase will revert the data back to the existing data that was fetched in test 2 and then log out."""
    def test_9_revert_to_old_values(self):
        facility_data = []
        default_data = []
        for incr in range(0,3):
            if '$' in AdjustmentsFE.facility_existing_values[0]:
                facility_data.append(AdjustmentsFE.facility_existing_values[incr].replace('$ ','').replace(',','').replace('.',''))
                default_data.append(AdjustmentsFE.default_existing_values[incr].replace('$ ', '').replace(',','').replace('.',''))
            elif '' in AdjustmentsFE.facility_existing_values:
                facility_data.append(AdjustmentsFE.facility_existing_values[incr])
                default_data.append(AdjustmentsFE.default_existing_values[incr])
            else:
                facility_data.append(int(float(AdjustmentsFE.facility_existing_values[incr]) * 10000))
                default_data.append(int(float(AdjustmentsFE.default_existing_values[incr]) * 10000))
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data, click_xpath = self.click_xpath, pageNum = AdjustmentsFE.pageNum)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.driver.save_screenshot(self.urlName + "_step_9_only_default_values.jpg")
    loggingFE.logger.info("all are reverted back to the original.")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))