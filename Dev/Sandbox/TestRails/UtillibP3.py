
import time
import os
from Sandbox.Libraries.Dev.XLLib import *
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import inspect



def Hello_World():
    print("Hello World")

def Open_Browser_And_Launch_Application(brow,url):
    if brow ==  'ff':
        driver = webdriver.Firefox()
     #   driver.get(url)
    if brow ==  'gc':
        driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        #driver = webdriver.Chrome()
        # driver.get(url)
        # driver = webdriver.Remote(command_executor='http://localhost:9515/',desired_capabilities=DesiredCapabilities.CHROME)
        # driver.get(url)
    if brow == 'ie':
        driver = webdriver.Ie()
    return driver


def get_webdriver_instance():
    se2lib = BuiltIn().get_library_instance('Selenium2Library')
    return se2lib._current_browser()


def increment_step_number(step):
    step = int(step) + int(1)

    return step

def generate_phonenum() :
    phnum = time.strftime("%d%m%Y%H%M%S")

    return phnum

def get_current_date():
    print (time.strftime("%H:%M:%S"))

    ## 12 hour format ##
    print (time.strftime("%I:%M:%S"))

    ## dd/mm/yyyy format
    print (time.strftime("%d/%m/%Y"))

    ## dd_mm_yyyy format
    print (time.strftime("%d_%m_%Y"))

    dttime = time.strftime("%d_%m_%Y")

    return dttime

def get_current_date_time():
    print (time.strftime("%H:%M:%S"))

    ## 12 hour format ##
    print (time.strftime("%I:%M:%S"))

    ## dd/mm/yyyy format
    print (time.strftime("%d/%m/%Y"))

    ## dd_mm_yyyy format
    print (time.strftime("%d_%m_%Y"))

    dttime = time.strftime("%d_%m_%Y_%H_%M_%S")

    return dttime

def create_directory(file):
    if not os.path.isdir(file):
        os.makedirs(file)
        print "Folder created successfully"
    else:
        print "Folder already exist."


def Add_Strings(Str1,Str2):
    str3 = Str1.strip() + Str2.strip()

    return str3

def Build_File_Path(Str1,Str2):
    str3 = Str1.strip() + "/" +  Str2.strip()

    return str3

def create_run_test_results_file(vTestResultsfile,vTestResultsheet):
    XLLib.Create_Workbook(vTestResultsfile,vTestResultsheet)
    XLLib.set_XL_cell_value(vTestResultsfile,vTestResultsheet,1,1,"TestCaseName")
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, 1, 2, "TestCaseDescription")
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, 1, 3, "Status")
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, 1, 4, "UpdatedDateTimeStamp")
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, 1, 5, "TestData")

def create_test_case_results_file(vTestCaseResultsfile,vTestCaseResultsheet,vTCName,vTCDescription):
    XLLib.Create_Workbook(vTestCaseResultsfile, vTestCaseResultsheet)
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 1, 1, "TestCaseName")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 1, 2, vTCName)
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 1, 3, "TestCaseDescription")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 1, 4,vTCDescription)

    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 1, "Test Case Steps")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 2,"Action")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 3, "Expected Result")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 4, "Actual Result")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 5, "Execution Status")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 6, "Comments")
    XLLib.set_XL_cell_value(vTestCaseResultsfile, vTestCaseResultsheet, 3, 7, "DateTime")

def update_run_test_results_file(vTestResultsfile, vTestResultsheet,irow,vtcname,vtcdescription,status,UpdatedDateTimeStamp,TestData):
    XLLib.Create_Workbook(vTestResultsfile, vTestResultsheet)
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, irow, 1, vtcname)
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, irow, 2, vtcdescription)
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, irow, 3, status)
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, irow, 4, UpdatedDateTimeStamp)
    XLLib.set_XL_cell_value(vTestResultsfile, vTestResultsheet, irow, 5, TestData)

def get_test_case_row_number(file,sheetname,TCName):
    irow = 0
    i = 1
    imax = XLLib.get_XL_row_count(file, sheetname)

    for x in range(i, imax):
        if XLLib.get_XL_cell_value(file,sheetname,x,1) == TCName :
            irow = x
            break

    return irow

def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_element_exists_by_xpath(driver,expath,timeout):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, expath))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for page to load"
        return False
    return True

def check_element_exists_by_xpath(driver,eid,timeout):
    try:
        element_present = EC.presence_of_element_located((By.ID, eid))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for page to load"
        return False
    return True

def scrollDown(driver, value):
    driver.execute_script("window.scrollBy(0,"+str(value)+")")

# Scroll down the page
def scrollDownAllTheWay(driver):
    old_page = driver.page_source
    while True:
        logging.debug("Scrolling loop")
        for i in range(2):
            scrollDown(driver, 500)
            time.sleep(2)
        new_page = driver.page_source
        if new_page != old_page:
            old_page = new_page
        else:
            break
    return True

def wait_for_page_element_to_be_visible_xpath(driver,expath,timeout) :
    element_visible = EC.visibilityOfElementLocated((By.XPATH , expath))
    WebDriverWait(driver, timeout).until(element_visible);


def wait_for_page_element_to_be_visible_css(driver,expath,timeout) :
    element_visible = EC.visibilityOfElementLocated(expath)
    WebDriverWait(driver, timeout).until(element_visible);


def check_element_exists_by_element(driver,eid,timeout):
    try:
        element_present = EC.presence_of_element_located(eid)
        WebDriverWait(driver, timeout).until(element_present)
        print "element found"
    except TimeoutException:
        print "Timed out waiting for page to load"
        return False
    return True