from equationcontrols import separateValues

dominio = [], num = [], den = []

def domain(x2):
    print("\nCalcolo dominio:")
    sol = solve_equation(x2)
    check = True
    if sol == False: # Impossibile
        check = False
    else:
        dominio = sol
        print("Valori del domino:")
        for i in range(len(dominio)):
            print("\nx diverso da: "+str(dominio[i]))
    return check

def numerator(x1):
    print("\nCalcolo numeratore:")
    sol = solve_equation(x1)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        num = sol
        print("Valori del numeratore:")
        for i in range(len(num)):
            print("\n"+str(num[i]))

def denominator(x2):
    print("\nCalcolo denominatore:")
    sol = solve_equation(x2)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        den = sol
        print("Valori del denominatore:")
        for i in range(len(den)):
            print("\n"+str(den[i]))

def rational_function(x1, x2):
    # inserire funzioni controllo impossibile
    if domain(x2) == True:  # se il dominio non è impossibile
        numerator(x1)
        denominator(x2)