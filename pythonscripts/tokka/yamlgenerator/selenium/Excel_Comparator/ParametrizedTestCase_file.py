import unittest
"""This class is used to parameterized all the values into the unittest class."""
class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', concept_name=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.concept_name = concept_name
    """THis is used to specify all the parameters that are used in the code and send them to main class logic"""
    @staticmethod
    def parametrize(testcase_class, concept_name=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, concept_name=concept_name))
        return suite