import smtplib
from email.mime.text import MIMEText

to = ['Email2dbuat1@quest.com']
cc = ['qstaf.testautomation@gmail.com']
#subject = '|SR Number:' + sr + '|'
gmail_user = 'art.cognizant1@gmail.com'
gmail_pwd = 'Quest@123'

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

smtpserver.login(gmail_user, gmail_pwd)
to1 = ['support@quest.com']
header = 'To:' + ", ".join(to) + '\n' + 'CC:' + ", ".join \
    (cc) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + to1 + '\n'
msg = header + '\n' + to1 + '\n\n'
print(header)
smtpserver.sendmail(gmail_user, to, msg)

to2 = ['license@quest.com']
header = 'To:' + ", ".join(to2) + '\n' + 'CC:' + ", ".join \
    (cc) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + 'license@quest.com' + '\n'
msg = header + '\n' + 'license@quest.com' + '\n\n'
print(header)
smtpserver.sendmail(gmail_user, to, msg)

to3 = ['OPLR@quest.com']
header = 'To:' + ", ".join(to3) + '\n' + 'CC:' + ", ".join \
    (cc) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + 'OPLR@quest.com' + '\n'
msg = header + '\n' + 'OPLR@quest.com' + '\n\n'
print(header)
smtpserver.sendmail(gmail_user, to3, msg)

to4 = ['QDL.LSO.Team@quest.com']
header = 'To:' + ", ".join(to) + '\n' + 'CC:' + ", ".join \
    (cc) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + to4 + '\n'
msg = header + '\n' + to4 + '\n\n'
print(header)
smtpserver.sendmail(gmail_user, to4, msg)

to5 = ['supportadmin@quest.com']
header = 'To:' + ", ".join(to5) + '\n' + 'CC:' + ", ".join \
    (cc) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + to5 + '\n'
msg = header + '\n' + to5 + '\n\n'
print(header)
smtpserver.sendmail(gmail_user, to5, msg)