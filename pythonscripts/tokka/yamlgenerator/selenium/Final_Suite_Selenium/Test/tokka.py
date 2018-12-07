import os
import pandas as pd

files = [x for x in os.listdir('C:\\Users\\SC057441\\Desktop\\') if x.startswith("query-results")]
pd.read_csv('C:\\Users\\SC057441\\Desktop\\'+files[0], delimiter=",").to_excel('C:\\Users\\SC057441\\Desktop\\'+'tokka.xlsx', index=False)
# with open('C:\\Users\\SC057441\\Desktop\\'+"tokka"+".xlsx", 'w') as tokkafile:
#     with open('C:\\Users\\SC057441\\Desktop\\' + files[0], 'r') as readfile:
#         for line in readfile:
#             line = line.split(',')
#             print(line)
#             for i in line:
#                 tokkafile.write(i)