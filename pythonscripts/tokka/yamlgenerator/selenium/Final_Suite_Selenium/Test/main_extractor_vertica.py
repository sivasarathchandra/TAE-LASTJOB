import sys
import json
import unittest
from ParametrizedTestCase_Extractor_Vertica import ParametrizedTestCase
from Extractor_Vertica import VerticaExtractorFE
import argparse
import xmlrunner
import pandas as pd
from datetime import datetime
import re
from pandas import ExcelWriter
import os

if __name__=="__main__":
    temp = []
    twoqueryfiles = []
    parser = argparse.ArgumentParser(description="Asking for all the details to run the code")
    parser.add_argument('queryname', help='Enter the key that is placed in the query json. Ideally for the concept you want to run')
    parser.add_argument('username', help='Kindly enter the user name to get access to 15stp reports query tool')
    parser.add_argument('password', help='authenticate by giving password')
    args = parser.parse_args()
    queryname = args.queryname
    username1 = args.username
    password = args.password
    suite = unittest.TestSuite()
    del sys.argv[1:]
    with open("query.json", 'r') as queryfile:
        query = json.load(queryfile)
    values = query[queryname]
    if len(values) > 2 and len(values)%2 == 0:
        chunks = [values[x:x + 2] for x in range(0, len(values), 2)]
        for outer in chunks:
            print(outer)
            suite.addTest(ParametrizedTestCase.parametrize(VerticaExtractorFE, query=outer[0], folder_name=outer[1], username=username1, password=password))
    else:
        suite.addTest(ParametrizedTestCase.parametrize(VerticaExtractorFE, query=values[0], folder_name=values[1], username=username1, password=password))
    for test_i in suite:
        runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
        runner.run(test_i)
    if queryname in twoqueryfiles:
        path = "C:\\Users\\sc057441\\Desktop\\Local\\tokka\\"
        files = [x for x in os.listdir(path) if x.startswith("RC_F")]
        workbook = pd.ExcelWriter(path + "RC_F_" + queryname + ".xlsx", engine='xlsxwriter')
        r1 = re.compile('2.*-.*-.*')
        for file in files:
            df_excel = pd.read_excel(path + file)
            file = file.split('.')
            for key, value in df_excel.items():
                if "date" in key:
                    if r1.match(str(value[0])) is not None:
                        col1 = value[0]
                        col1 = datetime.strptime(str(col1), "%Y-%m-%d %H:%M:%S")
                        col11 = pd.Series(col1).dt.strftime("%d-%m-%Y")
                        df_excel[key] = col11
                        print(df_excel[key])
                        # print(df_excel[key])
            df_excel.to_excel(workbook, file[0], index=False)
        workbook.save()
