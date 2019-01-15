from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary.BasePage import BasePage
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary.BasePage import Incorrectpageexception
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ITAFRepo.Dev.Marketing.Libs.Locators import *
from ITAFRepo.Dev.Guerrillamail import Guerillamaillib
from ITAFRepo.Dev.Utilities import Seleniumutil
from ITAFRepo.Dev.Utilities import Utillib
import time
import datetime

"""
****************************************************************************************************
**The class has functions related to the Download whitepaper Page.
*****************************************************************************************************
"""
class whitepapperleadregistrationpage(BasePage):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, driver, globaldict, datadict,datadictrownumber):
        super(whitepapperleadregistrationpage,self).__init__(driver, globaldict)
        self.datadict = datadict
        self.datadictrownumber = datadictrownumber
        #self.globaldict = globaldict

    def verify_page(self):

        self.wait_until_element_is_displayed(*whitepaper_logo)

    def fill_Lead_form_WhitePaper(self):
        utillib = Utillib.utillib(self.globaldict)
        curdttimestamp = utillib.get_current_date_time()
        rowdict = self.rowdict
        self.fill_out_field(curdttimestamp, *whitepaper_firstname_tbox)
        self.fill_out_field(curdttimestamp, *whitepaper_lastname_tbox)
        gureillamaillib = Guerillamaillib.guerillamaillib()
        email = gureillamaillib.set_temporary_email(curdttimestamp)
        self.fill_out_field(email, *whitepaper_email_tbox)
        company = 'www.' + curdttimestamp + '.com'
        self.fill_out_field(company, *whitepaper_company_tbox)
        self.select_dropdown_value('Developer',*whitepaper_jobtitle_sel)
        self.click_element(*whitepaper_downloadwhitepaper_btn)
