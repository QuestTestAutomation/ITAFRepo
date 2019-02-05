#from datetime import datetime
import datetime
import time
import pytz
import re


now_time = datetime.datetime.now().time()
start = datetime.time(17, 30)
end = datetime.time(4, 00)
if now_time >= start or now_time <= end:
    print('true')
else:
    print('false')

SROpenDatetime = '09/20/2019 6:59:07 PM'
SRopendatetime1 = datetime.datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p')
print(SRopendatetime1)
SRopendate = datetime.datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p').date()
print(SRopendate)
SRopentime= datetime.datetime.strptime(SROpenDatetime,'%m/%d/%Y %I:%M:%S %p').time()
print(SRopentime)

localtime = pytz.timezone('US/Pacific')

SROpendate_tz_info = datetime(SRopendate.year, SRopendate.month, SRopendate.day, tzinfo=pytz.timezone('US/Pacific'))
print(bool(SROpendate_tz_info.dst))
mydate = localtime.localize(SRopendate,is_dst=None)
print(localtime.localize(SRopendatetime1))
print(bool(mydate.dst))


"""

#NAM_Start_time =
#a = localtime.localize(SRopendate)
#print(bool(a.dst()))

new = re.sub('[^0-9]', '', str(SRopendatetime1))

print(int(new))


#timestamp = time.mktime()
#print(timestamp)
print(bool(time.localtime(int(new)).tm_isdst))
"""
