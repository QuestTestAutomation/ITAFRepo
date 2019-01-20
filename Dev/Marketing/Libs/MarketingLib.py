from selenium import webdriver
from ITAFRepo.Dev.Utilities import Utillib
#from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import contentmanagementpage
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import contentmanagementpage
from ITAFRepo.Dev.Marketing.Libs.PageObjectLibrary import whitepapperleadregistrationpage

class MarketingLib():

    def __init__(self,driver,globaldict):
        self.driver = driver
        self.globaldict = globaldict
        pass

    def Helloworld(self):
        print('Hello World')

    def add_whitepaper(self,datadict):
        contentmanagement_page = contentmanagementpage.contentmanagementpage(self.driver, self.globaldict, datadict)
        result = contentmanagement_page.add_whitepaper()
        stepdict = {}
        stepdict['expected'] = 'The White paper is added successfully.'
        stepdict['actual'] = result['actual']
        stepdict['status_id'] = result['status_id']
        return stepdict

    def search_and_publish_whitepaper(self,datadict):
        contentmanagement_page = contentmanagementpage.contentmanagementpage(self.driver, self.globaldict, datadict)
        result = contentmanagement_page.search_publish_whitepaper()
        #contentmanagement_page.Search_for_whitepaper()
        #whitepaperdict = contentmanagement_page.get_whitepaper_details()
        stepdict = {}
        stepdict['expected'] = 'The White paper is retrived and published succesfully'
        stepdict['actual'] = result['actual']
        stepdict['status_id'] = result['status_id']

        return stepdict

    def download_whitepaper(self, datadict):
        contentmanagement_page = contentmanagementpage.contentmanagementpage(self.driver, self.globaldict, datadict)
        contentmanagement_page.Search_for_whitepaper()
        contentmanagement_page.click_on_whitepaper()
        whitepapperleadregistration_page = whitepapperleadregistrationpage.whitepapperleadregistrationpage(self.driver, self.globaldict, datadict)
        result = whitepapperleadregistration_page.fill_Lead_form_WhitePaper()
        stepdict = {}
        stepdict['expected'] = 'The White paper is downloaded successfully'
        stepdict['actual'] = result['actual']
        stepdict['status_id'] = result['status_id']
        return stepdict

    def hello_world(self, datadict):
        print('executing helloworld')
        whitepage = whitepapperleadregistrationpage.whitepapperleadregistrationpage(self.driver, self.globaldict, datadict)
        print('object created helloworld')
        result = whitepage.hello_world_new()
        stepdict = {}
        stepdict['expected'] = 'Hello world'
        stepdict['actual'] = result['actual']
        stepdict['status_id'] = result['status_id']
        return stepdict



