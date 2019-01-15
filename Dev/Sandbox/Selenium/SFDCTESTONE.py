from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.SFDC import Sfdclib
from ITAFRepo.Dev.Siebel import Souilib
import time
browser = 'gc'
url = 'https://questsoftware--devfull.cs25.my.salesforce.com'
#url = 'https://questsoftware--devfull.cs25.my.salesforce.com/a4m1400000014vT'
suser ='sanumolu@quest.com.devfull'
spassword = 'testing@123'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)

utillib = Utillib.utillib(globaldict)
driver = utillib.get_driver_handle(browser)

sfdclib = Sfdclib.Sfdclib(driver,globaldict)
#sfdclib.launch_url(url)
sfdclib.login_into_sfdc(url,suser,spassword)
"""

print(sfdclib.get_text_column_value('quote number','1'))
print(sfdclib.get_text_column_value('Account','1'))
print(sfdclib.get_text_column_value('Status','1'))
print(sfdclib.get_text_column_value('Owner','1'))
print(sfdclib.get_text_column_value('Quote Comments','1'))
print(sfdclib.get_text_column_value('Overall Discount %','1'))
print(sfdclib.get_text_column_value('ship to account','1'))
"""
time.sleep(30)
sfdclib.click_screen_link('Accounts','1')
time.sleep(10)
sfdclib.click_screen_link('Documents','1')
time.sleep(10)
sfdclib.click_screen_link('Accounts','1')
time.sleep(5)
sfdclib.click_button('New',1)