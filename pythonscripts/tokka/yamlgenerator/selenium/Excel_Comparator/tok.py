import pandas as pd
from xlrd import open_workbook
import xlsxwriter
rb = open_workbook("C:\\Users\\SC057441\\Desktop\\Any\\pythonscripts\\tokka\\yamlgenerator\\selenium\\Excel_Comparator\\RCR-VR-OR-BO-Financial Transaction Universe-Revenue_1000.xlsx")
rb.save()