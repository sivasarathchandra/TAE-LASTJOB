import unittest
from yamlgenerator.Requests.Final_Suite.tests.TestSuit_Age_categories import TestAgeCategories
from yamlgenerator.Requests.Final_Suite.tests.TestSuit_Organization_Maps import TestOrganizationMaps
from yamlgenerator.Requests.Final_Suite.tests.TestSuit_Targets import TestTargets
from yamlgenerator.Requests.Final_Suite.tests.TestSuit_Syndication import TestSyndication

if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAgeCategories)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestOrganizationMaps)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestTargets)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestSyndication)
    suite = unittest.TestSuite([suite1,suite2,suite3,suite4])
    unittest.TextTestRunner().run(suite)
    #unittest.TextTestRunner().run(suite2)
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
