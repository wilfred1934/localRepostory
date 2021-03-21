import smtplib
import datetime as dt
import pandas as pd
import xlsxwriter
from pymongo import MongoClient
from datetime import datetime, timedelta, date

try:
  connection = MongoClient('test-server-fds4dvs45ssvkf.westus2.cloudapp.azure.com:39186', username="Training", password="Training@123")
  db = connection.TestDb
except Exception as e:
  print(f"{e}")



gmail_user = 'dwilfred2021@gmail.com'
gmail_password = 'dsouza@1934'

sent_from = gmail_user
to = ['wilfred.dsouza@liradolf.com', 'wilfred.dsouza94@ymail.com', 'chaturgirish151@gmail.com']
subject = "Important Message"
body = "Hey, what's up???"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
