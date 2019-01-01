"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("art.cognizant1@gmail.com", "Quest@123")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("art.cognizant1@gmail.com", "seshikanth.anumolu@quest.com", "test message")