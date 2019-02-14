from selenium import webdriver
from Poc1.Lib import Utillib
from Poc1.Lib.PageObjectLibrary.Todeletecnt import contentmanagement
from Poc1.Lib.PageObjectLibrary.cmgmt import contentmanagementobj1
from Poc1.Lib import TestRailLibraryExt
from Poc1.Lib import Utillib
from Poc1.Lib import XLLib





appurl = "http://stage-o2"
waitime = 30

"""

Datasheet = "C:/MTAF/01 Test Data/MTAF Oasis Data Sheet.xlsx"
TestRailURL = 'https://tr.labs.quest.com/testrail/'
TestRailUser = 'seshikanth.anumolu@quest.com'
TestRailPassword = 'P@ssw0rd@23'
project_name = "MS Patching"
run_name = "MS Patching December 2018"

tlibe = TestRailLibraryExt.TestRailLibraryExt(TestRailURL, TestRailUser, TestRailPassword)
runid = tlibe.Get_TestRail_RunID(tlibe,project_name,run_name)
print("runid")
print(runid)
XLLib = XLLib.XLLib()
sheet = "Data"
tabledictinoary = XLLib.load_xl_cell_values_dictionary(Datasheet,sheet)
print(tabledictinoary)

tableheaderdictinoary = tuple(XLLib.get_table_row_as_dictionary(1,tabledictinoary))
print(tableheaderdictinoary)
tablerowdictinoary = XLLib.get_table_row_as_dictionary(1, tabledictinoary)
"""
"""

for i in range(2,len(tabledictinoary)):
    print(i)
    tablerowdictinoary = XLLib.get_table_row_as_dictionary(i,tabledictinoary)
    print(tablerowdictinoary)
"""


utillib = Utillib.utillib()
driver = utillib.Get_Driver_Handle(utillib,"gc")

#mainpage = contentmanagementobj1(driver,appurl,waitime)
mainpage = contentmanagement(driver,appurl,waitime)
mainpage.Lauch_url()
mainpage.add_whitepaper()
#mainpage.Add_Whitepaper(**tablerowdictinoary)

