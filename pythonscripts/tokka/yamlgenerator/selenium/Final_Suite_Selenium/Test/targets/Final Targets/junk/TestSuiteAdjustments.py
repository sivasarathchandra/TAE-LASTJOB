import unittest
from ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
import sys
import json
from loginPage import login
from FinalTestSutie_Targets_Adjustments_FE import AdjustmentsFE
from logging_FE import loggingFE

if __name__ == '__main__':
    incre = 0
    """This is where the execution starts by giving the argument as dev or staging"""
    domain = sys.argv[1]
    del sys.argv[1:]
    loggingFE.logger.info("This is running from: ", domain)
    suite = unittest.TestSuite()
    """Fetching the data from a json that are required for test"""
    with open("inputParams.json",'r') as inputsJson:
        inputs = json.load(inputsJson)
    tabList = inputs['adjustmentTabList']
    adjustmentList = inputs['adjustmentList']
    """If the argument is staging or if it dev the control switches."""
    if domain == 'staging':
        browser = login.login_staging()
        stagingBaseUrl = inputs['stagingBaseUrl']
        facility_name = inputs['facility_name_staging']
        for incr in adjustmentList:
            adjustmentsUrl = stagingBaseUrl + incr
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(AdjustmentsFE, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = tabList))
    elif domain == 'dev':
        browser = login.login_dev()
        devBaseUrl = inputs['devBaseUrl']
        facility_name = inputs['facility_name_dev']
        for incr in adjustmentList:
            adjustmentsUrl = devBaseUrl + incr
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(AdjustmentsFE, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = tabList))
    """Running the test from the suite created for all the list of URL's"""
    for test_i in suite:
        runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml",outsuffix=adjustmentList[incre])
        incre = incre + 1
        runner.run(test_i)
    """Finally quiting from the browser."""
    browser.quit()