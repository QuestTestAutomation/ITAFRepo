from ITAFRepo.Dev.TestRails import ITAFTestRailLibrary
from ITAFRepo.Dev.Utilities import Utillib
from ITAFRepo.Dev.Excel import XLLib

ResultsFile = "C:/Users/sanumolu/Documents/PatchResults/Consolidated Patch Testing Results 15Feb2019.xlsx"
TestRailURL = 'https://tr.labs.quest.com/testrail/'
TestRailUser = 'seshikanth.anumolu@quest.com'
TestRailPassword = 'P@ssw0rd@24'
project_name = "MS Patching"
run_name = "MS Patching 2/15/2019"

tlibe = ITAFTestRailLibrary.TestRailLibraryExt(TestRailURL, TestRailUser, TestRailPassword)
runid = tlibe.Get_TestRail_RunID(tlibe,project_name,run_name)
print("runid")
print(runid)
XLLib = XLLib.XLLib()
sheet = "master"
tabledictinoary = XLLib.load_xl_cell_values_dictionary(ResultsFile,sheet)
print(tabledictinoary)

tableheaderdictinoary = tuple(XLLib.get_table_row_as_dictionary(1,tabledictinoary))
print(tableheaderdictinoary)
#print(tableheaderdictinoary.index['ID'])
casetemptupple = []
testidrow = '0'
for i in range(2,len(tabledictinoary)):

    if tabledictinoary.get(str(i)) != 'None':

        casetemptupple.append(((tabledictinoary.get(str(i)))[int(testidrow)])[1:])
        #print(str(tabledictinoary.get(str(i))))
        #print(str(((tabledictinoary.get(str(i)))[int(testidrow)])[1:]))
        #print(str(((tabledictinoary.get(str(i)))[2])))
        trailscaseid = str(((tabledictinoary.get(str(i)))[int(testidrow)])[1:])

        status = str(((tabledictinoary.get(str(i)))[3]))
        print(status)
        if status.upper() == 'PASS':
            statusID = 1
        else:
            statusID = 5

        print(statusID)
        result = {
            "status_id": statusID,
            "comment": "This is a comment",
            "custom_step_results": [
                {
                    "content": "Step 1",
                    "expected": str(((tabledictinoary.get(str(i)))[1])),
                    "actual": str(((tabledictinoary.get(str(i)))[2])),
                    "status_id": statusID
                }]
        }
        trurlstring = "add_result_for_case/" + str(runid) +  "/" + str(trailscaseid)
        tlibe.Add_Result_To_TestRail_Case_details(project_name,run_name,trailscaseid,result)
       # res = tlibe.send_post(trurlstring, result)
        print(trurlstring)
        #print(res)
print(casetemptupple)

print(tlibe.Get_TestRail_RunID(tlibe,project_name,run_name))




