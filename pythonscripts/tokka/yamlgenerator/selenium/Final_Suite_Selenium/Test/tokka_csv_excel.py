import win32com.client as win32
import win32gui
import win32con
import pandas as pd
import xlsxwriter
import os
import re
from datetime import datetime
queryname = "NonAR"

# xl = win32.gencache.EnsureDispatch('Excel.Application')
# wb = xl.Workbooks.Open(path+file)
# print("Opening new workbook")
# nwb = xl.Workbooks.Add()
# newfile = path+"RC_F_"+queryname+".xlsx"
# wb.Worksheets(["Sheet1"]).Copy(Before=nwb.Worksheets(1))
# nwb.BreakLink(Name=path+file, Type=1)
# nwb.SaveAs(newfile)
# xl.Application.Quit()



path = "C:\\Users\\SC057441\\Desktop\\Local\\tokka\\"
files = [x for x in os.listdir(path) if x.startswith("RC_F")]
# workbook = xlsxwriter.Workbook(path + queryname + ".xlsx", {'strings_to_numbers': True})
# worksheet = workbook.add_worksheet()
# format2 = workbook.add_format({'num_format': 'dd-mm-yy'})
# r1 = re.compile('2.*-.*-.*')
# with open(path + files[0], "r") as csv_read:
#     reader = csv_read.readline()
#     for r, row in enumerate(reader):
#         for c, col in enumerate(row):
#             if r1.match(col) is not None:
#                 col1 = datetime.strptime(col, "%Y-%m-%d")
#                 col11 = col1.strftime("%d-%m-%Y")
#                 col11 = datetime.strptime(col11, "%d-%m-%Y")
#                 print(type(col11))
#                 worksheet.write_datetime(r, c, col11, format2)
#             else:
#                 worksheet.write(r, c, col)
workbook = pd.ExcelWriter(path + "RC_F_"+queryname+".xlsx",engine='xlsxwriter')
r1 = re.compile('2.*-.*-.*')
for file in files:
    df_excel = pd.read_excel(path + file)
    file = file.split('.')
    for key,value in df_excel.items():
        if "date" in key:
            if r1.match(str(value[0])) is not None:
                col1 = value[0]
                col1 = datetime.strptime(str(col1), "%Y-%m-%d %H:%M:%S")
                col11 = pd.Series(col1).dt.strftime("%d-%m-%Y")
                df_excel[key]=col11
                print(df_excel[key])
                # print(df_excel[key])
    df_excel.to_excel(workbook, file[0], index=False)
workbook.save()
    # for k,v in df_excel.items():
    #     if r1.match(str(v[0])) is not None:
    #         print(v[0])
    #         col1 = datetime.strptime(v[0], "%Y-%m-%d")
    #         col11 = col1.strftime("%d-%m-%Y")
    #         col11 = datetime.strptime(col11, "%d-%m-%Y")
    #         print(type(col11))
    #         worksheet.write_datetime(r, c, col11, format2)
# workbook.save()