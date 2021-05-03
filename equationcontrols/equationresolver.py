import math
import python.functionalcalc.equationcontrols.separateValues
#import separateValues

def firstDegree(equ):
    a,b = separateFirstDegree(equ)
    x = (-b)/a
    n = [x]
    return n

def secondDegree(equ):
    a,b,c = separateSecondDegree(equ)
    if checkDelta(a,b,c):
        x1,x2 = Equation(a,b,c)
        n = [x1,x2]
        return n
    else:
        print("\nCalcolo impossibile")
        return False

def checkDegree(equ):  # check equation degree
    if 'x^2' in equ:
        n = 2
    elif 'x' in equ:
        n = 1
    else:
        n = 0
    return n

def checkDelta(a,b,c):  # check if delta is less than 0
    check = False
    delta = (b*b)-(4*a*c)
    if delta>=0:
        check = True
    return check

def Equation(a,b,c):
    delta = (b*b)-(4*a*c)
    delta = math.sqrt(delta)
    n1 = (-b + delta)/(2*a)
    n2 = (-b - delta)/(2*a)
    return n1,n2

def solveEquation(equ):
    if checkDegree(equ)==1:
        return firstDegree(equ)
    elif checkDegree(equ)==2:
        return secondDegree(equ)

scelta = "1"
while(scelta != "si"):
    print("\nNo space and comma to separate values\nequation format example: -x^2,+3x,-2")
    equ = input("Inserire equazione : ")
    solveEquation(equ)
    scelta = input("Vuoi uscire? (si/no): ")
