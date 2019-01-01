from ITAFRepo.Dev.Utilities import QSTAFrameworkLib
import os



Variablesfile  = 'C:/Users/sanumolu/Documents/QSTAFGdrive/VDI 1/ITAF/ITAFRepo/Dev/Resources/ITAFParameters.cfg'
filehandle = open(Variablesfile)
parameter_dict = {}
for Line in filehandle:
    #print(Line)
    Line = Line.strip()
    print(Line)
    #Initiatlize a parameter Dictinoary
    if not Line.startswith("#"):
        filekeyvalue = Line.split("=")
        if len(filekeyvalue) == 2:
            parameter_dict[filekeyvalue[0].strip()] = filekeyvalue[1].strip()

print(parameter_dict)

QSTAFLib = QSTAFrameworkLib.QSTAFrameworkLib()

QSTAFLib.initializevariables(QSTAFLib,Variablesfile)