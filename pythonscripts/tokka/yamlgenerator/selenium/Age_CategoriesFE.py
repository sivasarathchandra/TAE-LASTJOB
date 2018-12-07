from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.webdriver.common.action_chains import ActionChains

j=9


driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle/config/config/age_category")

search_field_UN = driver.find_element_by_xpath('//*[@id="principal"]')
search_field_UN.clear()
search_field_UN.send_keys("RCADMIN")
driver.find_element_by_xpath('//*[@id="invokeLogIn"]').click()
driver.implicitly_wait(500)
final_val = driver.find_element_by_xpath("/html/body/script[2]")
ff = final_val.get_attribute("innerHTML")
xpath_Prefix = '//*[@id="form-update"]/div/div/div/div[2]/article/div/div/table/tbody/tr['
xpath_Suffix = ']/td[6]/div'
for i in range(1,9):
   f_xpath = xpath_Prefix + str(i) + xpath_Suffix
   if i == 1:
      del_button = driver.find_element_by_xpath(f_xpath)
      actions = ActionChains(driver)
      actions.click(del_button).perform()
save_page = driver.find_element_by_xpath('//*[@id="save_config"]')
actions = ActionChains(driver)
actions.click(save_page).perform()
time.sleep(10)
driver.get("https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle/config/config/age_category")
new_line = driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr[8]/td[7]/div')
actions = ActionChains(driver)
actions.click(new_line).perform()

with open("C:/Users/SC057441/Desktop/Any/pythonscripts/tokka/yamlgenerator/selenium/testdata.csv","r") as read_file:
    for line in read_file:
        if re.match(r"^\d+.*$",line):
            l1 = line.split(',')
            xpath_0 = '/html/body/div/div[2]/main/div/div[2]/div/form/div/div/div/div[2]/article/div/div/table/tbody/tr['
            xpath_1 = ']/td['
            xpath_2 = xpath_0 + str(j) + xpath_1
            xpath_3 = ']/input'
            for i in range(2, 6):
                o_xpath = xpath_2 + str(i) + xpath_3
                search_field_UN = driver.find_element_by_xpath(o_xpath)
                search_field_UN.clear()
                search_field_UN.send_keys(l1[i-2])
            break
    save_page = driver.find_element_by_xpath('//*[@id="save_config"]')
    actions = ActionChains(driver)
    actions.click(save_page).perform()
    time.sleep(10)
    driver.close()


# with open("temp_sel.txt","w") as file_sel:
#    file_sel.write(ff)
# with open("temp_sel.txt","r") as out_file_sel:
#    for line in out_file_sel:
#       if line.startswith('w'):
#          regex = r':91,\"end_age\":(.*),\"created_at\":\"2015-11-09T22:44:10\.000Z\",\"updated_at\":\"2016-07-15T20:17:56\.000Z\",\"sort_order\":5}'
#          test_str = line
#          matches = re.search(regex, test_str)
#          if matches:
#             for groupNum in range(0, len(matches.groups())):
#                groupNum = groupNum + 1
#                print("value searching is for {group}".format(group=matches.group(groupNum)))