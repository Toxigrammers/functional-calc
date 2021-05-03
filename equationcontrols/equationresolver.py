import math
import python.functionalcalc.equationcontrols.separateValues
#import separateValues

def firstDegree(equ):
    a,b = separateFirstDegree(equ)
    x = (-b)/a
    print("Il risultato di x è "+x)

def secondDegree(equ):
    a,b,c = separateSecondDegree(equ)
    if(checkDelta(a,b,c)):
        n = Equation(a,b,c)
        if(len(n) == 1):
            print('Il risultato di x1 e x2 è '+str(n[0]))
        else:
            print('Il risultato di x1 è {} e x2 è {}'.format(n[0],n[1]))
    else:
        print("Calcolo impossibile")

def checkDegree(equ):  # check equation degree
    if(equ.contains('x^2')):
        n = 2
    elif(equ.contains('x')):
        n = 1
    else:
        n = 0
    return n

def checkDelta(a,b,c):  # check if delta is less than 0
    check = False
    delta = (b*b)-(4*a*c)
    if(delta>=0):
        check = True
    return check

def Equation(a,b,c):
    delta = (b*b)-(4*a*c)
    delta = math.sqrt(delta)
    n1 = (-b + delta)/(2*a)
    n2 = (-b - delta)/(2*a)
    n = []
    if(n1 == n2):
        n.append(n1)
    else:
        n.append(n1)
        n.append(n2)
    return n

scelta = "1"
while(scelta != "si"):
    print("\nNo space and comma to separate values\nequation format example: -x^2,+3x,-2")
    equ = input("Inserire equazione : ")
    if(checkDegree(equ)==1):
        firstDegree(equ)
    elif(checkDegree(equ)==2):
        secondDegree(equ)
    scelta = input("Vuoi uscire? (si/no): ")
