import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import os

path = "C:\\Users\\SC057441\\Desktop\\Local\\tokka\\"

files = [x for x in os.listdir(path) if x.startswith("RC_F_NON")]
workbook = ExcelWriter(path+"RC_F_Non_AR.xlsx")
for file in files:
    df_excel = pd.read_excel(path + file)
    print(file)
    file = file.split('.')
    print(file)
    if len(file[0])>31:
        name = file[0]
        file[0] = name[0:30]
    df_excel.to_excel(workbook, file[0], index=False)
workbook.save()