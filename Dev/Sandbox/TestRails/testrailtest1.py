from Sandbox.Libraries.DEV.TRLibi import *

#from ..Libraries.TestRailLibrary import TestRailLibrary


"""
class test2():

    def __init__(self):
        pass
"""
tlib = trlibrary()
"""
con = tlib.openconnection('http://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@20')
case = con.send_get('get_projects')
print(case)
print(len(case))
"""
tlib.get_projects()


#TRLIB = TestRailLibrary1('http://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@18')
#TRLIB = TestRailLibrary.__init__('https://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@18')
#tlib = TestRailLibrary.TestRailLibrary('https://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@18')
#TRLIB.__init__('https://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@18')