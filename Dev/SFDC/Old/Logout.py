from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from robot.libraries.BuiltIn import BuiltIn
import XLLib





def Logout_of_SFDC(driver) :
    driver.find_element_by_id('userNavLabel').click()
    time.sleep(10)
    driver.find_element_by_link_text('Logout').click()