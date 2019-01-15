from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Siebel import Souilib
from ITAFRepo.Dev.Excel import XLLib
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import *
import time
browser = 'gc'
url = 'http://stage-o2/v2/Documents/Edit/152/'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
runmanagerfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisRunManager.xlsx'
runmanagersheet = 'RunManager'
testdatafile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisDataBank.xlsx'

iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)
xllib = XLLib.XLLib()
rundict = xllib.load_xl_cell_values_dictionary(runmanagerfile, runmanagersheet)
print(rundict)
for key,value in rundict.items():
    print('key is ' + str(key))
    print('value is ' + str(value))

for row in range(2,XLLib.get_xl_row_count(runmanagersheet,runmanagersheet)):
    print('row ')
    print(str(row))
    print(XLLib.get_table_row_as_dictionary(row, rundict))
    run = XLLib.get_table_row_as_dictionary(row, rundict)
    if
    contentmanagement_page.add_whitepaper(XLLib.get_table_row_as_dictionary(row, tabledictinoary))
    time.sleep(30)



"""

testdatasheet = 'DataBank'
datadict = xllib.load_xl_cell_values_testrail_dictionary(testdatafile, testdatasheet)

print('Datadict')
print(datadict)
print('Rundict')
print(rundict)

utillib = Utillib.utillib(globaldict)
driver = utillib.get_driver_handle(browser)

seleniumutil = Seleniumutil.Seleniumutil(driver,globaldict)
seleniumutil.launch_url(url)

whitepaper = 'Test whitepaper12_20 hidden'
#whitepaper = 'Siebel Overview'
waitime = 30

contentmanagement_page = contentmanagementpage.contentmanagementpage(driver,globaldict,datadict,'1')

contentmanagement_page.Search_for_whitepaper(whitepaper)
time.sleep(10)
print('******---')
print(contentmanagement_page.get_whitepaper_details(whitepaper))
contentmanagement_page.click_on_whitepaper(whitepaper)

print(seleniumutil.get_webpage_url())
print('******')
"""