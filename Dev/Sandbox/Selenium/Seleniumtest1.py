from ITAFRepo.Dev.Utilities import Utillib
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

utillib = Utillib.utillib()
brow = "gc"
url  = "http://siebeluat/sales_enu/start.swe?SWECmd=AutoOn"
url = 'http://siebeluat.prod.quest.corp/dbsupport_enu/start.swe?SWECmd=AutoOn'

driver = utillib.Get_Driver_Handle(utillib,brow)
driver.get(url)
print("hello world!")

start = url.index("_enu")
end = start + 4
print('****' + str(start))
print('****' + str(end))
print('99999' + url[0:end])
time.sleep(30)
lists = driver.find_elements_by_id('s_swepi_1')
print(len(lists))
driver.find_element_by_id('s_swepi_1').click()
time.sleep(5)
driver.find_element_by_id('s_swepi_1').send_keys(Keys.HOME)
driver.find_element_by_id('s_swepi_1').send_keys('SUPPORT_ADMIN')
driver.find_element_by_id('s_swepi_2').click()
time.sleep(5)
driver.find_element_by_id('s_swepi_2').send_keys('SUPPORT_ADMIN')

time.sleep(5)
#driver.find_element_by_xpath('//*[@id="s_swepi_22"]').click()
driver.find_element_by_link_text('Login').click()

#driver.execute_script("document.getElementById('s_swepi_1').value='12345'")

#lists1 = driver.find_elements_by_xpath("//img[(@src,'About'])]")
#print(len(lists1))

