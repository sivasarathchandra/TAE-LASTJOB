import xmlrunner
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.chrome.options import Options
from datetime import datetime


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://sl044390:sl044390@associates.sandboxcerner.com/accounts/login//auto")
driver.implicitly_wait(10)
search_field_UN = driver.find_element_by_xpath('//*[@id="authUsername"]')
search_field_UN.clear()
search_field_UN.send_keys('SD056953')
search_field_PWD = driver.find_element_by_xpath('//*[@id="authPassword"]')
search_field_PWD.clear()
search_field_PWD.send_keys('$ds@0502')
driver.find_element_by_xpath('//*[@id="login"]').click()
driver.implicitly_wait(30)
driver.get('https://15stpdep.analytics.staginghealtheintent.com/reports/4297')
driver.find_element_by_xpath('//*[@id="global-wrapper"]/div[1]/main/div/div/article/div/div/ul/li[1]/a').click()
driver.implicitly_wait(30)
driver.get('https://15stpdep.analytics.staginghealtheintent.com/queries')