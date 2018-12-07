from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class GetPutValues():
    def getFacilityValues(self, driver, facilityName):
        self.browser = driver
        self.facility_existing_values = []
        matchFound = True
        while matchFound:
            try:
                facility = self.browser.find_elements_by_xpath("//td[contains(text(),'"+facilityName+"')]/following-sibling::td/input")
                if facility != None:
                    for i in range(0,3):
                        val = facility[i].get_attribute('value')
                        self.facility_existing_values.append(val)
                break
            except NoSuchElementException:
                browser.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
        return self.facility_existing_values

    def putFacilityValues(self, driver, facilityName, facilityValues):
        self.browser = driver
        self.facility_existing_values = []
        matchFound = True
        while matchFound:
            try:
                facility = self.browser.find_elements_by_xpath("//td[contains(text(),'" + facilityName + "')]/following-sibling::td/input")
                if facility != None:
                    for i in range(0,3):
                        facility[i].clear()
                        facility[i].send_keys(facilityValues[i])
                    if self.browser.find_element_by_id('save_config').get_attribute('disabled'):
                        print('cannot save')
                    else:
                        self.browser.find_element_by_id('save_config').click()
                    break
            except NoSuchElementException:
                browser.find_element_by_xpath('//*[@id="form-update"]/div/div/div/div/div/pagination/nav/span[3]/a[1]').click()
        alert_facility = self.browser.find_element_by_xpath("//td[contains(text(),'" + facilityName + "')]/preceding-sibling::td/div").get_attribute('title')
        return alert_facility

    def getDefaultValues(self, driver, defaultXpaths):
        self.browser = driver
        self.defaultXpaths = defaultXpaths
        self.default_existing_vals = []
        for i in self.defaultsXpath:
            val = self.driver.find_element_by_xpath(i).get_attribute('value')
            self.default_existing_vals.append(val)
        return self.default_existing_vals

    def putDefaultValues(self, driver, defaultXpaths, defaultValues):
        self.browser = driver
        self.defaultXpaths = defaultXpaths
        self.defaultValues = defaultValues
        for i in range(0,3):
            defaults = self.browser.find_element_by_xpath(self.defaultXpaths[i])
            defaults.clear()
            defaults.send_keys(defaultValues[i])
        if self.browser.find_element_by_id('save_config').get_attribute('disabled'):
            print('cannot save')
        else:
            self.browser.find_element_by_id('save_config').click()
        alert_default = self.browser.find_element_by_xpath("//*[@id='form-update']/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div").get_attribute('title')
        return alert_default