import xmlrunner
import logging
import unittest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class ChopsFE(unittest.TestCase):

    # def unc(self):
    #     matchFound = True
    #     while matchFound:
    #         try:
    #             facilityElement = self.browser.find_element_by_xpath("//td[contains(text(),'" + facilityName + "')]")
    #             if facilityElement != None:
    #                 facilityInputs = self.browser.find_elements_by_xpath(
    #                     "//td[contains(text(),'" + facilityName + "')]/following-sibling::td/input")
    #                 for incr in range(0, 3):
    #                     val = facilityInputs[incr].get_attribute('value')
    #                     self.facility_existing_values.append(val)
    #             break
    #         except NoSuchElementException:
    #             self.browser.find_element_by_xpath(click_xpath).click()
    #             pageNum = pageNum + 1
    #     loggingFE.logger.info("Returing the existing values")
    #     return self.facility_existing_values, pageNum

    def setUp(self):
        self.data = []
        self.date_today = []
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=800x600")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.xpath_0 = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/div/div/div/ul/li[2]/div/div/div/ul/li['
        self.xpath_1 = ']/div/div/div/div[1]/span/span/b'
        self.xpath_inner_0 = self.xpath_0
        self.xpath_inner_1 = ']/div/div/div/div[3]/ul/li/div/div/span/span/span[2]'
        self.s1 = 'SUCCEEDED'

    def test_front_end(self):
        try_num = 0
        self.driver.get("https://sl044390:sl044390@associates.devcerner.com/accounts/login//auto")
        self.driver.implicitly_wait(10)
        self.search_field_UN = self.driver.find_element_by_xpath('//*[@id="authUsername"]')
        self.search_field_UN.clear()
        self.search_field_UN.send_keys('SC057441')
        self.search_field_PWD = self.driver.find_element_by_xpath('//*[@id="authPassword"]')
        self.search_field_PWD.clear()
        self.search_field_PWD.send_keys('Pavan!1251')
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        self.driver.implicitly_wait(30)
        self.refresh = self.driver.get("https://chops.us.devhealtheintent.net/#/")
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/label').click()
        print("I clicked on the number")
        matchfound = True
        while matchfound:
            if try_num == 6:
                self.driver.close()
                break
            else:
                try:
                    self.div_open = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/div/div/div/div[1]/span/span/b')
                    if self.div_open != None:
                        self.div_open.click()
                        matchfound = False
                except NoSuchElementException:
                    self.refresh = self.driver.get("https://chops.us.devhealtheintent.net/#/")
                    self.driver.refresh()
                    self.driver.implicitly_wait(30)
                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/label').click()
                    try_num = try_num + 1
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/div/div/div/ul/li[2]/div/div/div/div[1]/span/span/b').click()
        for value in range(20, 21):
            self.driver.find_elements_by_xpath(self.xpath_0 + str(value) + self.xpath_1)[0].click()
            recentdate = self.driver.find_element_by_xpath(self.xpath_inner_0 + str(value) + self.xpath_inner_1).click()
            time1 = datetime.now()
            logger.info(time1)
            self.driver.implicitly_wait(30)
            time.sleep(10)
            tokka = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/button[1]/span').click()
            time.sleep(10)
            tokka = self.driver.find_element_by_xpath('//div[@class="modal fade  in"]//div[@class="modal-dialog ng-scope"]//div[@class="modal-content"]')
            tokka1 = tokka.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div[1]/button').click()
            print(tokka)
            print(tokka1)
            facilityElement = tokka.find_element_by_xpath('//table[@class="table table-striped"]//tr[@class="ng-scope"]//input[@ng-model="property.name"][@value=""]')
            facilityElement.send_keys("Cerner")
            facilityValue = tokka.find_element_by_xpath('//table[@class="table table-striped"]//tr[@class="ng-scope"]//input[@ng-model="property.value"][@value=""]')
            facilityValue.send_keys("Cerner")
            time.sleep(10)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
