from ITAFRepo.Dev.Utilities import Utillib
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
from ITAFRepo.Dev.Utilities import ExceptionLib
from ITAFRepo.Dev.Siebel import Souilib
import time

class Siebelservicelib(Souilib.Souilib):

    def __init__(self, driver, globaldict, url,datadict = {} ,rundict = {},resultdict = {}):
        super(Siebelservicelib, self).__init__(driver, globaldict)
        self.driver = driver
        self.webserverurl = self.get_webserver_url(url)
        self.exceptionlib = ExceptionLib.ExceptionLib()
        self.datadict = datadict
        self.rundict = rundict


    def load_sr_test_data(self,datafile):