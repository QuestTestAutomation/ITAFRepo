from Sandbox.Libraries.DEV.trlib1 import *
"""
class trail3:

    def __init__(self):
        pass
        t2 = trail2.test2()
t2.get_pro_id()
"""
cli = openconnection('https://tr.labs.quest.com/testrail/', 'seshikanth.anumolu@quest.com', 'P@ssw0rd@18')
"""
pro1 = get_projects(cli)
for pro in pro1:
    print(pro)
cas = get_case(cli, '138815')
print(cas)

cass = get_cases(cli, '16/35')
print(cass)
for cas in cass:
    print(cas)
projectname = 'Siebel'

cass = cli.send_get('get_suites/16')
print(cass)
for cas in cass:
    print(cas)
projectname = 'Siebel'
#result = cli.send_post('add_run/16')
#print(result)

cass = cli.send_get('get_sections/16\35')
print("Sections")
print(cass)
for cas in cass:
    print(cas)
"""
"""
cass = cli.send_get('get_cases/16&suite_id=35&section_id=13365')
print("Sections Cases")
print(len(cass))
for cas in cass:
    print(cas)

troy = {
	"suite_id": 35,
	"name": "This is a new test run1",
    "include_all": True
	}

result = cli.send_post('add_run/16',troy)
print(result)
"""
troy1 = {
	"status_id": 1,
	"comment": "This is a comment",
    "custom_step_results": [
		{
			"content": "Step 1",
			"expected": "Expected Result 1000",
			"actual": "Actual Result 1",
			"status_id": 1
		}]
	}


result = cli.send_post('add_result_for_case/928/138839',troy1)
print(result)

result = cli.send_get('get_run/928')

print(result)
