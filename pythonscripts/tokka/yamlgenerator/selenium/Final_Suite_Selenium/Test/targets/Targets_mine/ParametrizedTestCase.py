import unittest

class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', driverParam=None, urlParam=None, facility_name=None, urlListParam=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.driverParam = driverParam
        self.urlParam = urlParam
        self.facility_name = facility_name
        self.urlListParam = urlListParam

    @staticmethod
    def parametrize(testcase_class, driverParam=None, urlParam=None, facility_name=None, urlListParam=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, driverParam=driverParam, urlParam=urlParam, facility_name=facility_name, urlListParam=urlListParam))
        return suite