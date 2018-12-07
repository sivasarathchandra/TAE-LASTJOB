import unittest
"""This class is used to parameterized all the values into the unittest class."""
class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', query=None, folder_name=None,username=None,password=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.query=query
        self.folder_name=folder_name
        self.username=username
        self.password=password
    """THis is used to specify all the parameters that are used in the code and send them to main class logic"""
    @staticmethod
    def parametrize(testcase_class, query=None, folder_name=None,username=None,password=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, query=query, folder_name=folder_name,username=username,password=password))
        return suite