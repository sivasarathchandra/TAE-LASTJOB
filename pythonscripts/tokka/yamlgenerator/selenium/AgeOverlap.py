from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re

def printError():
    eror = driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[1]')
    error_msg = eror.get_attribute("innerHTML")
    driver.save_screenshot('Age_Overlap_Category.png')
    print(error_msg)
    driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
    driver.quit()

j=10
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://adventisthealthsystem.analytics.staginghealtheintent.com/explore/revenue_cycle/config/config/age_category")
driver.execute_script("window.onbeforeunload = function() {};")
search_field_UN = driver.find_element_by_id("authUsername")
search_field_UN.clear()
search_field_UN.send_keys("revcycleanalytics@gmail.com")
search_field_PN = driver.find_element_by_id("authPassword")
search_field_PN.clear()
search_field_PN.send_keys("rcanalytics1")
driver.find_element_by_id("login").click()
new_line = driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[9]/td[7]/div')
actions = ActionChains(driver)
actions.click(new_line).perform()
with open("AgeOverlapCategory.csv","r") as read_file:
    for line in read_file:
        if re.match(r"^\d+.*$", line):
            l1 = line.split(',')
            xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
            xpath_1 = ']/td['
            xpath_2 = xpath_0 + str(j) + xpath_1
            xpath_3 = ']/input'
            for i in range(2, 6):
                o_xpath = xpath_2 + str(i) + xpath_3
                search_field_UN = driver.find_element_by_xpath(o_xpath)
                search_field_UN.clear()
                search_field_UN.send_keys(l1[i - 2])
            if j == 10:
                new_line = driver.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr[10]/td[7]/div')
                actions = ActionChains(driver)
                actions.click(new_line).perform()
            j=j+1
            if j == 12:
                printError()