from equationcontrols import separateValues

dominio = [], num = [], den = []

def Dominio(x2):
    print("\nCalcolo dominio:")
    sol = solveEquation(x2)
    check = True
    if sol == False: # Impossibile
        check = False
    else:
        dominio = sol
        print("Valori del domino:")
        for i in range(len(dominio)):
            print("\nx diverso da: "+str(dominio[i]))
    return check

def Num(x1):
    print("\nCalcolo numeratore:")
    sol = solveEquation(x1)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        num = sol
        print("Valori del numeratore:")
        for i in range(len(num)):
            print("\n"+str(num[i]))

def Den(x2):
    print("\nCalcolo denominatore:")
    sol = solveEquation(x2)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        den = sol
        print("Valori del denominatore:")
        for i in range(len(den)):
            print("\n"+str(den[i]))

def rationalFunction(x1, x2):
    # inserire funzioni controllo impossibile
    if Dominio(x2) == True:  # se il dominio non è impossibile
        Num(x1)
        Den(x2)