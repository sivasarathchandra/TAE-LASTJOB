from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

i=0
lst1 = ['Month to Date','Quarter to Date','Year to Date','Last 2 Months','Last 13 Months','Last 2 Years','All Data','Custom']
driver = webdriver.Chrome()
driver.get("https://sl044390:sl044390@associates.sandboxcerner.com/accounts/login//auto")
driver.implicitly_wait(10)
driver.maximize_window()
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
iFrame = driver.find_element_by_xpath("//iframe[@style='display: block; width: 1300px; height: 1077px; visibility: visible;']")
driver.switch_to.frame(iFrame)
# driver.find_element_by_xpath('//*[@id="centeringContainer"]/div[2]/div[1]/div[1]/div[5]/span[2]').click()
# dropdown = driver.find_element_by_xpath('//*[@id="tableau_base_widget_ParameterControl_0"]/div/div[2]/span/div[2]')
dropdown=driver.find_element_by_xpath('//*[@id="tableau_base_widget_ParameterControl_0"]/div/div[1]/h3/span/div/span')
print(dropdown.text)
d1 = driver.find_element_by_xpath('//*[@id="tableau_base_widget_ParameterControl_0"]/div/div[2]/span/div[1]')
print(d1.text)
d1.click()
time.sleep(5)
# print(d1)
# d1.get_attribute("outerHTML")
# d_name = driver.find_element_by_xpath('//div[@class="tabMenuContent"]//div[@class="ttabMenuItem tabMenuItemComboDropdownTheme tab-ctrl-formatted-text tabMenuMenuItem"]').get_attribute("id")
# print(d_name)
d2 = driver.find_elements_by_xpath('//div[@class="tabMenuContent"]//div[@class="tabMenuItemNameArea"]//span[@class="tabMenuItemName"]')
actions = ActionChains(driver)
# actions.move_to_element(d2)
for d in d2:
    a1 = actions.move_to_element(d)
    if d.text in lst1:
        print("entered if")
        d1 = driver.find_element_by_xpath('//*[@id="tableau_base_widget_ParameterControl_0"]/div/div[2]/span/div[1]')
        d1.click()
        print(d.text)
    a1.send_keys(Keys.ARROW_DOWN+Keys.ENTER).perform()
    time.sleep(10)
    # iFrame = driver.find_element_by_xpath("//iframe[@style='display: block; width: 1300px; height: 1077px; visibility: visible;']")
    # driver.switch_to.frame(iFrame)
# a1.send_keys(u'\ue015').perform()
# d2 = driver.find_element_by_xpath('//div[@class="tabMenuContent"]//div[@class="tabMenuItemNameArea"]//span[@class="tabMenuItemName"]')
# print(d2.text)
# actions.move_to_element(d2).click()
# time.sleep(10)
# a1.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
# time.sleep(10)
# a1.send_keys(Keys.ENTER)
# time.sleep(10)
# driver.implicitly_wait(30)
# for d in d2:
#     print(d.text)
#     driver.implicitly_wait(30)
# d3=driver.find_element_by_xpath('//*[@id="tab-menuItem1"]/div/span')
# actions = ActionChains(driver)
# actions.move_to_element(d3)
# for i in range(0,len(d2)):
#     actions.key_down(Keys.ARROW_DOWN + Keys.ENTER)
#     driver.implicitly_wait(30)
#     i=i+1
# driver.close()
