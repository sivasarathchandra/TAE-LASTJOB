from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
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
time.sleep(20)
driver.find_element_by_xpath('//*[@id="expand-toggle"]').click()
print("clicked on the expand option.")

# divs = driver.find_element_by_class_name('main-content').get_attribute("outerHTML")
tokka =driver.find_element_by_css_selector('#tableau_base_widget_ParameterControl_0 > div > div.PCContent').click()
# driver.find_element_by_xpath('//*[@id="tableau_base_widget_ParameterControl_0"]/div/div[2]/span/div[1]').get_attribute("value")
print(tokka)