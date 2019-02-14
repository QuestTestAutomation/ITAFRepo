from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
#from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import contentmanagement
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary  import contentmanagementpage
from ITAFRepo.Dev.TestRails import ITAFTestRailLibrary
from ITAFRepo.Dev.Excel import XLLib
import time

appurl = "http://stage-o2"
waitime = 30

Datasheet = "C:/MTAF/01 Test Data/Oasis Data Sheet 1.xlsx"
TestRailURL = 'https://tr.labs.quest.com/testrail/'
TestRailUser = 'seshikanth.anumolu@quest.com'
TestRailPassword = 'P@ssw0rd@23'
project_name = "MS Patching"
run_name = "MS Patching December 2018"

tlibe = ITAFTestRailLibrary.TestRailLibraryExt(TestRailURL, TestRailUser, TestRailPassword)
runid = tlibe.Get_TestRail_RunID(tlibe,project_name,run_name)
print("runid")
print(runid)
XLLib = XLLib.XLLib()
sheet = "Data"
tabledictinoary = XLLib.load_xl_cell_values_dictionary(Datasheet,sheet)
print('*****' + str(tabledictinoary))

tableheaderdictinoary = tuple(XLLib.get_table_row_as_dictionary(1,tabledictinoary))
print(tableheaderdictinoary)
tablerowdictinoary = XLLib.get_table_row_as_dictionary(2, tabledictinoary)


utillib = Utillib.utillib()
driver = utillib.Get_Driver_Handle(utillib,"gc")

contentmanagement_page = contentmanagement(driver,appurl,waitime)
#mainpage.add()
for row in range(2,XLLib.get_xl_row_count(Datasheet,sheet)):
    print('row ')
    print(str(row))
    print(XLLib.get_table_row_as_dictionary(row, tabledictinoary))
    contentmanagement_page.add_whitepaper(XLLib.get_table_row_as_dictionary(row, tabledictinoary))
    time.sleep(30)
