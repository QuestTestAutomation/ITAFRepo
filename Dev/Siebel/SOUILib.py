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
from ITAFRepo.Dev.Utilities import ExceptionLib
import time


class Souilib(Seleniumutil.Seleniumutil):

    def __init__(self,driver,globaldict,url):
        super(Souilib,self).__init__(driver,globaldict)
        self.driver = driver
        self.webserverurl = self.get_webserver_url(url)
       # self.exceptionlib = ExceptionLib.ExceptionLib()

    def get_webserver_url(self,url):
        start = url.index("_enu")
        end = start + 4
        webserverurl = url[0:end]
        return webserverurl

    def Login_lite(self,url,user,password):

        try:
            self.launch_url(url)
            time.sleep(5)
            self.fill_out_field('SUPPORT_ADMIN', *(By.ID, 's_swepi_1'))
            self.fill_out_field('SUPPORT_ADMIN', *(By.ID, 's_swepi_2'))
            self.click_element(*(By.XPATH, '//*[@id="s_swepi_22"]'))
            time.sleep(30)
            self.click_sitemap()
        except:
            errmsg = 'Error while executing the function Login_lite'
            print(errmsg)


    def click_sitemap(self):
        try:

            elements = self.driver.find_elements_by_tag_name('img')
            for element in elements:

                if element.get_attribute('src').upper() == (self.webserverurl + '/images/icon_sitemap_1.gif').upper():
                    element.click()
                    WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sitemapSectionTitle")))
                    break
        except:
            errmsg = 'Error while executing the function click_sitemap'
            print(errmsg)

    def click_sitemap_screen_link(self,ScreenLink):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sitemapSectionTitle")))
            elements = self.driver.find_elements_by_css_selector('table.sitemapIndexSection a')
            for element in elements:
                #print(element.text)
                if (element.text).upper() == (ScreenLink).upper():
                    #print(element.text)
                    element.click()
                    time.sleep(5)
                    break
        except:
            errmsg = 'Error while executing the function click_sitemap'
            print(errmsg)

    def click_sitemap_screen_view_linkid(self,viewlinktext,viewindex):
        try:
            index = 0
            viewindex = int(viewindex)
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sitemapSectionTitle")))
            elements = self.driver.find_elements_by_css_selector('ul.sitemapMain span.viewName a')
            for element in elements:
                #print(element.text)
                if (element.text).upper() == (viewlinktext).upper():
                    index = index + 1
                    if index == int(viewindex):
                        #print(element.text)
                        element.click()
                        time.sleep(5)
                        break
        except:
            errmsg = 'Error while executing the function click_sitemap'
            print(errmsg)

    def click_view_link(self,viewlinktext,viewlevel,viewindex):
            try:
                viewexists = 0
                index = 0
                viewindex = int(viewindex)
               # WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#_sweclient div#_swescrnbar div#s_sctrl div#s_sctrl_tabScreen a)))
                if (viewlevel).upper() == ('L1').upper() :
                    elements = self.driver.find_elements_by_css_selector('div#_sweclient div#_swescrnbar div#s_sctrl div#s_sctrl_tabScreen a')
                elif (viewlevel).upper() == ('L2').upper() :
                    elements = self.driver.find_elements_by_css_selector('div#_sweclient div#s_sctrl_tabView a')
                elif (viewlevel).upper() == ('L3').upper():
                    elements = self.driver.find_elements_by_css_selector('div#s_vctrl_div div#s_vctrl_div_tabScreen a')
                elif (viewlevel).upper() == ('L4').upper():
                    elements = self.driver.find_elements_by_css_selector('div#s_vctrl_div div#s_vctrl_div_tabView a')

                #print('len(elements)')
                #print(len(elements))

                if len(elements) > 0 :

                    for element in elements:
                        #print(element.text)
                        #print((element.text).upper() == (viewlinktext).upper())
                        if (element.text).upper() == (viewlinktext).upper():
                            index = index + 1
                           #print('index == int(viewindex)')
                            #print(index == int(viewindex))
                            if index == int(viewindex):
                               # print(element.text)
                                element.click()
                                time.sleep(10)
                                viewexists = 1
                                break

                    if int(viewexists) == 0:
                        if (viewlevel).upper() == ('L3').upper():
                            selloc = (By.CSS_SELECTOR, '#j_s_vctrl_div_tabScreen')
                            self.select_dropdown_value(viewlinktext,*selloc)
                        elif (viewlevel).upper() == ('L1').upper():
                            selloc = (By.CSS_SELECTOR, '#j_s_sctrl_tabScreen')
                            self.select_dropdown_value(viewlinktext,*selloc)
            except:
                errmsg = 'Error while executing the function click_view_link'
                print(errmsg)

    def get_list_applet_column_id(self, columnlabel, appletindex, columnindex):
        try:
            print('executing get_list_applet_column_id ')
            columnid = None
            index = 0
            colindex = 0
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-jqgrid-htable")))
            elements = self.driver.find_elements_by_css_selector('.ui-jqgrid-htable')
            #print('tables : ' + str(len(elements)))
            for element in elements:
                index = index + 1
                if index == int(appletindex):
                    columns = element.find_elements_by_xpath('.//DIV')
                    for column in columns:
                       # print(column.text)
                        if (column.text).upper() == (columnlabel).upper():
                            colindex = colindex + 1
                            if (int(colindex)) == int(columnindex):
                                print(column.get_attribute('id'))
                                columnid = column.get_attribute('id')
                                columnid = columnid[4:]
                                break
            return columnid

        except:
            errmsg = 'Error while executing the function get_list_applet_column_id'
            print(errmsg)

    def get_list_applet_table_id(self, appletindex):
        try:
            print('executing get_list_applet_column_id ')
            columnid = None
            index = 0
            colindex = 0
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-jqgrid-btable")))
            elements = self.driver.find_elements_by_css_selector('.ui-jqgrid-btable')
            #print('tables : ' + str(len(elements)))
            for element in elements:
                index = index + 1
                if index == int(appletindex):
                   tableid = element.get_attribute('id')
                   break
            return tableid

        except:
            errmsg = 'Error while executing the function get_list_applet_table_id'
            print(errmsg)

    def set_list_applet_column_value(self, columnlabel, appletindex, columnindex,rownumber,columnvalue):
        try:
            columnid = rownumber + self.get_list_applet_column_id(columnlabel, appletindex, columnindex)
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.ID, columnid)))
            self.driver.find_element_by_id(columnid).send_keys(columnvalue)
            time.sleep(3)

        except:
            errmsg = 'Error while executing the function get_list_applet_table_id'
            print(errmsg)

    def get_list_applet_column_value(self, columnlabel, appletindex, columnindex, rownumber):
        try:
            columnid = rownumber + self.get_list_applet_column_id(columnlabel, appletindex, columnindex)
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.ID, columnid)))
            columnvalue = self.driver.find_element_by_id(columnid).text
            time.sleep(3)
            return columnvalue
        except:
            errmsg = 'Error while executing the function get_list_applet_table_id'
            print(errmsg)

    def press_keyboard_tab(self):
        self.send_keyboard_keys(Keys.TAB)
        time.sleep(3)

    def send_element_keyboard_tab(self,element):
        element.send_keys(Keys.TAB)
        time.sleep(3)

    def drilldown_on_list_applet_column(self, columnlabel, appletindex, columnindex,rownumber):
        try:
            columnid = rownumber + self.get_list_applet_column_id(columnlabel, appletindex, columnindex)
            self.driver.find_element_by_id(columnid).click()

        except:
            errmsg = 'Error while executing the function drilldown_on_list_applet_column'
            print(errmsg)

    def click_on_threadbar_link(self, threadbarindex):
        try:
            index = 0
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#siebui-threadbar")))
            elements = self.driver.find_elements_by_css_selector('#siebui-threadbar a')
            print('threadbar links')
            print(len(elements))
            for element in elements:
                index = index + 1
                if index == int(threadbarindex):
                    element.click()
        except:
            errmsg = 'Error while executing the function click_on_threadbar_link'
            print(errmsg)

    def click_button(self, buttontitle,buttonindex):
        try:
            index = 0
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#siebui-threadbar")))
            elements = self.driver.find_elements_by_tag_name('button')
            print('buttons')
            print(len(elements))
            for element in elements:

                if (element.text).upper() == (buttontitle).upper():
                    index = index + 1
                    if index == int(buttonindex):
                        element.click()
        except:
            errmsg = 'Error while executing the function click_button'
            print(errmsg)

    def get_form_field_name(self,fieldlabel):
        try:
            formfieldid = None
            elements = self.driver.find_elements_by_css_selector('div.mceGridField')
            for element in elements:
                inputelements = element.find_elements_by_xpath('.//input')
                for inputelement in inputelements:
                    #print(inputelement.get_attribute('aria-label'))
                    #print(inputelement.get_attribute('aria-label').upper() == (fieldlabel).upper())
                    if inputelement.get_attribute('aria-label').upper() == (fieldlabel).upper():
                        print(inputelement.get_attribute('name'))
                        formfieldid = inputelement.get_attribute('name')
                        break
            return formfieldid
        except:
            errmsg = 'Error while executing the function get_form_field_id'
            print(errmsg)

    def get_form_textarea_name(self,fieldlabel):
        try:
            formfieldid = None
            elements = self.driver.find_elements_by_css_selector('div.mceGridField')
            for element in elements:
                inputelements = element.find_elements_by_xpath('.//textarea')
                for inputelement in inputelements:
                    #print(inputelement.get_attribute('aria-label'))
                    #print(inputelement.get_attribute('aria-label').upper() == (fieldlabel).upper())
                    if inputelement.get_attribute('aria-label').upper() == (fieldlabel).upper():
                        print(inputelement.get_attribute('name'))
                        formfieldid = inputelement.get_attribute('name')
                        break
            return formfieldid
        except:
            errmsg = 'Error while executing the function get_form_field_id'
            print(errmsg)

    def set_form_applet_input_value(self,formfieldlabel,forminputvalue):
        formfieldname = '//input[@name="' + self.get_form_field_name(formfieldlabel) + '"]'
        print('**' + formfieldname)
        self.driver.find_element_by_xpath(formfieldname).click()
        self.driver.find_element_by_xpath(formfieldname).send_keys(forminputvalue)
        self.driver.find_element_by_xpath(formfieldname).send_keys(Keys.TAB)

    def set_form_applet_textarea_value(self,formfieldlabel,forminputvalue):
        formfieldname = '//textarea[@name="' + self.get_form_textarea_name(formfieldlabel) + '"]'
        print('**' + formfieldname)
        self.driver.find_element_by_xpath(formfieldname).click()
        self.driver.find_element_by_xpath(formfieldname).send_keys(forminputvalue)
        self.driver.find_element_by_xpath(formfieldname).send_keys(Keys.TAB)
