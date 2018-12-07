from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/total_adjustments")
search_field_UN = driver.find_element_by_id("authUsername")
search_field_UN.clear()
search_field_UN.send_keys("revcycleanalytics@gmail.com")
search_field_PN = driver.find_element_by_id("authPassword")
search_field_PN.clear()
search_field_PN.send_keys("rcanalytics1")
driver.find_element_by_id("login").click()
time.sleep(10)
#driver.implicitly_wait(30)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(30)
final_val = driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div/div/pagination/nav/span[3]/a[1]")
actions = ActionChains(driver)
actions.click(final_val).perform()
driver.implicitly_wait(30)
j = 3
with open("C://Users//SC057441//Desktop//Any//pythonscripts//tokka//yamlgenerator//selenium//Final_Suite_Selenium//Resource//Targets//Targets_Adding.csv", "r") as readfile:
    for line in readfile:
        if re.match(r"^\d+.*$", line):
            l1 = line.split(',')
            for data in l1:
                xpath0='//*[@id="form-update"]/div/div/div/div/div/table/tbody/tr[9]/td['
                xpath1=']/input'
                xpath_final = xpath0 + str(j) + xpath1
                j = j+1
                search_field_innovations = driver.find_element_by_xpath(xpath_final)
                search_field_innovations.clear()
                search_field_innovations.send_keys(data)
save_page = driver.find_element_by_xpath('//*[@id="save_config"]')
actions = ActionChains(driver)
actions.click(save_page).perform()

#driver.close()
