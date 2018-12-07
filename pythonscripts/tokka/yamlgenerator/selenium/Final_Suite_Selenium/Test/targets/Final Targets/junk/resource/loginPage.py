from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from resource.logging_FE import loggingFE

"""This is class is mainly used only for a headless loging."""
class login():
    def login_dev():
        loggingFE.logger.info("logging into dev")
        browser = webdriver.Chrome()
        browser.implicitly_wait(30)
        browser.maximize_window()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=800x600")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get("https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle")
        browser.implicitly_wait(30)
        search_field_UN = browser.find_element_by_xpath('//*[@id="principal"]')
        search_field_UN.clear()
        search_field_UN.send_keys("RCADMIN")
        browser.find_element_by_xpath('//*[@id="invokeLogIn"]').click()
        browser.implicitly_wait(30)
        return browser
    def login_staging():
        loggingFE.logger.info("logging into staging")
        browser = webdriver.Chrome()
        browser.implicitly_wait(30)
        browser.maximize_window()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=800x600")
        # browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle")
        browser.implicitly_wait(30)
        search_field_UN = browser.find_element_by_id("authUsername")
        search_field_UN.clear()
        search_field_UN.send_keys("revcycleanalytics@gmail.com")
        search_field_PN = browser.find_element_by_id("authPassword")
        search_field_PN.clear()
        search_field_PN.send_keys("rcanalytics1")
        browser.find_element_by_id("login").click()
        browser.implicitly_wait(30)
        return browser