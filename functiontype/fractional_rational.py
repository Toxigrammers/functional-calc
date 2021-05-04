from equationcontrols import equation_resolver
from functiontype.check_sign import get_existance, print_value
from equationcontrols.equation_resolver import solve_equation

dominio = [0]
num = [0]
den = [0]
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
    if sol != False: 
        num = get_existance(x1)
        print_value(x1)

def denominator(x2):
    print("\nCalcolo denominatore:")
    sol = solve_equation(x2)
    if sol != False:
        num = get_existance(x2)
        print_value(x2)

def rational_function(x1, x2):
    # inserire funzioni controllo impossibile
    if domain(x2) == True:  # se il dominio non è impossibile
        numerator(x1)
        denominator(x2)