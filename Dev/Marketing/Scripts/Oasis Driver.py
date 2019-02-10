from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Utilities import InitializeITAF
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Siebel import Souilib
from ITAFRepo.Dev.Excel import XLLib
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import *
from ITAFRepo.Dev.Marketing.Libs import MarketingLib
from ITAFRepo.Dev.TestRails import ITAFTestRailLibrary

import time
browser = 'ff'
url = 'http://stage-o2/v2/Documents/Edit/152/'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
runmanagerfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisRunManager.xlsx'
runmanagersheet = 'RunManager'
databankfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Marketing/OasisDataBank.xlsx'
trresultdict = {}

iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)
tlibe = ITAFTestRailLibrary.TestRailLibraryExt(globaldict['TestRailURL'], globaldict['TestRailUser'], globaldict['TestRailPassword'])
trailproject = 'Information Services Marketing'
trailrun = 'Marketing Automation POC - Demo'
trailrunid = tlibe.Get_TestRail_RunID(tlibe,trailproject ,trailrun)
print('trailrunid' + str(trailrunid))
xllib = XLLib.XLLib()
rundict = xllib.load_xl_cell_values_dictionary(runmanagerfile, runmanagersheet)
print(rundict)
print('row count ' + str(xllib.get_xl_row_count(runmanagerfile,runmanagersheet)))
#for key,value in rundict.items():
#    print('key is ' + str(key))
#    print('value is ' + str(value))
utillib = Utillib.utillib(globaldict)
driver = utillib.get_driver_handle(browser,url)

marketinglib = MarketingLib.MarketingLib(driver,globaldict)
resultsdirectory = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Results/Siebel Service'


for row in range(2,(int(xllib.get_xl_row_count(runmanagerfile,runmanagersheet) + 1))):
    #print('row ')
    #print(str(row))
    #print(xllib.get_table_row_as_dictionary(row, rundict))
    run = xllib.get_table_row_as_dictionary(row, rundict)
    if run['Run'].upper() == 'Y':
        print(run['ID'])
        print(run['ID'][1:])
        print(run['Function'])
        print('Execute')
        #etattr(globals()['XLLib'](), run['Function'])()
        # Get the function (from the instance) that we need to call
        functionlist = run['Function'].split(';')
        databanksheet = run['Datasheet']
        datadict = xllib.load_xl_cell_values_dictionary(databankfile, databanksheet)
        customresultsdictlist = []
        #get the Data dictinoary for execution
        for datarow in range(2, (int(xllib.get_xl_row_count(databankfile, databanksheet) + 1))):
            data = xllib.get_table_row_as_dictionary(datarow, datadict)
            if data['ID'].upper() == run['ID'].upper():
                stepno = 0
                for function in functionlist:
                    print(function)
                    stepno = stepno + 1
                    func = getattr(marketinglib, function)
                    print('str(stepno)')
                    print(str(stepno))
                    stepdict = func(data)
                    print('**************************************999999999999999999999')
                    print(stepdict)
                    tempdict = {}
                    tempdict['content'] = 'step' + str(stepno)
                    tempdict['expected'] = stepdict['expected']
                    tempdict['actual'] = stepdict['actual']
                    tempdict['status_id'] = stepdict['status_id']
                    customresultsdictlist.append(tempdict)
                    print(customresultsdictlist)

                print('customresultsdictlist')
                print(customresultsdictlist)
                trailscaseid = data['ID'][1:]
                result = {
                    "status_id": stepdict['status_id'],
                    "comment": "This is a comment",
                    "custom_step_results": customresultsdictlist

                }
                trurlstring = "add_result_for_case/" + str(trailrunid) + "/" + str(trailscaseid)
                tlibe.Add_Result_To_TestRail_Case_details(trailproject, trailrun, trailscaseid, result)
                time.sleep(10)
                break





    elif run['Run'].upper() == 'N':
        print(run['ID'])
        print('Dont Execute')



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
