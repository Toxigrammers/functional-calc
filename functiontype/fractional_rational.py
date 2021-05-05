from equationcontrols import equation_resolver
from functiontype.check_sign import print_existance, print_sign

dominio = [0]
num = [0]
den = [0]


def domain(x2):
    print("\nCalcolo dominio:")
    sol = equation_resolver.solve_equation(x2)
    check = True
    if not sol:  # Impossibile
        check = False
    else:
        dominio = sol
        print("Valori del domino:")
        for i in dominio:
            print("\nx diverso da: " + str(i))
    return check


def numerator(x1):
    print("\nCalcolo numeratore:")
    sol = equation_resolver.solve_equation(x1)
    if sol:
        equation_resolver.print_value(x1)
        print("\nValori esistenza:")
        print_existance(x1)


def denominator(x2):
    print("\nCalcolo denominatore:")
    sol = equation_resolver.solve_equation(x2)
    if sol:
        equation_resolver.print_value(x2)
        print("\nValori esistenza:")
        print_existance(x2)


def rational_function(x1, x2):
    # inserire funzioni controllo impossibile
    if domain(x2):  # se il dominio non è impossibile
        numerator(x1)
        print_existance(x1)
        denominator(x2)
        print_existance(x2)
        print_sign(x1, x2)
