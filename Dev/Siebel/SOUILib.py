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
from ITAFRepo.Dev.Utilities import Seleniumutil
import time


class Souilib(Seleniumutil.Seleniumutil):

    def __init__(self,driver,globaldict,url):
        super(Souilib,self).__init__(driver,globaldict)
        self.webserverurl = self.get_webserver_url(url)

    def get_webserver_url(self,url):
        start = url.index("_enu")
        end = start + 4
        webserverurl = url[0:end]
        return webserverurl

    def Login_lite(self,url,user,password):
        self.launch_url(url)
        time.sleep(5)
        #webserverurl = self.get_webserver_url(url)
        self.driver.find_element_by_id('s_swepi_1').send_keys(Keys.HOME)
        self.driver.find_element_by_id('s_swepi_1').send_keys('SUPPORT_ADMIN')
        self.driver.find_element_by_id('s_swepi_2').click()
        time.sleep(5)
        self.driver.find_element_by_id('s_swepi_2').send_keys('SUPPORT_ADMIN')

        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="s_swepi_22"]').click()
