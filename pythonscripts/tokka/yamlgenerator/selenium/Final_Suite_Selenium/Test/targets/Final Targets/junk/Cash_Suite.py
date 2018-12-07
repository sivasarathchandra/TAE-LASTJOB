import unittest
from resource.ParametrizedTestCaseTarget import ParametrizedTestCase
import xmlrunner
import sys
import json
import os
from resource.loginPage import login
from tests.RCR_VR_HA_FE_ConfigTool_Cash import CashFE
from resource.logging_FE import loggingFE

WORKSPACE = os.environ['WORKSPACE']

if __name__ == '__main__':
    incre = 0
    ret_val = []
    """This is where the execution starts by giving the argument as dev or staging"""
    domain = sys.argv[1]
    del sys.argv[1:]
    loggingFE.logger.info("This is running from: ", domain)
    suite = unittest.TestSuite()
    """Fetching the data from a json that are required for test"""
    with open('"'+WORKSPACE+'"'+"resource/inputParams.json",'r') as inputsJson:
        inputs = json.load(inputsJson)
    tabList = inputs['cashTabList']
    cashList = inputs['cashList']
    """If the argument is staging or if it dev the control switches."""
    if domain == 'staging':
        browser = login.login_staging()
        stagingBaseUrl = inputs['stagingBaseUrl']
        facility_name = inputs['facility_name_staging']
        for incr in cashList:
            cashUrl = stagingBaseUrl + incr
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(CashFE, driverParam=browser, urlParam=cashUrl, facility_name=facility_name, urlListParam = tabList))
    elif domain == 'dev':
        browser = login.login_dev()
        devBaseUrl = inputs['devBaseUrl']
        facility_name = inputs['facility_name_dev']
        for incr in cashList:
            cashUrl = devBaseUrl + incr
            """Sending the parameters with parameterized class."""
            suite.addTest(ParametrizedTestCase.parametrize(CashFE, driverParam=browser, urlParam=cashUrl, facility_name=facility_name, urlListParam = tabList))
    """Running the test from the suite created for all the list of URL's"""
    for test_i in suite:
        runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml",outsuffix=cashList[incre])
        incre = incre + 1
        ret = not runner.run(test_i).wasSuccessful()
        ret_val.append(ret)
    """Finally quiting from the browser."""
    browser.quit()
    for item in ret_val:
        if item == True:
            sys.exit(True)
    sys.exit(False)