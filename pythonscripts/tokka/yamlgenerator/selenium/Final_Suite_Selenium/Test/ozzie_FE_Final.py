import xmlrunner
import logging
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import base64
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.chrome.options import Options
import datetime


logger = logging.getLogger()
logger.level = logging.ERROR
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
        self.xpath_0 = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/div/div/div/ul/li[1]/div/div/div/ul/li['
        self.xpath_1 = ']/div/div/div/div[1]/span/span/b'
        self.xpath_inner_0 = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li/div/div/div/ul/li[1]/div/div/div/ul/li['
        self.xpath_inner_1 = ']/div/div/div/div[2]/ul/li[1]/div/div/span/span/span[2]/span'
        self.s1 = 'SUCCEEDED'
        self.today = datetime.datetime.today()
        self.workflowname = command_line_param
        self.username = base64.b64encode(bytes(username,"utf-8"))
        self.username = base64.b64decode(self.username).decode("utf-8")
        self.password = base64.b64encode(bytes(password, "utf-8"))
        self.password = base64.b64decode(self.password).decode("utf-8")

    def test_front_end(self):
        self.driver.get("https://sl044390:sl044390@associates.sandboxcerner.com/accounts/login//auto")
        self.driver.implicitly_wait(10)
        self.search_field_UN = self.driver.find_element_by_xpath('//*[@id="authUsername"]')
        self.search_field_UN.clear()
        self.search_field_UN.send_keys(self.username)
        self.search_field_PWD = self.driver.find_element_by_xpath('//*[@id="authPassword"]')
        self.search_field_PWD.clear()
        self.search_field_PWD.send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        self.driver.implicitly_wait(30)
        self.refresh = self.driver.get("https://chops.us.staginghealtheintent.net/#/")
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/label').click()
            self.driver.find_element_by_xpath('//div[1]/span/span/b[contains(text(),"Clients")]').click()
            self.driver.find_element_by_xpath('//b[contains(text(),"15stpdep")]').click()
            self.driver.find_element_by_xpath("//b[contains(text(),'"+self.workflowname+"')]").click()
            self.today = self.today.strftime("%m/%d/%Y")
            final_check = self.driver.find_element_by_xpath("//span[contains(text(),'" + self.today + "')]").click()
            if final_check != None:
                self.assertEqual(self.driver.find_element_by_xpath("//td[2]/span[contains(text(),SUCCEEDED)]").text,"SUCCEEDED")
                logger.info("Pipeline ran sucessfully.")
        except NoSuchElementException:
            self.fail(msg="There is no div to find")
            # self.assertEqual(1,0)

if __name__ == '__main__':
    command_line_param = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    del sys.argv[1:]
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=".//html/body/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/labelpython_unittests_xml"))