from Poc1.Lib import Utillib
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


import time
import datetime

utillib = Utillib.utillib()
brow = "gc"
url  = "http://stage-o2/"

driver = utillib.Get_Driver_Handle(utillib,brow)
driver.get(url)
print("hello world!")
Link = driver.find_element_by_link_text('Content Management')
Link.click()
time.sleep(5)
Link = driver.find_element_by_link_text('Docs')
Link.click()
Link = driver.find_element_by_link_text('White Paper')
Link.click()
time.sleep(10)
driver.find_element_by_id('SearchKeyword').send_keys(Keys.HOME)
driver.find_element_by_id('SearchKeyword').send_keys('menaka_murugeshan')
time.sleep(10)
driver.find_element_by_xpath('//input[@type="button"][@value="New White Paper"]').click()
time.sleep(10)
s1 = Select(driver.find_element_by_id('LanguageId'))
time.sleep(20)
s1.select_by_visible_text('English')
driver.find_element_by_id('DisplayName').send_keys('Title')
driver.find_element_by_id('Name').send_keys('Title')
driver.find_element_by_id('IsHidden').click()
driver.find_element_by_id('LiveDateUtc').send_keys(str(datetime.date.today()))
driver.find_element_by_id('ExpireDateUtc').send_keys(str('12/13/2019 12:00 AM'))
#driver.find_element_by_id('LiveDateUtc').send_keys(time.strftime(currentdate, '%m-%d-%Y'))

datetime.date.today()

'''
start = url.index("_enu")
end = start + 4
print(start)
print(end)
print(url[0:end])
time.sleep(30)
lists = driver.find_elements_by_id('s_swepi_1')
print(len(lists))
driver.find_element_by_id('s_swepi_1').click()
time.sleep(10)
driver.find_element_by_id('s_swepi_1').send_keys(Keys.HOME)
driver.find_element_by_id('s_swepi_1').send_keys('menaka_murugeshan')
driver.find_element_by_id('s_swepi_2').click()
time.sleep(10)
driver.find_element_by_id('s_swepi_2').send_keys("menaka_murugeshan")

driver.execute_script("document.getElementById('s_swepi_1').value='12345'")

lists1 = driver.find_elements_by_xpath("//img[(@src,'About'])]")
print(len(lists1))
'''