import unittest
import xmlrunner
from Tests.RCR_VR_HA_Service_ConfigTool_Age_Categories_PUT import TestAgeCategoriesPut
# from tests.org_sample import TestTargetsPut
from Tests.RCR_VR_HA_Service_ConfigTool_Organization_Map_PUT import TestOrganizationMapsDev
from Tests.RCR_VR_HA_Service_ConfigTool_Targets_PUT import TestTargetsPut
from Tests.RCR_VR_HA_Service_ConfigTool_Config_Items_PUT import TestSuiteConfigItemsPut
from Tests.config_API import configAPI
from Tests.logging_API import loggingAPI
import sys
import json

"""This is the start point of execution."""
if __name__ == "__main__":
    iter = 0
    incres = 0
    ret_val = []
    all_config_details = []
    all_config_value = []
    all_test_name = [TestAgeCategoriesPut,TestOrganizationMapsDev,TestTargetsPut,TestSuiteConfigItemsPut]
    filename = sys.argv[1]
    print(filename)
    del sys.argv[1:]
    with open(filename,'r')as configfile:
        conf = json.load(configfile)
        for incre , value in conf.items():
            all_config_details.append(incre)
            all_config_value.append(value)
        configfile.close()
    for iter in range(0,len(all_test_name)):
        configAPI.configlist = all_config_value[iter]
        loggingAPI.logger.info("The data that is being used to perform all the task are below:")
        loggingAPI.logger.info(configAPI.configlist)
        tests = unittest.TestLoader().loadTestsFromTestCase(all_test_name[iter])
        loggingAPI.logger.info(all_test_name[iter])
        result = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
        ret = not result.run(tests).wasSuccessful()
        ret_val.append(ret)
    for item in ret_val:
        if item == True:
            sys.exit(True)
    sys.exit(False)