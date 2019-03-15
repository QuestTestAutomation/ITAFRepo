import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailUser = 'art.cognizant1@gmail.com'
gmailPassword = 'Quest@123'
recipient = 'seshikanth.anumolu@quest.com'
message='your message here '

msg = MIMEMultipart()
msg['From'] = gmailUser
msg['To'] = recipient
msg['Subject'] = "Subject of the email"
msg.attach(MIMEText(message))

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmailUser, gmailPassword)
mailServer.sendmail(gmailUser, recipient, msg.as_string())
mailServer.close()
"""
user = 'art.cognizant1@gmail.com'
pwd = 'Quest@123'
recipient = 'seshikanth.anumolu@quest.com'
subject = 'Hello from Python'
body = 'Email Body'
FROM = user
TO = recipient if isinstance(recipient, list) else [recipient]
SUBJECT = subject
TEXT = body

# Prepare actual message
message = 
"""
#From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(user, pwd)
server.sendmail(FROM, TO, message)
server.close()
print('successfully sent the mail')
"""
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
except:
    print("failed to send mail")
"""