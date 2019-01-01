client = APIClient('https://tr.labs.quest.com/testrail/')
client.user = 'seshikanth.anumolu@quest.com'
client.password = 'P@ssw0rd@18'

#case = client.send_get('get_case/1/C21742')
case = client.send_get('get_projects')
print(case)
print(len(case))
#pprint(case)

#for c in case :
#print(c)
n = 0
cbmid = ""
while n < len(case) :
    case[n]['name']
    if case[n]['name'] == 'Channel Business Management':
        print(case[n]['name'])
        print(case[n]['id'])
        cbmid = case[n]['id']
    print(case[n]['name'])
    n = n + 1


