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


souilib = SOUILib.Souilib(driver,globaldict,url)
souilib.Login_lite(url,suser,spassword)
souilib.click_sitemap()
time.sleep(5)
#souilib.click_sitemap_screen_link('Accounts')
#time.sleep(2)
#souilib.click_sitemap_screen_view_linkid('Accounts List','1')
#souilib.click_sitemap_screen_view_linkid('Accounts List','1')
#souilib.click_sitemap_screen_view_linkid('Activities','3')
#time.sleep(2)
#souilib.click_view_link('Accounts Administration','L2','1')
#souilib.click_view_link('Assets','L3','1')
#souilib.click_view_link('Support Account Team','L3','1')
souilib.click_view_link('All Activities','L4','1')
#seleniumutil.launch_url(url)

souilib.click_view_link('Service','L1','1')
time.sleep(8)
souilib.click_button('New',1)
time.sleep(8)
#print(souilib.get_list_applet_column_id('SR #','1','1'))
#print(souilib.get_list_applet_table_id(1))
#print(souilib.get_list_applet_column_value('SR #','1','1','1'))
#souilib.press_keyboard_tab()
#souilib.drilldown_on_list_applet_column('SR #','1','1','3')
#time.sleep(5)
#souilib.drilldown_on_list_applet_column('Type','1','1','2')
#time.sleep(10)
#souilib.click_on_threadbar_link('1')
souilib.get_form_field_name('SR #')



