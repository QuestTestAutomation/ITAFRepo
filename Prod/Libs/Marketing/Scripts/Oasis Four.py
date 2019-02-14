from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import contentmanagementpage
from ITAFRepo.Dev.TestRails import ITAFTestRailLibrary
from ITAFRepo.Dev.Excel import XLLib
import time

appurl = "http://stage-o2/v2/Documents/Edit/152/"
waitime = 30
whitepaper = 'Test whitepaper12_20 hidden'
#whitepaper = 'Siebel Overview'
utillib = Utillib.utillib()
driver = utillib.Get_Driver_Handle(utillib,"gc")

contentmanagement_page = contentmanagementpage(driver,appurl,waitime)

contentmanagement_page.Search_for_whitepaper(whitepaper)
time.sleep(10)
print('******---')
print(contentmanagement_page.get_whitepaper_details(whitepaper))
print('******')

