import pandas

excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='wine')

# print whole sheet data
print(excel_data_df)