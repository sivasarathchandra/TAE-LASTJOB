import pandas as pd
import unittest
import openpyxl
import xlsxwriter
from Fetch_New_Files import File_Extractor

class TestExcelCompare(unittest.TestCase):

    row_num = 1
    file_name = File_Extractor().get_files_path_details()
    print(file_name)
    excel_1 = pd.read_excel(file_name[0]).fillna("No-Data")
    excel_2 = pd.read_excel(file_name[1]).fillna("No-Data")

    def write_to_excel(self, row, col):
        data = self.excel_1.iloc[row]
        data_list = list(data)
        self.worksheet.write(TestExcelCompare.row_num, 0, row+2)
        for col_num in range(0, self.excel_1_matrix[1]):
            if col_num == col:
                self.worksheet.write(TestExcelCompare.row_num, col_num+1, data_list[col_num], self.highlight)
            else:
                self.worksheet.write(TestExcelCompare.row_num, col_num+1, data_list[col_num])
        TestExcelCompare.row_num += 1

    def setUp(self):
        self.excel_1_columns = pd.Series(TestExcelCompare.excel_1.columns)
        self.excel_2_columns = pd.Series(TestExcelCompare.excel_2.columns)
        self.excel_1_matrix = TestExcelCompare.excel_1.shape
        self.excel_2_matrix = TestExcelCompare.excel_2.shape
        self.workbook = xlsxwriter.Workbook('Differences.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.highlight = self.workbook.add_format({'bold' : True, 'bg_color' : 'yellow', 'font_color' : 'red'})

    def test_1_validate_column_row_count(self):
        self.assertTupleEqual(self.excel_1_matrix, self.excel_2_matrix)

    def test_2_validate_column_names(self):
        excel_1_columns_list = list(self.excel_1_columns)
        excel_2_columns_list = list(self.excel_2_columns)
        self.assertListEqual(excel_1_columns_list, excel_2_columns_list)

    def test_3_validate_data(self):
        failure_ind = 0
        self.worksheet.write('A1', 'Row Num')
        self.worksheet.write_row('B1', list(self.excel_1_columns))
        for row in range(0, self.excel_1_matrix[0]):
            for col in range(0, self.excel_1_matrix[1]):
                if self.excel_1.iat[row, col] == self.excel_2.iat[row, col]:
                    continue
                else:
                    difference = self.excel_1.iat[row, col]
                    self.write_to_excel(row, col)
                    failure_ind = 1
        self.workbook.close()
        self.assertEqual(failure_ind, 0)

if __name__ == '__main__':
    unittest.main(failfast=True)