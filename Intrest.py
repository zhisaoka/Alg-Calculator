from meth import *
from decimal import *
from meth import *

tolerance = .01

def compound(a, r, t, c=1):
    global tolerance
    
    if type(t) == str:
        findX = True
        x = int(t.split("x")[0])
        t = 1
        print(x,t)
    else:
        findX = False
    
    if type(r) == str:
        findR = True
        x = int(r.split("x")[0])
        print(x)
        r = 1
        print(x, r)
    else:
        findR = False
    
    if type(a) == str:
        findA = True
        x = int(a.split("x")[0])
        print(x)
        a = 1
        print(x, a)
    else:
        findA = False
    
    r = r/100
    
    if findX != False: ## FIND X ##
        while (a*(1+(r/c))**(t*c)) <= x:
            t+=tolerance
            print("t:",t)
            print(x, t)
        print("solution: t aproximates to", t)
    
    
    if findR != False: ## FIND R ##
        while (a*(1+(r/c))**(t*c)) <= x:
            r+=tolerance
            print("r:",r)
            print(x, r)
        print("solution: r aproximates to", r)
    
    if findA != False: ## FIND A ##
        while (a*(1+(r/c))**(t*c)) <= x:
            a+=tolerance
            print("a:",a)
            print(x, a)
        print("solution: A aproximates to", a)
        
    compounding = a*(1+(r/c))**(t*c)
    print(compounding)
