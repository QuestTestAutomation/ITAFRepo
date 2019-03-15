import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("art.cognizant1@gmail.com", "Quest@123")
server.sendmail(
  "from@address.com",
  "to@address.com",
  "this message is from python")
server.quit()