from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Siebel import Souilib
from ITAFRepo.Dev.Siebel import SiebelLib
from ITAFRepo.Dev.Excel import XLLib

import time
browser = 'gc'
url = 'http://siebeluat.prod.quest.corp/dbsupport_enu/start.swe?SWECmd=AutoOn'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
runmanagerfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Siebel Servic/RunManager_Service.xlsx'
runmanagersheet = 'RunManager'
testdatafile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Siebel Service/DataBank_Service.xlsx'
testdatasheet = 'DataBank'
iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)
xllib = XLLib.XLLib()
datadict = xllib.load_xl_cell_values_dictionary(testdatafile, testdatasheet)
rundict = xllib.load_xl_cell_values_dictionary(runmanagerfile, runmanagersheet)
print('Datadict')
print(datadict)
print('Rundict')
print(rundict)
datarow = 1
rowdict = xllib.get_table_row_as_dictionary(datarow, datadict)
print('Rowdict')
print(rowdict)
utillib = Utillib.utillib(globaldict)
driver = utillib.get_driver_handle(browser,url)
seleniumutil = Seleniumutil.Seleniumutil(driver,globaldict)
osouilib = Souilib.Souilib(driver,globaldict,url)
sblib = SiebelLib.siebellib(driver, globaldict, url,datadict, rundict,rowdict)
osouilib.Login_lite(url,suser,spassword)
sblib.create_sr()
sblib.update_SR_substatus('Assigned')
sblib.update_sr_status('Deleted')
#sblib.query_contact()
#recordcount = osouilib.get_record_count()







"""


#seleniumutil = seleniumutil.seleniumutil(driver,globaldict,url)
#osoullib = SOUILib.SOUILib(driver,globaldict,url)


souilib = Souilib.Souilib(driver, globaldict, url)
souilib.Login_lite(url,suser,spassword)
souilib.open_ui_sync()
souilib.click_sitemap()
souilib.open_ui_sync()
#time.sleep(5)
#souilib.click_sitemap_screen_link('Accounts')
#time.sleep(2)
#souilib.click_sitemap_screen_view_linkid('Accounts List','1')
#souilib.click_sitemap_screen_view_linkid('Accounts List','1')
#souilib.click_sitemap_screen_view_linkid('Activities','3')
#time.sleep(2)
#souilib.click_view_link('Accounts Administration','L2','1')
#souilib.click_view_link('Assets','L3','1')
#souilib.click_view_link('Support Account Team','L3','1')
#souilib.click_view_link('All Activities','L4','1')
#seleniumutil.launch_url(url)

#souilib.click_view_link('Service','L1','1')
#time.sleep(8)
#souilib.click_button('New',1)
#time.sleep(8)
#print(souilib.get_list_applet_column_id('SR #','1','1'))
#print(souilib.get_list_applet_table_id(1))
#print(souilib.get_list_applet_column_value('SR #','1','1','1'))
#souilib.press_keyboard_tab()
#souilib.drilldown_on_list_applet_column('SR #','1','1','3')
#time.sleep(5)
#souilib.drilldown_on_list_applet_column('Type','1','1','2')
#time.sleep(10)
#souilib.click_on_threadbar_link('1')
#souilib.get_form_field_name('SR #')
#souilib.get_form_textarea_name('Description')
#souilib.set_form_applet_input_value('External SR #','SuR123')
#souilib.select_form_applet_input_value('Type','Support Admin')
#time.sleep(2)
#souilib.set_form_applet_textarea_value('Summary','This is summary')


souilib.click_sitemap_screen_view_linkid('Accounts Administration','1')
souilib.open_ui_sync()
#time.sleep(10)
souilib.wait_for_button('New','1')
souilib.click_button('New','1')

souilib.set_list_applet_column_value('Site',1,1,1,'Test Account Site')
time.sleep(3)
souilib.set_list_applet_column_value('Account Name',1,1,1,'Test Account')
time.sleep(3)
souilib.set_list_applet_column_value('Account Type',1,1,1,'Commercial')
time.sleep(3)
souilib.set_list_applet_column_value('Main Phone #',1,1,1,'9196754421')
time.sleep(3)
souilib.save_record()
#souilib.set_list_applet_column_value()

"""







