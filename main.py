from Factoring import *
from meth import *
from Intrest import *

from tkinter import *
from tkinter import ttk

def mainLoop():
    Input = input("1 - Factor | ENTER INPUT:\n")
    if Input == "1":
        InputFactor = input("Enter a,b,c:\n")
        a,b,c = InputFactor.split(",")
        Factor(int(a),int(b),int(c))    
    #FindFactors(-20)
    mainLoop()

#mainLoop()

compound(6,100,"333000000x")

#Math calculator diamond methode - choose value opperations
