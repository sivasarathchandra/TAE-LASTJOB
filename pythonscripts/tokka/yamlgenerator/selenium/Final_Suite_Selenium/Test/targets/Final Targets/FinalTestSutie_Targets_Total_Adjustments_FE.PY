import xmlrunner
import unittest
from ParametrizedTestCase import ParametrizedTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Facility_values import FacilityValues
from logging_FE import loggingFE

"""This is the class that has the exact code that assembles all the test cases."""
class TotalAdjustmentsFE(ParametrizedTestCase):
    """The setup is used to initialize all the variables used."""
    def setUp(self):
        self.driver = self.driverParam
        self.driver.get(self.urlParam)
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Changes you made may not be saved.')
            alert = self.driver.switch_to.alert
            alert.accept()
            loggingFE.info("alert accepted")
        except TimeoutException:
            loggingFE.info("no alert")
        self.driver.implicitly_wait(30)
        self.error_1 = 'Target should be greater than or equal to Bottom Zone'
        self.error_2 = 'Target should be less than or equal to Top Zone'
        self.error_3 = 'Top Zone should be greater than or equal to Bottom Zone'
        self.last_key = self.urlParam.split('/')
        self.length_URL = len(self.last_key)
        self.urlName = self.last_key[self.length_URL - 1]
        self.defaultsXpath = ['//*[@id="target"]', '//*[@id="bottom_zone"]', '//*[@id="top_zone"]']
    """This is the test case that is used to check the number of sub url's that are under one tab."""
    def test_1_validate_tabs(self):
        loggingFE.info("Checking for the number of sub-tabs below the main code")
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
        loggingFE.info("the list of values still remain the same.")

    """checking for the targets less than bottom zone error."""
    def test_2_target_less_than_bottom_zone(self):
        loggingFE.info("Checking for the error target less than bottom zone")
        innovation_data = [120000, 200000, 500000]
        default_data = [150000, 350000, 650000]
        alert_facility = FacilityValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=innovation_data)
        self.assertEqual(alert_facility, self.error_1)
        alert_default = FacilityValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_1)
        self.driver.save_screenshot(self.urlName+"_step1_target_less_than_bottom_zone.jpg")

    """Checking for the target greater than top zone error."""
    def test_3_target_greater_than_top_zone(self):
        loggingFE.info("checking for the error target greater than top zone")
        innovation_data = [620000, 200000, 500000]
        default_data = [750000, 350000, 650000]
        alert_facility = FacilityValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=innovation_data)
        self.assertEqual(alert_facility, self.error_2)
        alert_default = FacilityValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_2)
        self.driver.save_screenshot(self.urlName + "_step2_target_greater_than_top_zone.jpg")

    """Checking for the bottom zone greater than top zone error."""
    def test_4_bottom_zone_greater_than_top_zone(self):
        loggingFE.info("checking for the error bottom zone greater than top zone.")
        innovation_data = ['', 700000, 500000]
        default_data = ['', 750000, 650000]
        alert_facility = FacilityValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=innovation_data)
        self.assertEqual(alert_facility, self.error_3)
        alert_default = FacilityValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_3)
        self.driver.save_screenshot(self.urlName + "_step3_bottom_zone_greater_than_top_zone.jpg")

    """put some values in the respective divs and then extract them back to validate the same"""
    def test_5_put_default_values(self):
        loggingFE.info("enter values in the respective field and save and retrieve them to validate them")
        innovation_data = ['', '', '']
        default_data = [200000, 100000, 400000]
        facility_existing_values = FacilityValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        default_existing_values = FacilityValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        alert_facility = FacilityValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=innovation_data)
        alert_default = FacilityValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        loggingFE.info("The value at both facility and default levels are placed.")
        facility_new_values = FacilityValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        default_new_values = FacilityValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.assertEqual(facility_new_values, default_new_values)
        loggingFE.info("The values are same as the input")
        self.driver.save_screenshot(self.urlName + "_step4_put_default_values.jpg")
        alert_facility = FacilityValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_existing_values)
        alert_default = FacilityValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_existing_values)
        loggingFE.info("Finished the reverting task as well.")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))