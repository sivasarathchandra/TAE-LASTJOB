import unittest
"""This class is used to parameterized all the values into the unittest class."""
class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', filepointer_master=None, filepointer_actual=None, worksheet1=None, workbook1=None, row_offset1=None, primary_key=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.filepointer_master = filepointer_master
        self.filepointer_actual = filepointer_actual
        self.worksheet1 = worksheet1
        self.workbook1 = workbook1
        self.row_offset1 = row_offset1
        self.primary_key = primary_key
    """THis is used to specify all the parameters that are used in the code and send them to main class logic"""
    @staticmethod
    def parametrize(testcase_class, filepointer_master=None, filepointer_actual=None, worksheet1=None, workbook1=None, row_offset1=None, primary_key=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, filepointer_master=filepointer_master, filepointer_actual=filepointer_actual, worksheet1=worksheet1,workbook1=workbook1,row_offset1=row_offset1,primary_key=primary_key))
        return suite