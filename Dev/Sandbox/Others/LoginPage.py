from robot.libraries.BuiltIn import BuiltIn

import XLLib

driver = BuiltIn().get_variable_value("${webdriver}")
def initialize_webelements(driver):
    global we_uname
    global we_password
    global we_Login_Loginlink
    we_uname = driver.find_element_by_id('username')
    we_password = driver.find_element_by_id('password')
    we_Login_Loginlink = driver.find_element_by_id('Login')

def Load_Logindata(file,sheetname,rownum) :
    vURL = XLLib.using_column_header(file, sheetname, rownum, "Url_SFDC")
    vUserName = XLLib.using_column_header(file, sheetname, rownum, "UserName")
    vPassword = XLLib.using_column_header(file, sheetname, rownum, "Password")

def Login_into_SFDC(driver,uname,passw):
    initialize_webelements(driver)
    we_uname.click()
    we_uname.send_keys(uname)
    we_password.click()
    we_password.send_keys(passw)
    we_Login_Loginlink.click()