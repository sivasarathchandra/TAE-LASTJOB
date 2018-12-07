import pandas as pd
import unittest
from ParametrizedTestCase import ParametrizedTestCase
from logger_excel import loggingexcel


"""This is the class that is used to test all the possible cases while comparing two excels."""
class TestExcelCompare(ParametrizedTestCase):

    """This function is used to write the data to difference excel if there is any."""
    def write_to_excel(self, row_num, col_nums):
        data = self.filepointer_master.iloc[row_num]
        data_list = list(data)
        loggingexcel.logger.info(self.worksheet1)
        self.worksheet1.write(self.row_offset1, 0, row_num+2)
        for col_num in range(0, self.excel_1_matrix[1]):
            if col_num in col_nums:
                self.worksheet1.write(self.row_offset1, col_num+1, data_list[col_num], self.highlight)
            else:
                  self.worksheet1.write(self.row_offset1, col_num+1, data_list[col_num])
        self.row_offset1 += 1

    def setUp(self):
        self.excel_1_columns = pd.Series(self.filepointer_master.columns)
        self.excel_2_columns = pd.Series(self.filepointer_actual.columns)
        self.excel_1_matrix = self.filepointer_master.shape
        self.excel_2_matrix = self.filepointer_actual.shape
        self.primary_col_name = self.primary_key
        self.highlight = self.workbook1.add_format({'bold': True, 'bg_color': 'yellow', 'font_color': 'red'})

    """This test case is to validate the row and column count across both the docs for comparision."""
    def test_1_validate_column_row_count(self):
        loggingexcel.logger.info("Validating the column and the row counts")
        self.assertTupleEqual(self.excel_1_matrix, self.excel_2_matrix,"The 1st set of values are from master and 2nd are from the daily reports, mismatch in the column and row counts")
        if self.primary_col_name != "None":
            loggingexcel.logger.info(self.primary_col_name)
            self.assertEqual(set(list(self.filepointer_master[self.primary_col_name])),set(list(self.filepointer_actual[self.primary_col_name])),"This is to check if the primary key is missing in both of them or not.")
        else:
            pass

    """This test case is to validate the column names across both the excels."""
    def test_2_validate_column_names(self):
        loggingexcel.logger.info("Validating the column names and the returning if there are any swap in column locations.")
        excel_1_columns_list = list(self.excel_1_columns)
        excel_2_columns_list = list(self.excel_2_columns)
        self.assertEqual(excel_1_columns_list, excel_2_columns_list,"The 1st set of values are from master and 2nd are from the daily reports, mismatch in the column counts or even the names")

    """This test case is to validate the data that is in the actual file against the master files."""
    def test_3_validate_data(self):
        if self.primary_col_name == "None":
            failure_ind = 0
            self.worksheet1.write('A1', 'Row Num')
            self.worksheet1.write_row('B1', list(self.excel_1_columns))
            for row in range(0, self.excel_1_matrix[0]):
                row_num = -1
                col_nums = []
                col_num = 0
                for col in self.excel_1_columns:
                    if self.filepointer_master.at[row, col] == self.filepointer_actual.at[row, col]:
                        col_num += 1
                        continue
                    else:
                        # difference = self.excel_1.iat[row, col]
                        row_num = row
                        col_nums.append(col_num)
                        failure_ind = 1
                        col_num += 1
                if row_num >= 0:
                    self.write_to_excel(row_num, col_nums)
                    loggingexcel.logger.info("Writing to the difference excel.")
            self.assertEqual(failure_ind, 0,"There is a difference between Master file and the output file. Please find for the difference sheet with todays date in the name")
        else:
            self.worksheet1.write('A1', 'Row Num')
            self.worksheet1.write_row('B1', list(self.excel_1_columns))
            excel_1_columns_list = list(self.excel_1_columns)
            if set(list(self.filepointer_master[self.primary_col_name])) != set(list(self.filepointer_actual[self.primary_col_name])):
                value = list(self.filepointer_master[self.primary_col_name])
                for ele in value:
                    if ele not in list(self.filepointer_actual[self.primary_col_name]):
                        print("This is the value that is missing: ",ele)
                        for row in range(0, self.excel_1_matrix[0]):
                            cols = []
                            if self.filepointer_master.at[row, excel_1_columns_list[0]] == ele:
                                for col in range(0, self.excel_1_matrix[1]):
                                    failure_ind = 1
                                    cols.append(col)
                                self.write_to_excel(row, cols)
            failure_ind = 0
            for row in range(0, self.excel_1_matrix[0]):
                for row1 in range(0, self.excel_2_matrix[0]):
                    if self.filepointer_master.at[row,excel_1_columns_list[0]] == self.filepointer_actual.at[row1, excel_1_columns_list[0]]:
                        row_num = -1
                        col_nums = []
                        col_num = 0
                        for col in self.excel_1_columns:
                            if self.filepointer_master.at[row, col] == self.filepointer_actual.at[row1, col]:
                                col_num += 1
                                continue
                            else:
                                # difference = self.excel_1.iat[row, col]
                                row_num = row
                                col_nums.append(col_num)
                                failure_ind = 1
                                col_num += 1
                        if row_num >= 0:
                            self.write_to_excel(row_num, col_nums)
                            loggingexcel.logger.info("Writing to the difference excel.")
            self.assertEqual(failure_ind, 0,"There is a difference between Master file and the output file. Please find for the difference sheet with todays date in the name")

"""This is the starting point of this class."""
if __name__ == '__main__':
    unittest.main(failfast=True)