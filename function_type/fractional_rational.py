from equation_controls.equation_resolver import solve_equation, print_value
from function_type.check_sign import print_existance, print_sign

def domain(x2):
    print("\nCalcolo dominio:")
    sol = solve_equation(x2) # get equation solution
    if not sol:  # Impossibile
        return False
    else:
        print("Valori del domino:")
        for i in sol:
            print("\nx diverso da: " + str(i))
        return True


def numerator(x1):
    print("\nCalcolo numeratore:")
    sol = solve_equation(x1) # get equation solution
    if sol:
        print_value(x1)
        print("\nValori esistenza:")
        print_existance(x1)


def denominator(x2):
    print("\nCalcolo denominatore:")
    sol = solve_equation(x2) # get equation solution
    if sol:
        print_value(x2)
        print("\nValori esistenza:")
        print_existance(x2)


def rational_function(x1, x2):
    if domain(x2):  # if domain is not impossible
        numerator(x1)
        denominator(x2)
        print_sign(x1, x2)