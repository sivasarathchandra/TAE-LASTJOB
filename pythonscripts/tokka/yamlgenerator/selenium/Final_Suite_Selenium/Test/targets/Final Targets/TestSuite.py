import unittest
from ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
import sys
import json
from loginPage import login
from FinalTestSutie_Targets_Total_Adjustments_FE_1 import TotalAdjustmentsFE
from logging_FE import loggingFE

if __name__ == '__main__':
    """This is where the execution starts by giving the argument as dev or staging"""
    incr = 0
    domain = sys.argv[1]
    del sys.argv[1:]
    loggingFE.logger.info("This is running from: ", domain)
    suite = unittest.TestSuite()
    """Fetching the data from a json that are required for test"""
    with open("inputUrls.json",'r') as inputsJson:
        inputs = json.load(inputsJson)
    urllist = inputs['urllist']
    adjustmentList = inputs['adjustmentList']
    facility_name = inputs['facility_name']
    """If the argument is staging or if it dev the control switches."""
    if domain == 'staging':
        browser = login.login_staging()
        stagingBaseUrls = inputs['stagingBaseUrls']
        for i in adjustmentList:
            adjustmentsUrl = stagingBaseUrls+i
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(TotalAdjustmentsFE, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = urllist))
    elif domain == 'dev':
        browser = login.login_dev()
        devBaseUrls = inputs['devBaseUrls']
        for i in adjustmentList:
            adjustmentsUrl = devBaseUrls + i
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(TotalAdjustmentsFE, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = urllist))
    """Running the test from the suite created for all the list of URL's"""
    for test_i in suite:
        runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml",outsuffix=adjustmentList[incr])
        incr = incr + 1
        runner.run(test_i)
    """Finally quiting from the browser."""
    browser.quit()

