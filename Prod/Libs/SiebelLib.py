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
from ITAFRepo.Dev.Siebel.Siebelservicelib import Siebelservicelib
from ITAFRepo.Dev.DateTime import DateTimelib
from ITAFRepo.Dev.Siebel import Souilib
import time

class siebellib(Souilib.Souilib):

    def __init__(self, driver, globaldict, url,datadict, rundict,rowdict):
        super(siebellib, self).__init__(driver, globaldict,url)
        self.driver = driver
        self.webserverurl = self.get_webserver_url(url)
        #self.exceptionlib = ExceptionLib.ExceptionLib()
        self.datadict = datadict
        self.rundict = rundict
        self.rowdict = rowdict


    def query_contact(self):
        self.click_sitemap_screen_view_linkid('Contacts List', '1')
        self.open_ui_sync()
        self.wait_for_button('Query','1')
        self.click_button('Query','1')
        self.open_ui_sync()
        self.set_list_applet_column_value('Email','1','1','1','art.cognizant2@gmail.com.dev')

        self.set_list_applet_column_value('Account', '1', '1', '1', 'QUEST SOFTWARE INC')

        self.wait_for_button('Go', '1')
        time.sleep(3)
        self.click_button('Go', '1')
        time.sleep(3)
        self.open_ui_sync()
        self.wait_for_button('Query', '1')


    def create_sr(self):
        Product = 'Toad for Oracle'
        Summary ='Summary'
        Asset = None
        self.query_contact()
        self.drilldown_on_list_applet_column('Last Name', '1', '1', '1')
        time.sleep(2)
        self.click_view_link('Contact Software SR','L3','1')
        time.sleep(2)
        self.click_button('New',2)
        time.sleep(2)
        self.set_list_applet_column_value('Product', '1', '1', '1', Product)
        self.set_list_applet_column_value('Summary', '1', '1', '1', Summary)
        time.sleep(3)
        if not Asset == None:
            self.set_list_applet_column_value('End User Asset #', '1', '1', '1', Asset)
        self.save_record()
        time.sleep(3)
        self.open_ui_sync()
        time.sleep(3)
        SR = self.get_list_applet_column_value('SR #','1','1','1')
        print(SR)
        self.click_on_list_applet_column('Summary','1','1','1')
        time.sleep(3)
        self.drilldown_on_list_applet_column('SR #','1','1','1')
        time.sleep(3)
        self.wait_for_button('New','1')
        SLAExpriyTimeActual = self.get_form_applet_input_value('SLA Expiry Time')
        Support = self.get_form_applet_input_value('Premier')
        EntitlementRegion = self.get_form_applet_input_value('Entitlement Region')
        Severity = self.get_form_applet_input_value('Severity')
        OpenDate = self.get_form_applet_input_value('Date Opened')
        print('SLAExpriyTimeActual : ' + SLAExpriyTimeActual)
        print('Support   : ' + Support)
        print('EntitlementRegion   : ' + EntitlementRegion)
        print('Severity   : ' + Severity)
        SLAExpriyTimeCalculated = Siebelservicelib.calculate_sla_expiry_time(OpenDate,EntitlementRegion,Severity,Support)
        print('SLAExpriyTimeCalculated : ' + SLAExpriyTimeCalculated)
        SLAExpirytimediff = DateTimelib.datetimelib.subtract_dates(SLAExpriyTimeActual, SLAExpriyTimeCalculated)
        print(SLAExpirytimediff)
        if SLAExpirytimediff < 60:
            print('Entitlement verification is pass.')
        else :
            print('Entitlement verification has failed. The SLA Expiry time in Siebel is ' + SLAExpriyTimeActual + '. The calculated SLA Expiry time is ' + SLAExpriyTimeCalculated + ' .')


    def update_SR_substatus(self,substatus):
        self.select_form_applet_input_value('substatus', substatus)
        self.save_record()
        time.sleep(3)
        self.open_ui_sync()

    def update_sr_status(self,status):
        self.click_view_link('Related SRs','L3','1')
        time.sleep(3)
        self.open_ui_sync()
        self.select_form_applet_input_value('status', status)
        self.save_record()
        time.sleep(3)
        self.open_ui_sync()









        """
        
        recordcount = self.get_record_count()
        print('****')
        print(recordcount)
        print(recordcount == '1')
        if str(recordcount) == '1':
            time.sleep(5)
            self.query_contact()
            self.click_on_list_applet_column('First Name', '1', '1', '1')
            self.drilldown_on_list_applet_column('Last Name', '1', '1', '1')
            time.sleep(3)
            #self.open_ui_sync()
        """



