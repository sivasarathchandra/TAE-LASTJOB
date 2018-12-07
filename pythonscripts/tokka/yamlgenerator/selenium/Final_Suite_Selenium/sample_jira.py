import pandas as pd

df1 = pd.read_excel('1.xlsx')
df2 = pd.read_excel('2.xlsx')
df1=df1.fillna("no_data")
df2=df2.fillna("no_data")
col1_name = pd.Series(df1.columns.values, name='x')
col2_name = pd.Series(df2.columns.values, name='x')
df1_matrix = df1.shape
df2_matrix = df2.shape
print(df1_matrix[0])
print(df2_matrix[0])
# for i in range(1,3):
#     print("====================")
#     df1_row = [df1.head(i)]
#     df2_row = [df2.head(i)]
#     print(df1_row)
#     print(df2_row)
#     if df1_row==df2_row:
#         print("i am good")
#     else:
#         print("get lost")
#     print("lines are going on")

col_df1 = [col for col in df1.columns]
col_df2 = [col for col in df2.columns]
if len(col1_name) == len(col2_name) and set(col_df1) == set(col_df2):
    print("both col are same as what we thought..")

    for i in col_df1:
        col_inner_1 = df1[i]
        col_inner_2 = df2[i]
        if len(col_inner_1)==len(col_inner_2) and set(col_inner_1)==set(col_inner_2):
            continue
    #        print("The values are all correct in the tables")
        else:
            difference = col_inner_1[col_inner_1 != col_inner_2]
            print(i)
            print(difference)
        print("The values are all correct in the tables")

# data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]


# print(dataframe1)
# print(dataframe2)
# difference = df1[df1!=df2]
# print(difference)