import unittest
import pandas as pd
import os
import xlsxwriter
import sys
from datetime import datetime
import argparse
import xmlrunner
from ParametrizedTestCase import ParametrizedTestCase
from Final_Excel_Comparator import TestExcelCompare
from logger_excel import loggingexcel
import json

def main_fnuc(file_list):
    print(file_list)


class File_Extractor(unittest.TestCase):

    def setUp(self):
        self.concept_name = "NonAR"

    def test_get_files_path_details(self):
        file_list = []
        with open("details_local.json", 'r')as configfile:
            conf = json.load(configfile)
            for incre, value in conf.items():
                if self.concept_name in incre:
                    file_list.append(self.file_details(value[0],value[1]))
            configfile.close()
        loggingexcel.logger.info("The list of files and paths selected for both master and slave operations are as follows : %s", file_list)
        main_fnuc(file_list)

    def file_details(self,path,regfile):
        if "HI_Master"in path:
            print(regfile+".xlsx",path)
            return regfile+".xlsx",path
        else:
            files = [x for x in os.listdir(path) if x.startswith(regfile)]
            date_created = os.path.getmtime(path +"\\"+ files[0])
            today_date = datetime.fromtimestamp(date_created).strftime('%Y-%m-%d')
            loggingexcel.logger.info("Checking if the above files are the most recent one i.e dates: %s",today_date)
            now = datetime.now()
            now = now.strftime("%Y-%m-%d")
            if now == today_date:
                return files[0],path
if __name__=="__main__":
    unittest.main()