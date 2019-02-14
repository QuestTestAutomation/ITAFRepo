from ITAFRepo.Dev.Utilities import Utillib
from datetime import datetime, timedelta
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
from ITAFRepo.Dev.DateTime import DateTimelib
import time

class Siebelservicelib(Souilib.Souilib):

    def __init__(self, driver, globaldict, url,datadict = {} ,rundict = {},resultdict = {}):
        super(Siebelservicelib, self).__init__(driver, globaldict)
        self.driver = driver
        self.webserverurl = self.get_webserver_url(url)
        self.exceptionlib = ExceptionLib.ExceptionLib()
        self.datadict = datadict
        self.rundict = rundict

    @staticmethod
    def get_next_working_day(srdate,workingdays):
         srdate = srdate + timedelta(days=1)
         for i in range(1, 3):

             if bool(srdate.weekday() not in workingdays):
                 srdate = srdate + timedelta(days=1)

             elif bool(srdate.weekday() in workingdays):
                 break
         return srdate

    @staticmethod
    def set_SLA_dictinoary():
        SLAdict = {}
        SLAdict['ALL_Start'] = '00:00:00'
        SLAdict['ALL_End'] = '23:59:59'
        SLAdict['AMER_Start'] = '05:00:00'
        SLAdict['AMER_End'] = '17:00:00'
        SLAdict['EMEA_Start'] = '00:00:00'
        SLAdict['EMEA_End'] = '09:30:00'
        SLAdict['JAPAN_Start'] = '17:00:00'
        SLAdict['JAPAN_End'] = '02:00:00'
        SLAdict['JAPAN_Start_DST'] = '16:00:00'
        SLAdict['JAPAN_End_DST'] = '01:00:00'
        SLAdict['APAC_Start'] = '15:00:00'
        SLAdict['APAC_End'] = '02:00:00'
        SLAdict['APAC_Start_DST'] = '14:00:00'
        SLAdict['APAC_End_DST'] = '01:00:00'
        SLAdict['APMER_workdays'] = (0, 1, 2, 3, 4)
        SLAdict['EMEA_workdays'] = (0, 1, 2, 3, 4)
        SLAdict['JAPAN_workdays'] = (0, 1, 2, 3, 4, 6)
        SLAdict['APAC_workdays'] = (0, 1, 2, 3, 4, 6)
        SLAdict['ALL_workdays'] = (0, 1, 2, 3, 4, 6)
        SLAdict['STD_Level1'] = (3600 - 3)
        SLAdict['STD_Level2'] = (7200 - 3)
        SLAdict['STD_Level3'] = (14400 - 3)
        SLAdict['STD_Level4'] = (28800 - 3)
        SLAdict['Premier_Level1'] = (1800 - 3)
        SLAdict['Premier_Level2'] = (3600 - 3)
        SLAdict['Premier_Level3'] = (7200 - 3)
        SLAdict['Premier_Level4'] = (14400 - 3)


        return SLAdict

    @staticmethod
    def calculate_sla_expiry_time(SROpenDatetime,EntitlementRegion,severity,support):
        SRopendate = datetime.strptime(SROpenDatetime, '%m/%d/%Y %I:%M:%S %p').date()

        SLAdict = Siebelservicelib.set_SLA_dictinoary()
        # set entitlement start and end date
        if EntitlementRegion.upper() == 'AMER'.upper():
            entstarttime = SLAdict['AMER_Start']
            entendtime = SLAdict['AMER_End']
            entitlementworkingdays = SLAdict['APMER_workdays']
        elif EntitlementRegion.upper() == 'ALL'.upper():
            entstarttime = SLAdict['ALL_Start']
            entendtime = SLAdict['ALL_End']
            entitlementworkingdays = SLAdict['ALL_workdays']
        elif EntitlementRegion.upper() == 'EMEA'.upper():
            entstarttime = SLAdict['EMEA_Start']
            entendtime = SLAdict['EMEA_End']
            entitlementworkingdays = SLAdict['EMEA_workdays']
        elif EntitlementRegion.upper() == 'EMEA'.upper():
            entstartdatetime = str(SRopendate) + ' ' + SLAdict['EMEA_Start']
            entenddatetime = str(SRopendate) + ' ' + SLAdict['EMEA_End']
            entitlementworkingdays = SLAdict['EMEA_workdays']
        elif EntitlementRegion.upper() == 'JAPAN'.upper():
            isdst = DateTimelib.datetimelib.verify_date_is_dst(SROpenDatetime, 'US/Pacific')
            if isdst:
                entstarttime = SLAdict['JAPAN_Start_DST']
                entendtime = SLAdict['JAPAN_End_DST']
                entitlementworkingdays = SLAdict['JAPAN_workdays']
            else:
                entstarttime = SLAdict['JAPAN_Start']
                entendtime = SLAdict['JAPAN_End']
                entitlementworkingdays = SLAdict['JAPAN_workdays']
        elif EntitlementRegion.upper() == 'APAC'.upper():
            isdst = DateTimelib.datetimelib.verify_date_is_dst(SROpenDatetime, 'US/Pacific')
            if isdst:
                entstarttime = SLAdict['APAC_Start_DST']
                entendtime = SLAdict['APAC_End_DST']
                entitlementworkingdays = SLAdict['APAC_workdays']
            else:
                entstarttime = SLAdict['APAC_Start']
                entendtime = SLAdict['APAC_End']
                entitlementworkingdays = SLAdict['APAC_workdays']

        # format date
        SRopendatetimef = datetime.strptime(SROpenDatetime, '%m/%d/%Y %I:%M:%S %p')

        # Set SLA start Date
        if (bool(SRopendate.weekday()) in entitlementworkingdays):
            tempstartdate = SRopendate

        else:
            tempstartdate = Siebelservicelib.Siebelservicelib.get_next_working_day(SRopendatetimef.date(), entitlementworkingdays)

        entstartdatetime = str(tempstartdate) + ' ' + entstarttime
        if EntitlementRegion.upper() == 'APAC'.upper() or EntitlementRegion.upper() == 'JAPAN'.upper():
            tempenddate = tempstartdate + timedelta(days=1)
        else:
            tempenddate = tempstartdate
        entenddatetime = str(tempenddate) + ' ' + entendtime

        entstartdatetimef = datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S")
        entenddatetimef = datetime.strptime(entenddatetime, "%Y-%m-%d %H:%M:%S")
        SRopendatetimef = datetime.strptime(SROpenDatetime, '%m/%d/%Y %I:%M:%S %p')

        if bool(entstartdatetimef < SRopendatetimef < entenddatetimef):
            SLAstartdatetime = SRopendatetimef
        elif SRopendatetimef > entenddatetimef:
            SLAstartdate = Siebelservicelib.get_next_working_day(SRopendatetimef.date(), entitlementworkingdays)
            SLAstartdatetime = datetime.strptime(str(SLAstartdate) + ' ' + entstarttime, "%Y-%m-%d %H:%M:%S")
        elif SRopendatetimef <= entstartdatetimef:
            SLAstartdatetime = entstartdatetimef
        print('SLAstartdatetime')
        print(SLAstartdatetime)
        # Calculate End Date based on start date
        if EntitlementRegion.upper() == 'APAC'.upper() or EntitlementRegion.upper() == 'JAPAN'.upper():
            tempenddate = tempstartdate + timedelta(days=1)
        else:
            tempenddate = tempstartdate
            ""
        entenddatetime = str(tempenddate) + ' ' + entendtime

        print('entenddatetime')
        print(entenddatetime)
        # format dates
        entstartdatetimef = datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S")
        entenddatetimef = datetime.strptime(entenddatetime, "%Y-%m-%d %H:%M:%S")

        if (severity.upper() == 'Level 1'.upper()) and (support.upper() == 'Y'.upper()):
            SLAtime = SLAdict['Premier_Level1']
        elif (severity.upper() == 'Level 2'.upper()) and (support.upper() == 'Y'.upper()):
            SLAtime = SLAdict['Premier_Level2']
        elif (severity.upper() == 'Level 3'.upper()) and (support.upper() == 'Y'.upper()):
            SLAtime = SLAdict['Premier_Level3']
        elif (severity.upper() == 'Level 4'.upper()) and (support.upper() == 'Y'.upper()):
            SLAtime = SLAdict['Premier_Level4']

        elif (severity.upper() == 'Level 1'.upper()) and (support.upper() == 'N'.upper()):
            SLAtime = SLAdict['STD_Level1']
        elif (severity.upper() == 'Level 2'.upper()) and (support.upper() == 'N'.upper()):
            SLAtime = SLAdict['STD_Level2']
        elif (severity.upper() == 'Level 3'.upper()) and (support.upper() == 'N'.upper()):
            SLAtime = SLAdict['STD_Level3']
        elif (severity.upper() == 'Level 4'.upper()) and (support.upper() == 'N'.upper()):
            SLAtime = SLAdict['STD_Level4']

        print(SLAtime)

        # determine SLA exprity time.

        tempSLAenddatetime = SLAstartdatetime + timedelta(seconds=SLAtime)
        print(tempSLAenddatetime)
        print(entenddatetimef)
        print(tempSLAenddatetime <= entenddatetimef)
        if tempSLAenddatetime < entenddatetimef:
            SLAenddatetimef = tempSLAenddatetime
        elif tempSLAenddatetime > entenddatetimef:
            tempenddate = Siebelservicelib.get_next_working_day(SRopendatetimef.date(), entitlementworkingdays)
            print('tempenddate')
            print(tempenddate)
            tempSLAstartdatetime = datetime.strptime(str(tempenddate) + ' ' + entstarttime, "%Y-%m-%d %H:%M:%S")
            print('tempSLAstartdatetime')
            print(tempSLAstartdatetime)
            tempdeltatime = tempSLAenddatetime - entenddatetimef
            print(tempdeltatime.total_seconds())
            SLAenddatetimef = tempSLAstartdatetime + timedelta(seconds=tempdeltatime.total_seconds())
        print('tempSLAenddatetime')
        print(tempSLAenddatetime)
        print(SLAenddatetimef)
        # print(time.strftime('%m/%d/%Y %I:%M:%S %p',SLAenddatetimef))
        print(SLAenddatetimef.strftime('%m/%d/%Y %I:%M:%S %p'))
        return SLAenddatetimef.strftime('%m/%d/%Y %I:%M:%S %p')


    def load_sr_test_data(self,datafile):
        pass