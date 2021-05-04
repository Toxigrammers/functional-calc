from equationcontrols import equation_resolver
from functiontype.check_sign import get_existance, print_existance

dominio = [0]
num = [0]
den = [0]
def domain(x2):
    print("\nCalcolo dominio:")
    sol = equation_resolver.solve_equation(x2)
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
    sol = equation_resolver.solve_equation(x1)
    if sol != False: 
        equation_resolver.print_value(x1)
        print("\nValori esistenza:")
        print_existance(x1)

def denominator(x2):
    print("\nCalcolo denominatore:")
    sol = equation_resolver.solve_equation(x2)
    if sol != False:
        equation_resolver.print_value(x2)
        print("\nValori esistenza:")
        print_existance(x2)

def rational_function(x1, x2):
    # inserire funzioni controllo impossibile
    if domain(x2) == True:  # se il dominio non è impossibile
        numerator(x1)
        denominator(x2)
        print_sign(x1,x2)