
# import smtplib
# from email.message import EmailMessage



# EMAIL_ADDRESS = 'dwilfred2021@gmail.com'
# EMAIL_PASSWORD = 'dsouza@1934'



# Recipients = "wilfred.dsouza@liradolf.com,wilfred.dsouza94@ymail.com"

# recipients = Recipients
# recipients = recipients.split(',')
# msg = EmailMessage()
# msg['Subject'] = 'Grab dinner this weekend?'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = ", ".join(recipients)
# msg.set_content('How about dinner at 6pm this Saturday?')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     smtp.send_message(msg)



# import smtplib
# from email.message import EmailMessage

# SENDER_EMAIL = 'dwilfred2021@gmail.com'
# EMAIL_PASSWORD = 'dsouza@1934'

# Recipients = "wilfred.dsouza@liradolf.com,wilfred.dsouza94@ymail.com,chaturgirish151@gmail.com"

# recipients = Recipients
# recipients = recipients.split(',')
# msg = EmailMessage()
# msg['Subject'] = 'Attached attendance log with this mail.'
# msg['From'] = SENDER_EMAIL
# msg['To'] = ", ".join(recipients)
# msg.set_content("pls check the attachment")

# with open('Attendance1.xlsx', 'rb') as f:
#     file_data = f.read()
#     file_name = f.name
# msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
#     smtp.send_message(msg)



import smtplib
from email.message import EmailMessage

SENDER_EMAIL = 'dwilfred2021@gmail.com'
EMAIL_PASSWORD = 'dsouza@1934'

Recipients = "wilfred.dsouza@liradolf.com,wilfred.dsouza94@ymail.com"

recipients = Recipients
recipients = recipients.split(',')
msg = EmailMessage()
msg['Subject'] = 'Attached attendance log with this mail.'
msg['From'] = SENDER_EMAIL
msg['To'] = ", ".join(recipients)
msg.set_content("pls check the attachment")

with open('Attendance1.xlsx', 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
    smtp.send_message(msg)
