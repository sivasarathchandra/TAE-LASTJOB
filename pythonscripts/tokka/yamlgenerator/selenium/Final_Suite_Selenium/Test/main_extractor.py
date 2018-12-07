import unittest
import xmlrunner
from GeneralARResultSetExporterFrontEnd import GeneralARVerticaExtractorFE
from NonARResultSetExporterFrontEnd import NonARVerticaExtractorFE
from ClientARResultSetExporterFrontEnd import ClientARVerticaExtractorFE
from logginQuery import logginQuery

if __name__=="__main__":
    logginQuery.logger.info("The querying starts from here")
    incer = 0
    test_names=[GeneralARVerticaExtractorFE,NonARVerticaExtractorFE,ClientARVerticaExtractorFE]
    for incer in test_names:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_names[incer])
        incer = incer + 1
        result = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
        result.run(tests)
