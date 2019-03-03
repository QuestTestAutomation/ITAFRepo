from  ITAFRepo.Dev.GMAILAPI.GmailAPILib import *

to = "seshikanth.anumolu@quest.com"
sender = "art.cognizant1@gmail.com"
subject = "subject test1"
message_text_html = r'Hi<br/>Html <b>hello</b>'
message_text_plain = "Hi\nPlain Email this email is sent from Lib"
attached_file = r'C:\Users\sanumolu\Downloads\master.csv'
create_message_and_send(sender,to,subject, message_text_plain, message_text_html, attached_file)