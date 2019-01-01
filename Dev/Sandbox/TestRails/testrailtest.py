class TRLib():

    def __init__(self, TestRailURL='https://tr.labs.quest.com/testrail/', user='seshikanth.anumolu@quest.com', APIkey='P@ssw0rd@18'):
        self._client = APIClient(TestRailURL)
        self._client.user = user
        self._client.password = APIkey

    def Get_TestRail_Case(self,caseid = 'T307953'):

         cases = self._client.send_get('get_cases')
         for case in cases:
             print(case)
         #return case
         """
         projects = self._client.send_get('get_projects')
         for project in projects:
             print(project)
             print(len(projects))
          """

tlib = TRLib('https://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@18')
#tlib = TRLib('http://tr.labs.quest.com/testrail/','seshikanth.anumolu@quest.com','P@ssw0rd@20')
tlib.Get_TestRail_Case('T307953')
#print(c)
