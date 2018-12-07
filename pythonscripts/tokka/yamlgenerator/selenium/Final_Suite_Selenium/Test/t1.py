from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://app.analyticsquerytool.devcernerpophealth.com/')
driver.find_element_by_xpath('//*[@id="principal"]').send_keys("Abraham_Edward")
driver.find_element_by_xpath('//*[@id="invokeLogIn"]').click()
driver.get('https://app.analytics.devcernerpophealth.com/queries')
driver.find_element_by_xpath('//*[@id="sql-input"]/textarea').send_keys("select * from app_il_cdh5.ph_f_affiliation LIMIT 50;")