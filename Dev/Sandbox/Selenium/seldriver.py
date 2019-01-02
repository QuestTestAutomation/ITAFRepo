from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Siebel import SOUILib
import time
browser = 'gc'
url = 'http://siebeluat.prod.quest.corp/dbsupport_enu/start.swe?SWECmd=AutoOn'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)

utillib = Utillib.utillib(globaldict)
driver = utillib.get_driver_handle(browser)

#seleniumutil = seleniumutil.seleniumutil(driver,globaldict,url)
#osoullib = SOUILib.SOUILib(driver,globaldict,url)


SOUILibobj = SOUILib.Souilib(driver,globaldict,url)
SOUILibobj.Login_lite(url,suser,spassword)

#seleniumutil.launch_url(url)



