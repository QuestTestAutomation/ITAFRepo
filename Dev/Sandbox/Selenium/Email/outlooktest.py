"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

#Next, log in to the server
server.login("dsg.art@outlook.com", "testing@123")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("dsg.art@outlook.com", "seshikanth.anumolu@quest.com", msg)