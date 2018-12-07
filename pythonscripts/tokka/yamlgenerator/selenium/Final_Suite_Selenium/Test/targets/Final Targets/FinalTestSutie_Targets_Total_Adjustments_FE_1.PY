import xmlrunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from ParametrizedTestCase import ParametrizedTestCase
from loginPage import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from GetPutValues import GetPutValues

class TotalAdjustmentsFE(ParametrizedTestCase):

    facility_existing_values = []
    default_existing_values = []

    def setUp(self):
        self.driver = self.driverParam
        self.driver.get(self.urlParam)
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Changes you made may not be saved.')
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        self.driver.implicitly_wait(30)
        self.error_1 = 'Target should be greater than or equal to Bottom Zone'
        self.error_2 = 'Target should be less than or equal to Top Zone'
        self.error_3 = 'Top Zone should be greater than or equal to Bottom Zone'
        self.last_key = self.urlParam.split('/')
        self.length_URL = len(self.last_key)
        self.urlName = self.last_key[self.length_URL - 1]
        self.defaultsXpath = ['//*[@id="target"]', '//*[@id="bottom_zone"]', '//*[@id="top_zone"]']

    def test_1_validate_tabs(self):
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

    def test_2_fetch_existing_values(self):
        TotalAdjustmentsFE.facility_existing_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        TotalAdjustmentsFE.default_existing_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.driver.save_screenshot(self.urlName + "_step_2_fetch_existing_values.jpg")

    def test_3_target_less_than_bottom_zone(self):
        facility_data = [120000, 200000, 500000]
        default_data = [150000, 350000, 650000]
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data)
        self.assertEqual(alert_facility, self.error_1)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_1)
        self.driver.save_screenshot(self.urlName+"_step_3_target_less_than_bottom_zone.jpg")

    def test_4_target_greater_than_top_zone(self):
        facility_data = [621234, 201234, 501234]
        default_data = [751234, 351234, 651234]
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data)
        self.assertEqual(alert_facility, self.error_2)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_2)
        self.driver.save_screenshot(self.urlName + "_step_4_target_greater_than_top_zone.jpg")

    def test_5_bottom_zone_greater_than_top_zone(self):
        facility_data = ['', 700000, 500000]
        default_data = ['', 750000, 650000]
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data)
        self.assertEqual(alert_facility, self.error_3)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.assertEqual(alert_default, self.error_3)
        self.driver.save_screenshot(self.urlName + "_step_5_bottom_zone_greater_than_top_zone.jpg")

    def test_6_only_facility_values(self):
        facility_data = [500000, 200000, 900000]
        default_data = ['', '', '']
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        facility_new_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        formatted_facility_data = []
        for i in facility_data:
            if '$' in facility_new_values[0]:
                formatted_facility_data.append('$ {:,.2f}'.format(i/100) )
            else:
                formatted_facility_data.append(i/10000)
        self.assertEqual(formatted_facility_data, facility_new_values)
        self.driver.save_screenshot(self.urlName + "_step_6_only_facility_values.jpg")

    def test_7_both_facility_and_default_values(self):
        default_data = [300025, 200069, 500036]
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath,defaultValues=default_data)
        facility_new_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        default_new_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.assertNotEqual(facility_new_values, default_new_values)
        self.driver.save_screenshot(self.urlName + "_step_7_both_facility_and_default_values.jpg")

    def test_8_only_default_values(self):
        facility_data = ['', '', '']
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name,facilityValues=facility_data)
        facility_new_values = GetPutValues.getFacilityValues(self, driver=self.driver, facilityName=self.facility_name)
        default_new_values = GetPutValues.getDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath)
        self.assertEqual(facility_new_values, default_new_values)
        self.driver.save_screenshot(self.urlName + "_step_8_only_default_values.jpg")

    def test_9_revert_to_old_values(self):
        facility_data = []
        default_data = []
        for iter in range(0,3):
            facility_data.append(TotalAdjustmentsFE.facility_existing_values[iter].replace('$ ','').replace(',','').replace('.',''))
            default_data.append(TotalAdjustmentsFE.default_existing_values[iter].replace('$ ', '').replace(',','').replace('.',''))
        alert_facility = GetPutValues.putFacilityValues(self, driver=self.driver, facilityName=self.facility_name, facilityValues=facility_data)
        alert_default = GetPutValues.putDefaultValues(self, driver=self.driver, defaultXpaths=self.defaultsXpath, defaultValues=default_data)
        self.driver.save_screenshot(self.urlName + "_step_9_only_default_values.jpg")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))