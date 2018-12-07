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

"""This is a global variable that helps in deciding the xml report for all the test cases that this class runs."""
runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml")

"""This class is used to check if the master and the actual file is present in the folder specified in JSON."""
class File_Extractor(unittest.TestCase):

    def setUp(self):
        self.concept_name = concept_name
        self.primary_key = primary_key

    """This test case get the new files and their path for further use."""
    def test_1_get_files_path_details(self):
        file_list = []
        with open("details_local.json", 'r')as configfile:
            conf = json.load(configfile)
            for incre, value in conf.items():
                if self.concept_name in incre:
                    """This line takes the values like partial path and partial name to find the exact path and file name."""
                    file_list.append(self.file_details(value[0], value[1]))
            configfile.close()
        loggingexcel.logger.info("The list of files and paths selected for both master and slave operations are as follows : %s", file_list)
        """This is used to trigger the rest of the test cases once we get the path and the file names."""
        self.main_fnuc(file_list,self.primary_key,self.concept_name)

    """This function will return the file names and its exact path."""
    def file_details(self, path, regfile):
        if "HI_Master" in path:
            return regfile + ".xlsx", path
        elif "temp" in path:
            print(regfile + ".xlsx", path)
            print(path+"\\"+regfile+".xlsx")
            workbook1 = xlsxwriter.Workbook(path+"\\"+regfile+".xlsx")
            print(workbook1)
            workbook1.close()
            return regfile + ".xlsx", path
        else:
            print(path,regfile)
            files = [x for x in os.listdir(path) if x.startswith(regfile)]
            date_created = os.path.getmtime(path + "\\" + files[0])
            print(date_created)
            today_date = datetime.fromtimestamp(date_created).strftime('%Y-%m-%d')
            print(today_date)
            loggingexcel.logger.info("Checking if the above files are the most recent one i.e dates: %s", today_date)
            now = datetime.now()
            now = now.strftime("%Y-%m-%d")
            print(now)
            if now == today_date:
                return files[0], path

    """This is to run the already built test suite"""
    def run_suite(self,ret_suite,sheet_name_xml):
        suite1 = ret_suite
        incre =0
        ret=[]
        for test_i in suite1:
            runner1 = xmlrunner.XMLTestRunner(output="./python_unittests_xml", outsuffix=sheet_name_xml[incre])
            incre += 1
            ret1 = not runner1.run(test_i).wasSuccessful()
            ret.append(ret1)
        return ret

    """This is to build a test suite"""
    def build_suite(self,excel_1_sheet_name,excel_2_sheet_name,workbook,primarykey,sheetname1,row_offset):
        suite1 = unittest.TestSuite()
        p_key = primarykey
        excel_1 = pd.read_excel(excel_1_sheet_name, sheetname1).fillna("No-Data")
        excel_2 = pd.read_excel(excel_2_sheet_name, sheetname1).fillna("No-Data")
        worksheet = workbook.add_worksheet(sheetname1)
        loggingexcel.logger.info(sheetname1)
        suite1.addTest(ParametrizedTestCase.parametrize(TestExcelCompare, filepointer_master=excel_1, filepointer_actual=excel_2,
                                             worksheet1=worksheet, workbook1=workbook, row_offset1=row_offset,
                                             primary_key=p_key))
        return suite1
    """This function is the start point in creating the test cases and building the suite with a difference file."""
    def main_fnuc(self, file_list,primary_key,concept_name):
        concept_name = concept_name
        primary_key = primary_key
        ret_suite = []
        file_list1 = []
        for val in file_list:
            file_list1.append(str(val[1]) + "\\" + str(val[0]))
        excel_1_sheet = pd.ExcelFile(file_list1[0])
        excel_2_sheet = pd.ExcelFile(file_list1[1])
        now = datetime.now()
        today = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name_diff = 'Differences_Master_' +concept_name+'_'+ today + '.xlsx'
        workbook = xlsxwriter.Workbook(file_name_diff)
        excel_1_sheet_name = pd.ExcelFile(file_list1[0])
        excel_2_sheet_name = pd.ExcelFile(file_list1[1])
        sheet_name_xml = excel_2_sheet.sheet_names
        row_offset = 1
        if set(excel_1_sheet.sheet_names[2:]) == set(excel_2_sheet.sheet_names):
            if "None" == primary_key[1]:
                primarykey="None"
                for sheetname1 in excel_1_sheet.sheet_names:
                    if sheetname1 == "Requirements" or sheetname1 == "Scenario_Mapping":
                        continue
                    else:
                        ret_suite1 = self.build_suite(excel_1_sheet_name,excel_2_sheet_name,workbook,primarykey,sheetname1,row_offset)
                        ret_suite.append(ret_suite1)
                ret1 = self.run_suite(ret_suite,sheet_name_xml)
            else:
                count =0
                for sheetname1 in excel_1_sheet.sheet_names:
                    if sheetname1 == "Requirements" or sheetname1 == "Scenario_Mapping":
                        continue
                    else:
                        ret_suite1 = self.build_suite(excel_1_sheet_name, excel_2_sheet_name, workbook,primary_key[count],sheetname1, row_offset)
                        count= count +1
                        ret_suite.append(ret_suite1)
                ret1 = self.run_suite(ret_suite, sheet_name_xml)
        else:
            print("the sheet names are not matching")
            workbook.close()
            sys.exit(1)
        if 1 in ret1:
            print("I am exiting 1")
            workbook.close()
            sys.exit(1)

"""This is the start point of the code to """
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Asking for all the details to run the code")
    parser.add_argument('primary_key',type=str,help='Please enter the primary key if there is any with the excels or just mention None')
    parser.add_argument('concept_name', help='Please enter the concept name that you would want to run.')
    args = parser.parse_args()
    primary_key = args.primary_key.split(',')
    print(primary_key)
    concept_name = args.concept_name
    del sys.argv[1:]
    runner.run(File_Extractor('test_1_get_files_path_details'))
