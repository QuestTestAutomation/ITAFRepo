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
from guerrillamail import *
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

    def __init__(self, driver, globaldict, rowdict):
        super(whitepapperleadregistrationpage,self).__init__(driver, globaldict)
        self.rowdict = rowdict
        pass


    def verify_page(self):

        self.wait_until_element_is_displayed(*whitepaper_logo)

    def fill_Lead_form_WhitePaper(self):
        status_id = '5'
        utillib = Utillib.utillib(self.globaldict)
        curdttimestamp = utillib.get_current_date_time()
        print(utillib.generate_phonenum())
        rowdict = self.rowdict
        """
        if rowdict['FirstName'] is not None:
            self.fill_out_field(rowdict['FirstName'], *whitepaper_firstname_tbox)
        else :
            self.fill_out_field(curdttimestamp, *whitepaper_firstname_tbox)
        """

        self.fill_out_field(curdttimestamp, *whitepaper_firstname_tbox)
        self.fill_out_field(curdttimestamp, *whitepaper_lastname_tbox)

        session = GuerrillaMailSession()
        session.set_email_address(curdttimestamp)
        #print(session.get_session_state()['email_address'])
        #print(session.get_email_list()[0].guid)
        email = session.get_session_state()['email_address']
        #print(email)
        self.fill_out_field(email, *whitepaper_email_tbox)
        company = 'www.' + curdttimestamp + '.com'
        self.fill_out_field(company, *whitepaper_company_tbox)
        self.select_dropdown_value('Developer',*whitepaper_jobtitle_sel)
        self.select_dropdown_value('UNITED STATES', *whitepaper_Country_sel)
        self.select_dropdown_value('CALIFORNIA', *whitepaper_state_sel)
       # self.select_dropdown_value('1-1,000', *whitepaper_companysize_sel)
        selelement = Select(self.driver.find_element(*whitepaper_companysize_sel))
        selelement.select_by_index(1)

        self.fill_out_field('Aleso Viejo', *whitepaper_city_tbox)
        self.fill_out_field('92656', *whitepaper_postalcode_tbox)
        self.fill_out_field(utillib.generate_phonenum(), *whitepaper_phone_tbox)
        self.click_element(*whitepaper_downloadwhitepaper_btn)
        time.sleep(60)
        emaillist = session.get_email_list()
        for email in emaillist:

            print(email.guid)
            emailattr = session.get_email(email.guid)
            print(emailattr.sender)
            print(emailattr.subject)
            #print(emailattr.body)
            if (rowdict['EnglishName'].upper()) in emailattr.subject.upper():
                print('email came')
                #print(emailattr.body)
                status_id = '1'
        result = {}
        result['actual'] = 'Whitepaper ' + str(rowdict['EnglishName']) + ' is downloaded and an email is sent. Email : ' + str(email) + ' email Subject : ' + str(emailattr.subject) + '.'
        result['status_id'] = status_id
        #self.driver.switch_to.window(self.driver.window_handles[0])
        #self.driver.window_handles[1].close()
        return result

    def hello_world_new(self):

        print('Helloworld')
        result = {}
        result['actual'] = 'Whitepaper '
        result['status_id'] = '1'
        return result


