import xmlrunner
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.chrome.options import Options
import datetime


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class ChopsFE(unittest.TestCase):

    def setUp(self):
        self.data = []
        self.date_today = []
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=800x600")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.xpath_0 = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div/div/div/ul/li[2]/div/div/div/ul/li['
        self.xpath_1 = ']/div/div/div/div[1]/span/span/b'
        self.xpath_inner_0 = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div/div/div/ul/li[2]/div/div/div/ul/li['
        self.xpath_inner_1 = ']/div/div/div/div[2]/ul/li[1]/div/div/span/span/span[2]/span'
        self.s1 = 'SUCCEEDED'
        self.today = datetime.datetime.today()

    def test_front_end(self):
        self.driver.get("https://sl044390:sl044390@associates.sandboxcerner.com/accounts/login//auto")
        self.driver.implicitly_wait(10)
        self.search_field_UN = self.driver.find_element_by_xpath('//*[@id="authUsername"]')
        self.search_field_UN.clear()
        self.search_field_UN.send_keys('SC057441')
        self.search_field_PWD = self.driver.find_element_by_xpath('//*[@id="authPassword"]')
        self.search_field_PWD.clear()
        self.search_field_PWD.send_keys('Pavan!1251')
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        self.driver.implicitly_wait(30)
        self.refresh = self.driver.get("https://chops.us.staginghealtheintent.net/#/")
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/label').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div/div/div/div[1]/span/span/b').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div/div/div/ul/li[2]/div/div/div/div[1]/span/span/b').click()
        for value in range(12, 13):
            self.driver.find_elements_by_xpath(self.xpath_0 + str(value) + self.xpath_1)[0].click()
            recentdate = self.driver.find_element_by_xpath(self.xpath_inner_0 + str(value) + self.xpath_inner_1)
            logger.info(recentdate.text)
            self.date_today = recentdate.text.split(" ")
            if self.date_today[0] == self.today.strftime("%m/%d/%Y"):
                actions = ActionChains(self.driver)
                actions.click(recentdate).perform()
                status = self.driver.find_elements_by_class_name('ng-binding')
                for iter in status:
                    self.data.append(iter.text)
                logger.info(self.data)
                self.assertIn(self.s1, self.data)
                logger.info("Pipeline Passed sucessfully.")
            else:
                logger.info("pipeline didn't run")
                self.assertEqual(self.date_today[0],self.today.strftime("%m/%d/%Y"))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))