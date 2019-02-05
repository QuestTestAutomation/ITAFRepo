from datetime import datetime, timedelta
from datetime import timedelta
import time
import pytz
from ITAFRepo.Dev.DateTime import DateTimelib
from ITAFRepo.Dev.Siebel import Siebelservicelib


SROpenDatetime = '10/30/2018 12:24:50 PM'
SRopendate = datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p').date()
entstartdate = datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p').date()
SRopendatetimef = datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p')
SROpendate_tz_info = datetime(SRopendatetimef .year, SRopendatetimef .month, SRopendatetimef.day, tzinfo=pytz.timezone('US/Pacific'))
print(SROpendate_tz_info)
print(bool(SROpendate_tz_info.dst()))

pstz = pytz.timezone('US/Pacific')
pstz.localize((datetime(SRopendatetimef .year, SRopendatetimef .month, SRopendatetimef.day))).dst()
print(bool(pstz.localize((datetime(SRopendatetimef .year, SRopendatetimef .month, SRopendatetimef.day))).dst()))

print(DateTimelib.datetimelib.verify_date_is_dst(SROpenDatetime,'US/Pacific'))

SLAdict = {}
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
SLAdict['APMER_workdays'] = (0,1,2,3,4)
SLAdict['EMEA_workdays'] = (0,1,2,3,4)
SLAdict['JAPAN_workdays'] = (0,1,2,3,4,6)
SLAdict['APAC_workdays'] = (0,1,2,3,4,6)



print(SLAdict)

print(SRopendatetimef.weekday())
print(SRopendatetimef.weekday() in SLAdict['APAC_workdays'])
entitlementregion = 'AMER'
entitlementworkingdays = SLAdict['APMER_workdays']
if entitlementregion.upper() == 'AMER'.upper():
    entstarttime = SLAdict['AMER_Start']
    entendtime = SLAdict['AMER_End']
    entstartdatetime = str(SRopendate) + ' ' + SLAdict['AMER_Start']
    entenddatetime = str(SRopendate) + ' ' + SLAdict['AMER_End']
    print(entstartdatetime)
    print(entenddatetime)
    print(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S"))
    print(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").date())
    print(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").time())
    print(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").weekday())
#    print(datetime.strftime(entstartdatetime, "%Y-%m-%d %H:%M:%S"))
    entstartdatetimef = datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S")
    entenddatetimef = datetime.strptime(entenddatetime, "%Y-%m-%d %H:%M:%S")
    print(bool(entstartdatetimef < SRopendatetimef < entenddatetimef))

    print('******************************************************')
    print(entenddatetimef)
    print(entenddatetimef + timedelta(seconds=128800))

    print('******************************************************')

    EntitlementRegion = 'AMER'
    support = 'Y'
    severity = 'Level 4'

    SLAdict = Siebelservicelib.Siebelservicelib.set_SLA_dictinoary()
    #set entitlement start and end date
    if EntitlementRegion.upper() == 'AMER'.upper():
        entstartdatetime = str(SRopendate) + ' ' + SLAdict['AMER_Start']
        entenddatetime = str(SRopendate) + ' ' + SLAdict['AMER_End']
        entitlementworkingdays = SLAdict['APMER_workdays']
    elif EntitlementRegion.upper() == 'ALL'.upper():
        entstartdatetime = str(SRopendate) + ' ' + SLAdict['ALL_Start']
        entenddatetime = str(SRopendate) + ' ' + SLAdict['ALL_End']
        entitlementworkingdays = SLAdict['ALL_workdays']
    elif EntitlementRegion.upper() == 'EMEA'.upper():
        entstartdatetime = str(SRopendate) + ' ' + SLAdict['EMEA_Start']
        entenddatetime = str(SRopendate) + ' ' + SLAdict['EMEA_End']
        entitlementworkingdays = SLAdict['EMEA_workdays']
    elif EntitlementRegion.upper() == 'EMEA'.upper():
        entstartdatetime = str(SRopendate) + ' ' + SLAdict['EMEA_Start']
        entenddatetime = str(SRopendate) + ' ' + SLAdict['EMEA_End']
        entitlementworkingdays = SLAdict['EMEA_workdays']
    elif EntitlementRegion.upper() == 'JAPAN'.upper():
        isdst = DateTimelib.datetimelib.verify_date_is_dst(SRopendate,'US/Pacific')
        if isdst:
            entstartdatetime = str(SRopendate) + ' ' + SLAdict['JAPAN_Start_DST']
            entenddatetime = str(SRopendate) + ' ' + SLAdict['JAPAN_End_DST']
            entitlementworkingdays = SLAdict['JAPAN_workdays']
        else:
            entstartdatetime = str(SRopendate) + ' ' + SLAdict['JAPAN_Start']
            entenddatetime = str(SRopendate) + ' ' + SLAdict['JAPAN_End']
            entitlementworkingdays = SLAdict['JAPAN_workdays']
    elif EntitlementRegion.upper() == 'APAC'.upper():
        isdst = DateTimelib.datetimelib.verify_date_is_dst(SRopendate, 'US/Pacific')
        if isdst:
            entstartdatetime = str(SRopendate) + ' ' + SLAdict['APAC_Start_DST']
            entenddatetime = str(SRopendate) + ' ' + SLAdict['APAC_End_DST']
            entitlementworkingdays = SLAdict['APAC_workdays']
        else:
            entstartdatetime = str(SRopendate) + ' ' + SLAdict['APAC_Start']
            entenddatetime = str(SRopendate) + ' ' + SLAdict['APAC_End']
            entitlementworkingdays = SLAdict['APAC_workdays']

    # Set SLA start Date


    if bool(entstartdatetimef < SRopendatetimef < entenddatetimef):
        SLAstartdatetime = SRopendatetimef
    elif SRopendatetimef > entenddatetimef :
        SLAstartdate = Siebelservicelib.Siebelservicelib.get_next_working_day(SRopendatetimef.date(),entitlementworkingdays)
        SLAstartdatetime = datetime.strptime(str(SLAstartdate) + ' ' + entstarttime,"%Y-%m-%d %H:%M:%S")
    elif SRopendatetimef <= entstartdatetimef :
        SLAstartdatetime = entstartdatetimef
    print(SLAstartdatetime)




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

    #determine SLA exprity time.

    tempSLAenddatetime = SLAstartdatetime + timedelta(seconds=SLAtime)
    if tempSLAenddatetime <= entenddatetimef:
        SLAenddatetimef = tempSLAenddatetime
    elif tempSLAenddatetime > entenddatetimef:
        tempenddate = Siebelservicelib.Siebelservicelib.get_next_working_day(SRopendatetimef.date(),entitlementworkingdays)
        tempSLAstartdatetime = datetime.strptime(str(tempenddate) + ' ' + entstarttime, "%Y-%m-%d %H:%M:%S")
        tempdeltatime = tempSLAenddatetime - entenddatetimef
        print(tempdeltatime.total_seconds())
        SLAenddatetimef = tempSLAstartdatetime + timedelta(seconds=tempdeltatime.total_seconds())
    print('tempSLAenddatetime')
    print(tempSLAenddatetime)
    print(SLAenddatetimef)





    """
    print('*****---**')
    print(entstartdatetime)
    tempdate = datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").date()
    tempdate1 = tempdate + timedelta(days=1)
    print('*****---')
    print(tempdate1)
    entstartdatetime = tempdate1
    print(entstartdatetime)
    #print(bool(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").weekday() in entitlementworkingdays))
    print('----')
    #print(bool(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").weekday() not in entitlementworkingdays))
    #bolworkday = bool(datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").weekday() not in entitlementworkingdays)
    """
"""
    for i in range(1,3):
        if bool(entstartdate.weekday() in entitlementworkingdays):
            print('&&&&')
            print(entstartdate.weekday())
            print(entitlementworkingdays)
            break
        elif bool(entstartdate.weekday() not in entitlementworkingdays):
            #tempdate = datetime.strptime(entstartdate, "%Y-%m-%d").date()
            entstartdate = entstartdate + timedelta(days=1)
            print(entstartdate.weekday())
            print(entitlementworkingdays)
    print('*****')
    print(entstartdate)
"""


"""

    while bolworkday:
        tempdate = datetime.strptime(entstartdatetime, "%Y-%m-%d %H:%M:%S").date()
        tempdate1 = tempdate + timedelta(days=1)
        entstartdatetime = tempdate1
        print('*****')
        print(entstartdatetime)
        print(entstartdatetime.weekday())
        print(entstartdatetime.weekday() in entitlementworkingdays)
        bolworkday = bool(entstartdatetime.weekday() in entitlementworkingdays)

        if bool(entstartdatetime.weekday() in entitlementworkingdays):
            print('*****')
            print(entstartdatetime)
            break

def add_days_to_date(startdate,daysdelta):
    tempdate = datetime.strptime(startdate, "%Y-%m-%d %H:%M:%S").date()
    tempdate1 = tempdate + timedelta(days=daysdelta)
    return tempdate1
"""

 #   if bool(entstartdatetimef < SRopendatetimef < entenddatetimef):
 #       SRSLAStartDatetime = SRopendatetimef
 #       print(SRSLAStartDatetime)




















"""

localtime = pytz.timezone('US/Pacific')
mydate = localtime.localize(SROpendate_tz_info)
print(mydate)
print(bool(time.localtime(mydate ).tm_isdst))
print(bool(time.localtime(SROpendate_tz_info).tm_isdst))
"""