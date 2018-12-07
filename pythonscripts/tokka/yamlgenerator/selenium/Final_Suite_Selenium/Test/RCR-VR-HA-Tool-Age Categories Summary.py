import unittest
from FinalTestSuite_Age_Categories_FE import TestAgeCategoriesFE
from ParametrizedTestCase import ParametrizedTestCase
import xmlrunner
import sys
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    value = sys.argv[1]
    del sys.argv[1:]
    logger.info("This is running in", value)
    suite.addTest(ParametrizedTestCase.parametrize(TestAgeCategoriesFE, param=value))
    kwargs = {
        "output": "./python_unittests_xml",
    }
    runner = xmlrunner.XMLTestRunner(**kwargs)
    # runner.run(suite)
    for test_i in suite:
        ret = not runner.run(test_i).wasSuccessful()
        sys.exit(ret)