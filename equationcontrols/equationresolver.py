import math
from equationcontrols.separateValues import separate

def firstGrade():

def secondGrade():

def checkEqu(equ):  # check equation 
    x2 = equ.find("x^2")
    x1 = equ.find("x")
    if(x2 != -1):
        n = 2
    elif(x2 == 1 and x1 !=-1):
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

def calcEqu2(equ):
    a,b,c = separate(equ)
    if(checkDelta(a,b,c)):
        n = Equation(a,b,c)
        print("n length = "+str(len(n)))
        if(len(n)==1):
            
            print("Il risultato di x1 e x2 è "+str(n[0]))
        else:
            print("Il risultato di x1 è "+str(n[0])+" e x2 è "+str(n[1]))
    else:
        print("Calcolo impossibile")

scelta = "1"
print("Il programma funziona con valori minori di 100 e con equazioni di grado massimo 2")
while(scelta != "si"):
    print("² = ^2")
    equ = input("Inserire equazione : ")
    if(checkEqu(equ)==1):
        calcEqu(equ)
    else(checkEqu(equ)==2):
        calcEqu2(equ)
    scelta = input("Vuoi uscire? (si/no): ")
