import unittest
import pandas as pd
import os
import xlsxwriter
from datetime import datetime
import xmlrunner
from ParametrizedTestCase import ParametrizedTestCase
from Final_Excel_Comparator import TestExcelCompare
import json
# from logging_FE import loggingFE


class File_Extractor():

    def get_files_path_details(self):
        file_list = []
        with open("details.json", 'r')as configfile:
            conf = json.load(configfile)
            for incre, value in conf.items():
                file_list.append(self.file_details(value[0],value[1]))
            configfile.close()
        print(file_list)
        return file_list

    def file_details(self,path,regfile):
        print(path)
        if "HI_Master"in path:
            return regfile
        else:
            files = [x for x in os.listdir(path) if x.startswith(regfile)]
            date_created = os.path.getmtime(path +"\\"+ files[0])
            today_date = datetime.fromtimestamp(date_created).strftime('%Y-%m-%d')
            now = datetime.now()
            now = now.strftime("%Y-%m-%d")
            if now == today_date:
                return files[0]

if __name__ == '__main__':
    file_list = []
    suite = unittest.TestSuite()
    file_list = File_Extractor().get_files_path_details()
    excel_1_sheet = pd.ExcelFile(file_list[0])
    excel_2_sheet = pd.ExcelFile(file_list[1])
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    workbook = xlsxwriter.Workbook('Differences_'+name+'_'+today+'.xlsx')
    excel_1_sheet_name = pd.ExcelFile(file_list[0])
    excel_2_sheet_name = pd.ExcelFile(file_list[1])
    row_offset = 1
    if set(excel_1_sheet.sheet_names[2:]) == set(excel_2_sheet.sheet_names):
        for sheetname1 in excel_1_sheet.sheet_names:
            if sheetname1 == "Requirements" or sheetname1 == "Scenario_Mapping":
                continue
            else:
                excel_1 = pd.read_excel(excel_1_sheet_name, sheetname1).fillna("No-Data")
                excel_2 = pd.read_excel(excel_2_sheet_name, sheetname1).fillna("No-Data")
                worksheet = workbook.add_worksheet(sheetname1)
                print(sheetname1)
                suite.addTest(ParametrizedTestCase.parametrize(TestExcelCompare, filepointer_master=excel_1, filepointer_actual=excel_2, worksheet1=worksheet, workbook1=workbook, row_offset1=row_offset))
        for test_i in suite:
            runner = xmlrunner.XMLTestRunner(output="./python_unittests_xml")
            runner.run(test_i)
    workbook.close()
