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


class contentmanagement(BasePage):
    """
    Base class that all page models can inherit from
    """
    def __init__(self, driver,url,wait_time):
        super(contentmanagement,self).__init__(driver,url,wait_time)


    def verify_page(self):
        try:
            self.wait_until_page_is_displayed(*cmgmt_contentmanagement_lnk)
        except:
            raise Exception("Incorrectpageexception")



    def Lauch_url(self):
        self.navigate()

    def add_whitepaper(self):
        self.navigate()
        print(*cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_Document_lnk)
        self.click_element(*cmgmt_WhitePaper_lnk)
        #self.fill_out_field(rowdict['searchkeyword'],*cmgmt_searchkeyword_tbox)
        self.fill_out_field('bujjulu', *cmgmt_searchkeyword_tbox)
        self.click_element(*cmgmt_NewWhitePaper_btn)
        #time.sleep(10)
        #self.click_element(*Language_loc)
        #self.select_dropdown_value(rowdict['Language'],*cmgmt_Language_sel)




