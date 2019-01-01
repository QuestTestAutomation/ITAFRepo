from Sandbox.Libraries.DEV import TestRailLibrary

tlib = TestRailLibrary.TestRailLibrary('https://tr.labs.quest.com/testrail/', 'seshikanth.anumolu@quest.com', 'P@ssw0rd@20')
#tlib.__init__('https://tr.labs.quest.com/testrail/', 'seshikanth.anumolu@quest.com', 'P@ssw0rd@28')
result = tlib.Get_TestRail_ProjectID(tlib,'Channel Business Management')
print(result)
projects = tlib.get_projects()
#projid= tlib.Get_TestRail_ProjectID()Get_TestRail_ProjectID
