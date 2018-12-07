import unittest
from ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
import sys
import json
from sample_test import SampleTest
from loginPage import login

if __name__ == '__main__':
    domain = sys.argv[1]
    del sys.argv[1:]
    suite = unittest.TestSuite()
    with open("inputUrls.json",'r') as inputsJson:
        inputs = json.load(inputsJson)
    urllist = inputs['urllist']
    adjustmentList = inputs['adjustmentList']
    facility_name = inputs['facility_name']

    if domain == 'staging':
        browser = login.login_staging()
        stagingBaseUrls = inputs['stagingBaseUrls']
        for i in adjustmentList:
            adjustmentsUrl = stagingBaseUrls+i
            print(i,adjustmentsUrl)
            suite.addTest(ParametrizedTestCase.parametrize(SampleTest, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = urllist))
    elif domain == 'dev':
        browser = login.login_dev()
        devBaseUrls = inputs['devBaseUrls']
        for i in adjustmentList:
            adjustmentsUrl = devBaseUrls + i
            suite.addTest(ParametrizedTestCase.parametrize(SampleTest, driverParam=browser, urlParam=adjustmentsUrl, facility_name=facility_name, urlListParam = urllist))

    kwargs = {
        "output": "./python_unittests_xml",
    }
    runner = xmlrunner.XMLTestRunner(**kwargs)
    # runner.run(suite)
    for test_i in suite:
        runner.run(test_i)
