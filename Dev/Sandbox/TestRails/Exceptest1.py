import inspect

def Exceptionmod(err,functionname):
    print(err)
    print(functionname)

def add(a,b):

    try :
        c = a + b
    except:
        print("exception raised")
        e = "All exception"
        Exceptionmod(e,inspect.stack()[0][3])

x1 = 1
x2 = "3"
print(add(x1,x2))