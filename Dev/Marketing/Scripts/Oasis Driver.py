from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Siebel import Souilib
from ITAFRepo.Dev.Excel import XLLib
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import contentmanagementpage
import time
browser = 'gc'
url = 'http://stage-o2/v2/Documents/Edit/152/'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
runmanagerfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisRunManager.xlsx'
runmanagersheet = 'RunManager'
testdatafile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisDataBank.xlsx'
testdatasheet = 'DataBank'
iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)
xllib = XLLib.XLLib()
datadict = xllib.load_xl_cell_values_testrail_dictionary(testdatafile, testdatasheet)
rundict = xllib.load_xl_cell_values_testrail_dictionary(runmanagerfile, runmanagersheet)
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
