from Poc1.Lib.PageObjectLibrary.BasePage import BasePage
from Poc1.Lib.PageObjectLibrary.BasePage import Incorrectpageexception
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Poc1.Lib.Locators import *

import time
import datetime


class contentmanagementobj1(BasePage):
    """
    Base class that all page models can inherit from
    """


    def __init__(self, driver, url, wait_time):
        super(contentmanagementobj1,self).__init__(driver, url, wait_time)

    """
    def verify_page(self):
        pass



        try:
            self.wait_until_element_is_displayed(*content_management_lnk)
        except:
            raise Exception("Incorrectpageexception")
        :return: 
        """

    def Lauch_url(self):
        self.navigate()

    def add_whitepaper(self):
        #content_management_lnk = (By.LINK_TEXT, 'Content Management')

        self.navigate()
        print(*content_management_lnk)
        #self.click_element(*startButton_loc)
        self.click_element(*cmgmt_Document_lnk)
        self.click_element(*cmgmt_WhitePaper_lnk)
        # self.fill_out_field(rowdict['searchkeyword'],*cmgmt_searchkeyword_tbox)
        self.fill_out_field('bujjulu', *cmgmt_searchkeyword_tbox)
        self.click_element(*cmgmt_NewWhitePaper_btn)
        # time.sleep(10)
        # self.click_element(*Language_loc)
        # self.select_dropdown_value(rowdict['Language'],*cmgmt_Language_sel)




