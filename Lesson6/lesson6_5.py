import openpyxl
import pandas
from openpyxl.utils.dataframe import dataframe_to_rows

wb=openpyxl.Workbook()
ws=wb.active

data= pandas.read_csv('less6_4.csv',sep=',',skip_blank_lines=True)
print(data.columns)
data.drop(columns='age', axis='columns', inplace= True)
data.index=data.index+1
data2=data.transpose().add_prefix('person ')
print(data2)
for row in dataframe_to_rows(data2, index=True,header=True):
    ws.append(row)
ws.delete_rows(2)
wb.save('less6_5.xlsx')