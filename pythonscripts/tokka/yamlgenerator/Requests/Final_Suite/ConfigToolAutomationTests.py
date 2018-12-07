import unittest
import xmlrunner
from tests.RCRVRHAServiceConfigToolAgeCategoriesGET import TestAgeCategories
from tests.RCRVRHAServiceConfigToolOrganizationMapsGET import TestOrganizationMaps
from tests.RCRVRHAServiceConfigToolSyndicationfieldsGET import TestSyndication
from tests.RCRVRHAServiceConfigToolTargetsGET import TestTargets
from tests.RCRVRHAServiceConfigToolConfigitemGET import TestConfigitems
from tests.configAPI import configAPI
from tests.loggingAPI import loggingAPI
import sys
import json

"""This is the start point of execution."""
if __name__ == "__main__":
    iter = 0
    incres = 0
    ret_val = []
    all_config_details = []
    all_config_value = []
    all_test_name = [TestAgeCategories,TestOrganizationMaps,TestSyndication,TestTargets,TestConfigitems]
    filename = sys.argv[1]
    del sys.argv[1:]
    with open(filename,'r')as configfile:
        conf = json.load(configfile)
        for incre , value in conf.items():
            all_config_details.append(incre)
            all_config_value.append(value)
        configfile.close()
    for iter in range(0,5):
        configAPI.configlist = all_config_value[iter]
        split_value_config_name = all_config_details[iter].split('_')
        loggingAPI.logger.info(split_value_config_name)
        loggingAPI.logger.info(split_value_config_name[0])
        if iter >= 5:
            tests = unittest.TestLoader().loadTestsFromTestCase(all_test_name[incres])
            incres = incres + 1
            loggingAPI.logger.info(all_test_name[incres])
            result = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
            result.run(tests)
        else:
            tests = unittest.TestLoader().loadTestsFromTestCase(all_test_name[iter])
            loggingAPI.logger.info(all_test_name[iter])
            result = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
            ret = not result.run(tests).wasSuccessful()
            ret_val.append(ret)
    for item in ret_val:
        if item == True:
            sys.exit(True)
    sys.exit(False)
