from Sandbox.Libraries.DEV import TestRailLibraryExt
from Sandbox.Libraries.DEV import Utillib
from Sandbox.Libraries.DEV import XLLib
from Sandbox.Libraries.DEV import GlobalVariables


#gvar = GlobalVariables.globalvariables()
XLLib = XLLib.XLLib()
File = "c:/files/master.xlsx"
sheet = "master"
#print(XLLib.load_xl_cell_values_dictionary(File,sheet))
tabledictinoary = XLLib.load_xl_cell_values_dictionary(File,sheet)
#XLLib.get_table_row_as_dictionary(2,tabledictinoary)
#print(len(tabledictinoary))
tableheaderdictinoary = tuple(XLLib.get_table_row_as_dictionary(1,tabledictinoary))
print(tableheaderdictinoary)
print(tableheaderdictinoary.index['ID'])
casetemptupple = []
testidrow = '0'
for i in range(2,len(tabledictinoary)):
    #casetemptupple.append(tabledictinoary.get(str(i)))
    if tabledictinoary.get(str(i)) != 'None':
        #print((tuple(tabledictinoary.get(str(i)))[int(testidrow)])[1:])
        #print(((tabledictinoary.get(str(i)))[int(testidrow)])[1:])
        #casetemptupple.append((tabledictinoary.get(str(i))[0]))
        casetemptupple.append(((tabledictinoary.get(str(i)))[int(testidrow)])[1:])
        #print(str(tabledictinoary.get(str(i))))
print(casetemptupple)
"""

  #  for val in tabledictinoary.get(str(i)):
  #      print(val[1])
    #print(tabledictinoary.get(str(i)).[0])

#for key, value in tabledictinoary.items():
#    print(value.keys()[0])
casetupple = []
for j  in range(1,len(casetemptupple)):
    print(casetemptupple[j])
    m = casetemptupple[j]
    if casetemptupple[j] != 'None':
        n = tuple(m)
        print(n[0])
        print(m[0])
"""
