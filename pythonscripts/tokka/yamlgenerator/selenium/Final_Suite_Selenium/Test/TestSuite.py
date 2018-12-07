import unittest
from TestOne import TestOne
from ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
from pyunitreport import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    urls = ["https://adventisthealthsystem.analytics.devcernerpophealth.com/explore/revenue_cycle/config/config/total_adjustments",]
    for i in urls:
        #suite.addTest(xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
        suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=i))
    kwargs = {
        "output": "./python_unittests_xml",
        "failfast": True
    }
    runner = HTMLTestRunner(**kwargs)
    # runner.run(suite)
    for test_i in suite:
        runner.run(test_i)
