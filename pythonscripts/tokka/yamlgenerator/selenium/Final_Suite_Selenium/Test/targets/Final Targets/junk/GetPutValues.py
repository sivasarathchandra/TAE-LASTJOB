from selenium.common.exceptions import NoSuchElementException
from resource.logging_FE import loggingFE
"""This class is for re usable codes for fetching and placing the values from the pages."""
class GetPutValues():
    """This method is to get the data at facility level"""
    def getFacilityValues(self, driver, facilityName, click_xpath, pageNum):
        loggingFE.logger.info("Get the facility values")
        self.browser = driver
        self.facility_existing_values = []
        if pageNum > 0:
            for incr in range(0, pageNum):
                self.browser.find_element_by_xpath(click_xpath).click()
        matchFound = True
        while matchFound:
            try:
                facilityElement = self.browser.find_element_by_xpath("//td[contains(text(),'"+facilityName+"')]")
                if facilityElement != None:
                    facilityInputs = self.browser.find_elements_by_xpath("//td[contains(text(),'" + facilityName + "')]/following-sibling::td/input")
                    for incr in range(0,3):
                        val = facilityInputs[incr].get_attribute('value')
                        self.facility_existing_values.append(val)
                break
            except NoSuchElementException:
                self.browser.find_element_by_xpath(click_xpath).click()
                pageNum = pageNum + 1
        loggingFE.logger.info("Returing the existing values")
        return self.facility_existing_values, pageNum

    """This method is to put the data at facility level"""
    def putFacilityValues(self, driver, facilityName, facilityValues, click_xpath, pageNum):
        loggingFE.logger.info("placing the new valule within the exact positions of facility")
        self.browser = driver
        self.facility_existing_values = []
        if pageNum > 0:
            for incr in range(0, pageNum):
                self.browser.find_element_by_xpath(click_xpath).click()
        matchFound = True
        while matchFound:
            try:
                facilityElement = self.browser.find_element_by_xpath("//td[contains(text(),'" + facilityName + "')]")
                if facilityElement != None:
                    facilityInputs = self.browser.find_elements_by_xpath("//td[contains(text(),'" + facilityName + "')]/following-sibling::td/input")
                    for incr in range(0,3):
                        facilityInputs[incr].clear()
                        facilityInputs[incr].send_keys(facilityValues[incr])
                    alert_facility = self.browser.find_element_by_xpath("//td[contains(text(),'" + facilityName + "')]/preceding-sibling::td/div").get_attribute(
                        'title')
                    if self.browser.find_element_by_id('save_config').get_attribute('disabled'):
                        loggingFE.logger.info("cannot save")
                    else:
                        self.browser.find_element_by_id('save_config').click()
                    break
            except NoSuchElementException:
                self.browser.find_element_by_xpath(click_xpath).click()
        loggingFE.logger.info("returning the value to the base function")
        return alert_facility

    """This method is to get the data at Default level"""
    def getDefaultValues(self, driver, defaultXpaths):
        loggingFE.logger.info("getting the existing value at the Default level")
        self.browser = driver
        self.defaultXpaths = defaultXpaths
        self.default_existing_vals = []
        for incr in self.defaultXpaths:
            val = self.browser.find_element_by_xpath(incr).get_attribute('value')
            self.default_existing_vals.append(val)
        loggingFE.logger.info("Returning the default value from the existing page")
        return self.default_existing_vals

    """This method is to put the data at Default level"""
    def putDefaultValues(self, driver, defaultXpaths, defaultValues):
        loggingFE.logger.info("Placing the values at the Default level")
        self.browser = driver
        self.defaultXpaths = defaultXpaths
        self.defaultValues = defaultValues
        for incr in range(0,3):
            defaults = self.browser.find_element_by_xpath(self.defaultXpaths[incr])
            defaults.clear()
            defaults.send_keys(defaultValues[incr])
        if self.browser.find_element_by_id('save_config').get_attribute('disabled'):
            loggingFE.logger.info("cannot save")
        else:
            self.browser.find_element_by_id('save_config').click()
        alert_default = self.browser.find_element_by_xpath("//*[@id='form-update']/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/div").get_attribute('title')
        loggingFE.logger.info("Returning the default value from the existing page")
        return alert_default