from logging_FE import loggingFE
from GetPutValues import GetPutValues

class ErrorValidationClass:

    error_1 = 'Target should be greater than or equal to Bottom Zone'
    error_2 = 'Target should be less than or equal to Top Zone'
    error_3 = 'Top Zone should be greater than or equal to Bottom Zone'

    """This testcase will check for an error when the target less than bottom zone"""
    def target_less_than_bottom_zone(self, driver, facilityName, clickXpath, pageNum, defaultsXpath):
        loggingFE.logger.info("Checking target less than bottom zone")
        facility_data = [120000, 200000, 500000]
        default_data = [150000, 350000, 650000]
        print('In ErrorValidation - target_less_than_bottom_zone')
        print(pageNum)
        alert_facility = GetPutValues.putFacilityValues(self, driver=driver, facilityName=facilityName,
                                                        facilityValues=facility_data, click_xpath=clickXpath,
                                                        pageNum=pageNum)
        alert_default = GetPutValues.putDefaultValues(self, driver=driver, defaultXpaths=defaultsXpath,
                                                      defaultValues=default_data)

        if alert_facility == ErrorValidationClass.error_1 and alert_default == ErrorValidationClass.error_1:
            return 1
        else:
            return 0

    """This testcase will check for an error when the target is greater than top zone"""

    def target_greater_than_top_zone(self, driver, facilityName, clickXpath, pageNum, defaultsXpath):
        loggingFE.logger.info("Checking if target greater than top zone")
        facility_data = [621234, 201234, 501234]
        default_data = [751234, 351234, 651234]
        print('In ErrorValidation - target_greater_than_top_zone')
        print(pageNum)
        alert_facility = GetPutValues.putFacilityValues(self, driver=driver, facilityName=facilityName,
                                                        facilityValues=facility_data, click_xpath=clickXpath,
                                                        pageNum=pageNum)
        alert_default = GetPutValues.putDefaultValues(self, driver=driver, defaultXpaths=defaultsXpath,
                                                      defaultValues=default_data)

        if alert_facility == ErrorValidationClass.error_2 and alert_default == ErrorValidationClass.error_2:
            return 1
        else:
            return 0

    """This testcase will check for an error when the bottom zone is greater than top zone"""
    def bottom_zone_greater_than_top_zone(self, driver, facilityName, clickXpath, pageNum, defaultsXpath):
        loggingFE.logger.info("Checking if bottom zone can be greater than top zone")
        facility_data = ['', 700000, 500000]
        default_data = ['', 750000, 650000]
        print('In ErrorValidation - bottom_zone_greater_than_top_zone')
        print(pageNum)
        alert_facility = GetPutValues.putFacilityValues(self, driver=driver, facilityName=facilityName,
                                                        facilityValues=facility_data, click_xpath=clickXpath,
                                                        pageNum=pageNum)
        alert_default = GetPutValues.putDefaultValues(self, driver=driver, defaultXpaths=defaultsXpath,
                                                      defaultValues=default_data)

        if alert_facility == ErrorValidationClass.error_3 and alert_default == ErrorValidationClass.error_3:
            return 1
        else:
            return 0