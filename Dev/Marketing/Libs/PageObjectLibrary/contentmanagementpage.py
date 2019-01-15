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

    def __init__(self, driver, url, wait_time):
        super(contentmanagement,self).__init__(driver, url, wait_time)

    def add_whitepaper(self,rowdict):
        """


        self.navigate()
        self.wait_until_page_is_displayed(self, *cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_Document_lnk)
        self.click_element(*cmgmt_WhitePaper_lnk)

        """
        self.Navigate_to_whitepaper()
        self.click_element(*cmgmt_NewWhitePaper_btn)
        time.sleep(5)
        self.click_element(*cmgmt_Language_sel)

        self.select_dropdown_value(rowdict['Language'],*cmgmt_Language_sel)
        self.fill_out_field(rowdict['LocalizedTitle'],*cmgmt_Localizedtitle_tbox)
        self.fill_out_field(rowdict['EnglishName'], *cmgmt_Englishname_tbox)
        self.fill_out_field(rowdict['StartDate'], *cmgmt_Statedate_dt)
        self.fill_out_field(rowdict['EndDate'], *cmgmt_Enddate_dt)
        self.fill_out_field(rowdict['Owner'], *cmgmt_Owner_tbox)
        self.click_element(*cmgmt_Search_btn)
        time.sleep(5)

        self.fill_out_field(rowdict['Abstract'], *cmgmt_Abstract_tbox)
        self.add_whitepaper_description(rowdict)
        self.select_dropdown_value(rowdict['BuyersJourney'], *cmgmt_BuyersJourney_sel)
        self.select_multiple_options(rowdict['RelatedProducts'], ';', *cmgmt_RelatedProducts_sel)
        time.sleep(3)
        self.click_element(*cmgmt_addrelatedproduct_btn)
        time.sleep(3)



        if ((rowdict['Registration']).upper().strip()) == 'LINK DIRECTLY TO A DOCUMENT':
            self.click_element(*cmgmt_registration_link_url_radio)
            time.sleep(5)
            """
            self.fill_out_field(rowdict['Abstract'], *cmgmt_Abstract_tbox)
            self.click_element(*cmgmt_Search_btn)
            time.sleep(3)
            
            currwindowhandle = self.driver.current_window_handle
            self.switch_to_iframe(*cmgmt_Description_iframe)
            time.sleep(3)
            self.click_element(*cmgmt_Description_tbox)
            time.sleep(3)

            self.fill_out_field_textarea(rowdict['Description'], *cmgmt_Description_tbox)
            self.switch_to_window(currwindowhandle)
            #self.switch_back_to_mainwindow()
            time.sleep(3)
            self.click_element(*cmgmt_Abstract_tbox)
            """
            self.fill_out_field(rowdict['Author'], *cmgmt_Author_tbox) #Fill Date of Document
            self.fill_out_field(rowdict['DateofDocument'], *cmgmt_DocumentDate_tbox)


            self.select_multiple_options(rowdict['RelatedProducts'],';',*cmgmt_RelatedProducts_sel)
            self.click_element(*cmgmt_addrelatedproduct_btn)
            time.sleep(5)


        elif ((rowdict['Registration']).upper().strip()) == 'UPLOAD A DOCUMENT':
            self.click_element(*cmgmt_registration_upload_document_radio)
            time.sleep(5)
            """
            self.fill_out_field(rowdict['Abstract'], *cmgmt_Abstract_tbox)
            currwindowhandle = self.driver.current_window_handle
            self.switch_to_iframe(*cmgmt_Description_iframe)
            time.sleep(3)
            self.click_element(*cmgmt_Description_tbox)
            time.sleep(3)

            self.fill_out_field_textarea(rowdict['Description'], *cmgmt_Description_tbox)
            self.switch_to_window(currwindowhandle)


            # self.switch_back_to_mainwindow()
            time.sleep(3)
            self.click_element(*cmgmt_Abstract_tbox)
            """
            self.fill_out_field(rowdict['Author'], *cmgmt_Author_tbox)  # Fill Date of Document
            self.fill_out_field(rowdict['DateofDocument'], *cmgmt_DocumentDate_tbox)
            self.select_dropdown_value(rowdict['BuyersJourney'], *cmgmt_BuyersJourney_sel)
            self.select_multiple_options(rowdict['RelatedProducts'], ';', *cmgmt_RelatedProducts_sel)
            self.click_element(*cmgmt_addrelatedproduct_btn)
            time.sleep(5)
            self.click_element(*cmgmt_addrelatedproduct_btn)
            time.sleep(3)
            self.click_element(*cmgmt_FileUpload_btn)

            self.upload_file(rowdict)
            time.sleep(10)


        elif ((rowdict['Registration']).upper().strip()) == (('FULL REGISTRATION - LEAD ONLY').upper().strip()):
            self.click_element(*cmgmt_registration_fullregistrationlead_radio)
            time.sleep(5)
            self.fill_out_field(rowdict['PageTitle'], *cmgmt_PageTitle_tbox)
            self.fill_out_field(rowdict['MetaKeyword'], *cmgmt_PageMetaKeyword_tbox)
            self.fill_out_field(rowdict['MetaDescription'], *cmgmt_PageMetaDescription_tbox)
#            self.fill_out_field(rowdict['Description'], *cmgmt_Description_tbox)
            self.select_dropdown_value(rowdict['MarketIntrest'], *cmgmt_Marketingintrest_sel)
            self.select_dropdown_value(rowdict['LeadForm'], *cmgmt_Leadform_sel)
            self.fill_out_field(rowdict['AssetCode'], *cmgmt_Assetcode_tbox)
            self.fill_out_field(rowdict['DateofDocument'], *cmgmt_DocumentDate_tbox)

            self.add_file_document_link(rowdict)
            self.add_internalemail(rowdict)

        #save and preview the white paper
        self.click_element(*cmgmt_saveandarchive_btn)


    def add_file_document_link(self,rowdict):
        self.click_element(*cmgmt_Addfile_btn)
        time.sleep(10)
        print("filename")
        print(rowdict['FileName'])
        self.fill_out_field(rowdict['FileName'], *cmgmt_Filename_tbox)
        currwindowhandle = self.driver.current_window_handle
        self.switch_to_iframe(*cmgmt_FileDescription_iframe)
        time.sleep(3)
        self.click_element(*cmgmt_Filedescription_tbox)
        time.sleep(3)

        self.fill_out_field_textarea(rowdict['FileDescription'], *cmgmt_Filedescription_tbox )
        self.switch_to_window(currwindowhandle)
        # self.switch_back_to_mainwindow()
        #self.click_element(*cmgmt_Addfile_btn)
        time.sleep(3)
        self.select_dropdown_value(rowdict['FileSelection'], *cmgmt_Fileselection_sel)
        time.sleep(3)
        if ((rowdict['FileSelection']).upper().strip()) == (('Upload File').upper().strip()):
            self.click_element(*cmgmt_Linkfileupload_btn)
            time.sleep(10)
            self.upload_file(rowdict)
            time.sleep(3)
        elif ((rowdict['FileSelection']).upper().strip()) == (('URL of Document').upper().strip()):
            self.fill_out_field(rowdict['Link'], *cmgmt_FileVersion_tbox)

        self.fill_out_field(rowdict['FileVersion'], *cmgmt_FileVersion_tbox)
        self.fill_out_field(rowdict['FileLastupdated'], *cmgmt_FileLastUpdated_tbox)
        time.sleep(4)
        self.click_element(*cmgmt_Addfile_save_btn)


    def upload_file(self,rowdict):
        time.sleep(10)

        print(rowdict['Files'].replace('\\', '/'))
        self.add_file((rowdict['Files'].replace('\\', '/')), *cmgmt_SelectFiles_tbox)
        time.sleep(5)
        self.click_element(*cmgmt_closefiles_btn)

    def add_internalemail(self,rowdict):
        self.click_element(*cmgmt_addemail_lnk )
        self.fill_out_field(rowdict['EmailSubject'], *cmgmt_Emailsubject_tbox )
        self.fill_out_field(rowdict['Emailto'], *cmgmt_EmailTo_tbox)
        self.fill_out_field(rowdict['EmailBody'], *cmgmt_EmailBody_tbox)
        self.click_element(*cmgmt_EmailSave_btn)

    def add_whitepaper_description(self,rowdict):
        currwindowhandle = self.driver.current_window_handle
        self.switch_to_iframe(*cmgmt_Description_iframe)
        time.sleep(3)
        self.click_element(*cmgmt_Description_tbox)
        time.sleep(3)

        self.fill_out_field_textarea(rowdict['Description'], *cmgmt_Description_tbox)
        self.switch_to_window(currwindowhandle)

    def Navigate_to_whitepaper(self):
        self.navigate()
        self.wait_until_page_is_displayed(self, *cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_contentmanagement_lnk)
        self.click_element(*cmgmt_Document_lnk)
        self.click_element(*cmgmt_WhitePaper_lnk)

    def Search_for_whitepaper(self,whitepaper):

        self.Navigate_to_whitepaper()
        self.click_element(*cmgmt_Searchkeyword_tbox)
        self.fill_out_field(whitepaper,*cmgmt_Searchkeyword_tbox)
        self.click_element(*cmgmt_Searchkeyword_btn)
        time.sleep(10)


    def get_whitepaper_details(self,whitepaper) :
        print('mantu')
        headerrowdict = {}
        whitepaperdict = {}
        tableheaders = self.driver.find_elements_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/thead/tr/th')

        for i in range(1, len(tableheaders)):
            headerxpath = '/html/body/div[1]/section/div[3]/div[2]/table/thead/tr/th[' + str(i) + ']'
            #print(headerxpath)
            #print(self.driver.find_element_by_xpath(headerxpath).get_attribute('data-title'))
            headerrowdict[self.driver.find_element_by_xpath(headerxpath).get_attribute('data-title')] = str(i)


        tablerows = self.driver.find_elements_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr')
        print('tablerows')
        print(len(tablerows))
        for row in range(1, (len(tablerows)+1)):
            Title = 'English Name'
            colsxpath = '/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict[
                Title] + ']'
            print('row : ' + str(row))
            # get English Name
            print('Column Value : ' + self.driver.find_element_by_xpath(colsxpath).get_attribute('innerHTML'))
            print('Column Value : ' + (whitepaper).upper().strip())
            print((self.driver.find_element_by_xpath(colsxpath).get_attribute('innerHTML').upper().strip()) == ((whitepaper).upper().strip()))
            print(headerrowdict['Live'])

            #get the White paper is live details
            if (self.driver.find_element_by_xpath(colsxpath).get_attribute('innerHTML').upper().strip()) == ((whitepaper).upper().strip()):
                whitepaperdict['English Name'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['English Name'] + ']').get_attribute('innerHTML')
                whitepaperdict['Localized Title'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Localized Title'] + ']').get_attribute('innerHTML')
                whitepaperdict['Language'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Language'] + ']').get_attribute('innerHTML')
                whitepaperdict['Live'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']').get_attribute('innerHTML')
                print(headerrowdict['Live'])
                print('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/img')
                imagetext = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/img').get_attribute('src')
                print(imagetext)
                # print(driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']').getattributes())
                if self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']').is_displayed():
                    imagetext = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/img').get_attribute('src')
                    print(imagetext)
                    if 'Disabled.gif' in (self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/img').get_attribute('src')):
                        print("Not yet Live")
                        whitepaperdict['Live'] = 'Draft'
                        whitepaperdict['LiveLink'] = None
                    elif 'Checkmark.gif' in (self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/img').get_attribute('src')):
                        print('live')
                        whitepaperdict['Live'] = 'Live'
                        whitepaperdict['LiveLink'] = self.driver.find_element_by_xpath('html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/a')
                        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']/a').click()

                #get the Last Updated


                if self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Live'] + ']').is_displayed():
                    imagetext = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Preview'] + ']/img').get_attribute('src')
                    print(imagetext)
                    if 'Disabled.gif' in (self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Preview'] + ']/img').get_attribute('src')):
                        print("Not yet Live")
                        whitepaperdict['Live'] = 'Draft'
                        whitepaperdict['LiveLink'] = None
                    elif 'Checkmark.gif' in (self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Preview'] + ']/img').get_attribute('src')):
                        print('Preview')
                        whitepaperdict['Preview'] = 'Live'
                        whitepaperdict['PreviewLink'] = self.driver.find_element_by_xpath('html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Preview'] + ']/a')
                        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Preview'] + ']/a').click()

                #get Promted Assets

                    print('Last Updated')
                    print(self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Last Updated'] + ']').is_displayed())
                    print(self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Last Updated'] + ']/div').text)

                    if self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Last Updated'] + ']').is_displayed():

                        whitepaperdict['Last Updated'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Last Updated'] + ']/div').text
                        # get Promted Assets

                    if len(self.driver.find_elements_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Promoted Assets'] + ']/*')) == int(0) :
                        whitepaperdict['Promoted Assets'] = None
                    elif self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Promoted Assets'] + ']').is_displayed():
                        whitepaperdict['Promoted Assets'] = self.driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/table/tbody/tr[' + str(row) + ']/td[' + headerrowdict['Promoted Assets'] + ']/span/a')

                break

        print(whitepaperdict)
        return whitepaperdict
















