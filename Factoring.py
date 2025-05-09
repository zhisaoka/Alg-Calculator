import math
from meth import inverse

debug = False

def checkDecimal(x):
    return x == math.floor

def FindFactors(x):
    if debug:
        print(f"Executing: FindFactors({x})")
    factors = []
    for i in range(1, abs(x) + 1): # range from 1 - positive(x)/absolute value + 1(within)
        if x % i == 0:
            factors.append(i)
            factors.append(-i)
    
    if debug:
        print(f"Factors: {factors}")
    return factors

def FactorValues(a,b,c):
    if debug:
        print(f"Executing: FactorValues{a,b,c}")
    ac = a*c
    factors = FindFactors(ac)
    
    for i in range(len(factors)): # Repeat by quantity of factors,
        for j in range(len(factors)): # for all factors,
            # set varibles
            f1 = factors[i] # grabs a factor by i's value, increases after every cycle
            f2 = factors[j] # grabs a second factor by j, increasing during every cycle
            
            if f1*f2 == ac and f1+f2 == b :
                if debug:
                    print(f"found: {f1} + {f2} = {b}:{f1+f2}")
                return f1, f2
    return None,None # if none are found

def Diamond(a, b, c, x, y):
    if debug:
        print(f"Executing: Diamond{a,b,c,x,y}")
    def s(count):
        return "  " * count

    ac = a * c
    count = 0
    length = 10

    for i in range(length + 1):
        if count <= int(length / 2):
            if count == round((length / 2) / 2.5):
                print(f"{s(count)}.{s(count + 1)}{ac}{s(length - count * 3 - 1)}.")
            elif count == round(length / 2):
                print(f"{s(round(count / 2))}{x}{s(round(count / 2))} .{s(length - count * 3 - 1)}.{s(round(count / 2) + 1)}{y}")
            else:
                print(f"{s(count)}.{s(length - count - count)}.")
            count += 1
        else:
            if count == round(length / 2 + (length / 2 / 2)):
                print(f"{s(length - count)}.{s(round(count / 2 - 1))}{b}{s(round(count / 2 - 1))}.")
            else:
                print(f"{s(length - count)}.{s(count + count - length)}.")
            count += 1

def Factor(a, b, c):
    if debug:
        print(f"Executing: Factor{a,b,c}")
    x, y = FactorValues(a, b, c)

    if x is not None and y is not None:
        Diamond(a, b, c, x, y)
    else:
        print("No valid factor pair found.")
