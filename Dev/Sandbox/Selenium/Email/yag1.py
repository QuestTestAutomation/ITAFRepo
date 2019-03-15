import yagmail
yag = yagmail.SMTP('art.cognizant1@gmail.com')
yag.send('seshikanth.anumolu@quest.com', subject = 'Hi', contents = 'Hello')