from  ITAFRepo.Dev.GMAILAPI.GmailAPILib import *

to = "seshikanth.anumolu@quest.com"
sender = "art.cognizant1@gmail.com"
subject = "subject test1"
message_text_html = r'Hi<br/>Html <b>hello</b>'
message_text_plain = "Hi\nPlain Email this email is sent from Lib"
attached_file = r'C:\Users\sanumolu\Downloads\master.csv'
create_message_and_send(sender,to,subject, message_text_plain, message_text_html, attached_file)

SRS = ['4405345','4405346','4405347','4405348','4405349','4405350','4405351','4405352','4405353','4405354','4405355','4405356','4405357']

for sr in SRS:
    for m in range (1,3):
        to = 'Email2dbuat1@quest.com'
        subject = '|SR Number:' + sr + '|'
        create_message_and_send(sender, to, subject, message_text_plain, message_text_html, attached_file)