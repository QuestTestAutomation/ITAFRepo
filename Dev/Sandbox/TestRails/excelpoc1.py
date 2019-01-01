from Sandbox.Libraries.DEV import XLLib

xltest = XLLib.XLLib()
xltest.pri()

Xlfile = 'C:\\Users\\SANUMOLU\\Documents\\files\TestRail\\trail1.xlsx'
XLSheet = "master"
print(xltest.get_xl_row_count(Xlfile,XLSheet))
print(xltest.get_XL_column_count(Xlfile,XLSheet))
xlrowcount = int(xltest.get_xl_row_count(Xlfile,XLSheet))
xlcolumncount = int(xltest.get_XL_column_count(Xlfile,XLSheet))
xlheaderdict = {}
xlheaderdictlist = []
datatablelist = []
for xlcolumn in range(1, xlcolumncount):
    print("column number is : " + str(xlcolumn))
    print(xltest.get_xl_cell_value(Xlfile, XLSheet, 1, int(xlcolumn)))
    xlheaderdictlist.append(xltest.get_xl_cell_value(Xlfile, XLSheet, 1, int(xlcolumn)))


print(xlheaderdictlist)
for xlheader in xlheaderdictlist:
    print("xlheader is :" + xlheader)
for xlcolumn in range(0, len(xlheaderdictlist)):
    print(int(xlcolumn))

    print("xlheaderlist is :" + xlheaderdictlist[int(xlcolumn)])

for xlrow in range(1,int(xlrowcount)):
    print("row number is : " + str(xlrow))
    for xlcolumn in range(1,xlcolumncount):
        xlheaderdict[xlheaderdictlist[int(xlcolumn)-1]] = xltest.get_xl_cell_value(Xlfile,XLSheet,int(xlrow),int(xlcolumn))
        print("column number is : " + str(xlcolumn))
        print(xltest.get_xl_cell_value(Xlfile,XLSheet,int(xlrow),int(xlcolumn)))
    datatablelist.append(xlheaderdict)

print(datatablelist)