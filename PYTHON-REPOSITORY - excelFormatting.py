import smtplib
from email.message import EmailMessage
import smtplib
import pandas as pd
import numpy as np
import json
import xlsxwriter
from pymongo import MongoClient
from datetime import datetime, timedelta, date
import datetime as dt


try:
  connection = MongoClient('test-server-fds4dvs45ssvkf.westus2.cloudapp.azure.com:39186', username="Training", password="Training@123")
  db = connection.TestDb
except Exception as e:
  print(f"{e}")


def cell_format(data, method='', value=''):
    attr = [str(method) + ": " + str(value)]
    return pd.DataFrame(np.where(data, attr, attr), index=data.index, columns=data.columns)

def create_file():

    fromDate = dt.datetime(2021,3,12)
    fileName = str(dt.datetime.now().strftime('%Y%m%d')) + ' AttendanceLog.xlsx'
    query = list(db.AttendanceLog.find({"InTime": { "$gte": fromDate}}))
    df = pd.DataFrame(query)
    # df.replace("", 0, inplace=True)
    writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
    df = df.style.set_properties(**{'text-align': 'center', 'border-style': 'solid', 'border-width': '1Pt', 'color': 'black',
                                    'border-color': 'black', 'font-size': '12Pt'})
    df = df.apply(cell_format, method='border-style', value='solid', axis=None)
    df = df.apply(cell_format, method='border-color', value='black', axis=None)
    df = df.apply(cell_format, method='border-width', value='1Pt', axis=None)
    df = df.apply(cell_format, method='background-color', value='red', axis=None)
    columnName = df.columns
    df.to_excel(writer, sheet_name="test", index=False)
    workbook = writer.book
    worksheet = writer.sheets['test']
    header_format = workbook.add_format({ 'bold': True,'align': 'center','bg_color': 'ADFF2F','border': 1,'font_size': 13 })
    for col_num, val in enumerate(columnName.values):
        worksheet.write(0, col_num, val, header_format)
    workbook.close()

if __name__ == '__main__':
    create_file()







    # df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=0, startcol=0, header=True)
    # headerFormat = workbook.add_format({'bold': True, 'border': 1, 'align': 'center', 'font_size': 13,
    #                                      'font_color': 'red', 'border_color': 'black', 'bg_color': 'ADFF2F'})
    # attendanceWorksheet = writer.sheets['Sheet1']
    # for colNum, value in enumerate(df.columns.values):
    #     attendanceWorksheet.write(0, colNum + 0, value, headerFormat)
    # borderFormat = workbook.add_format({'bold': False, 'align':'left', 'font_color': 'black', 'border': 1})
    # attendanceWorksheet.set_column('A:X', 15, borderFormat)
    # attendanceWorksheet.conditional_format( 'A2:X6' , { 'type' : 'no_blanks' , 'format' : borderFormat} )
    # writer.save()

# https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html










