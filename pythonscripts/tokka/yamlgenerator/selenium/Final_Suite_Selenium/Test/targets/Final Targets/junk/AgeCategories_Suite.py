import unittest
from tests.RCR_VR_HA_Tool_Age_Categories_Summary import TestAgeCategoriesFE
from resource.ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
import sys
from resource.loggin_FE import loggingFE

if __name__ == '__main__':
    suite = unittest.TestSuite()
    value = sys.argv[1]
    del sys.argv[1:]
    loggingFE.logger.info("This is running in", value)
    suite.addTest(ParametrizedTestCase.parametrize(TestAgeCategoriesFE, param=value))
    kwargs = {
        "output": "./python_unittests_xml",
    }
    runner = xmlrunner.XMLTestRunner(**kwargs)
    # runner.run(suite)
    for test_i in suite:
        ret = not runner.run(test_i).wasSuccessful()
        sys.exit(ret)