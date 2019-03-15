import smtplib
#smtpObj = smtplib.SMTP_SSL('smtp.gmail.com')
#smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
smtpObj = smtplib.SMTP('smtp.gmail.com')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('art.cognizant1@gmail.com', 'Quest@123')
smtpObj.sendmail('art.cognizant1@gmail.com', 'seshikanth.anumolu@quest.com', 'Subject: SubjectText.\nMessage Text')
smtpObj.quit()