import pandas as pd
import openpyxl
offset = 0

def write_to_excel(row):
    data = df1.loc[row:row]
    global offset
    if offset == 0:
        offset += len(data)
        data.to_excel(writer)
    else:
        offset += len(data)
        data.to_excel(writer,header=False,startrow=offset)

    # row.to_excel(writer)

diff = []
df1 = pd.read_excel('1.xlsx')
df2 = pd.read_excel('2.xlsx')
writer = pd.ExcelWriter("temp.xlsx")
df1=df1.fillna("no_data")
df2=df2.fillna("no_data")
col1_name = pd.Series(df1.columns.values, name='x')
col2_name = pd.Series(df2.columns.values, name='x')
df1_matrix = df1.shape
df2_matrix = df2.shape
print(df1_matrix)
print(df2_matrix)
for r in range(0,df1_matrix[0]):
    for c in col1_name:
        if df1.loc[r,c] == df2.loc[r,c]:
            continue
        else:
            difference = df1.loc[r,c]
            write_to_excel(r)

col_df1 = [col for col in df1.columns]
col_df2 = [col for col in df2.columns]
if len(col1_name) == len(col2_name) and set(col_df1) == set(col_df2):
    offset = 0
    for i in col_df1:
        col_inner_1 = df1[i]
        col_inner_2 = df2[i]
        if len(col_inner_1)==len(col_inner_2) and set(col_inner_1)==set(col_inner_2):
            continue
    #        print("The values are all correct in the tables")
        else:
            difference = col_inner_1[col_inner_1 != col_inner_2]
            offset += len(i)
            difference.to_excel(writer,header=True, sheet_name="sheet2",startrow=offset)


# diff.to_excel(writer,header=True, sheet_name="sheet2",startrow=offset)
# for i in diff:
#     print(i)
#     if offset == 0:
#         offset += len(i)
#         i.to_excel(writer,sheet_name="sheet2")
#     else:
#         offset += len(i)
#         i.to_excel(writer,header=True, sheet_name="sheet2",startrow=offset)
writer.save()
