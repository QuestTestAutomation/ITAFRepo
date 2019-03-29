from selenium import webdriver
from Dev.Utilities import Utillib
from Dev.Utilities import InitializeITAF
from Dev.Utilities import Seleniumutil
from Dev.Siebel import Souilib
from Dev.Excel import XLLib
from Dev.Utilities import Seleniumutil
from Dev.Marketing.Libs.PageObjectLibrary import *
#from Dev.Marketing.Libs import MarketingLib
from Dev.TestRails import ITAFTestRailLibrary
from Dev.Siebel import Siebelservicelib

import time
browser = 'gc'
url = 'http://google.co.in'
suser ='SUPPORT_ADMIN'
spassword = 'SUPPORT_ADMIN'
Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
runmanagerfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Siebel Service/RunManager_Service v3.0.xlsx'
runmanagersheet = 'RunManager'
databankfile = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Siebel Service/ITAF_DataBank_Service.xlsx'
trresultdict = {}

iniittaf = InitializeITAF.initializeITAF()
globaldict = iniittaf.set_global_dictionary(Variablesfile)
print('globaldict')
print(globaldict)
tlibe = ITAFTestRailLibrary.TestRailLibraryExt(globaldict['TestRailURL'], globaldict['TestRailUser'], globaldict['TestRailPassword'])
trailproject = 'Siebel'
trailrun = 'Siebel Regression 29Mar2019'
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
rundicttemp = {}
#siebelservicelib = Siebelservicelib.Siebelservicelib(driver,globaldict,url,rundicttemp)
textresultsfolder = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Files/Siebel Service/Results/'
textresultsfile =  textresultsfolder + 'SiebelService_' + str(utillib.get_current_date_time()) + '.txt'
resultsfile = open(textresultsfile, 'x')
srtextresultsfile =  textresultsfolder + 'SiebelService_' + str(utillib.get_current_date_time()) + '_sr.txt'
srresultsfile = open(srtextresultsfile, 'x')
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
            url = data['Url']
            siebelservicelib = Siebelservicelib.Siebelservicelib(driver, globaldict, url, data)
            if data['ID'].upper() == run['ID'].upper():
                stepno = 0
                for function in functionlist:
                    print('function')
                    print(function)

                    stepno = stepno + 1

                    func = getattr(siebelservicelib, function)
                    print('str(stepno)')
                    print(str(stepno))
                    stepdict = func()
                    print('**************************************999999999999999999999')
                    print(stepdict)
                    tempdict = {}
                    if stepno == 1:
                        if not stepdict['actual'] is None:

                            #sr = stepdict['actual']
                            srresultsfile.write(str(stepdict['actual']))
                    tempdict['content'] = 'step' + str(stepno)
                    if stepdict['expected'] is None:
                        tempdict['expected'] = 'As Expected'
                    else:
                        tempdict['expected'] = stepdict['expected']
                    if stepdict['actual'] is None:
                        tempdict['expected'] = 'As, Expected'
                    else:
                        tempdict['actual'] = stepdict['actual']
                    if stepdict['status_id'] is None:
                        tempdict['status_id'] = '1'
                    else:
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
                resultsfile.write(str(customresultsdictlist))
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
