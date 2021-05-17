from equation_controls.equation_resolver import check_degree, solve_equation, print_value
from function_type.check_sign import print_existance, print_sign, get_existance, get_all_solution, get_sign, get_all_sign

def domain(den):
    print("\nCalcolo dominio:")
    sol = solve_equation(den) # get equation solution
    if not sol:  # Impossibile
        return False
    else:
        print("Valori del domino:")
        for i in sol:
            print(f"\nx diverso da: {str(i)}")
        return True


def numerator(num):
    print("\nCalcolo numeratore:")
    sol = solve_equation(num) # get equation solution
    if sol:
        print_value(num)
        print("\nValori esistenza:")
        print_existance(num)


def denominator(den):
    print("\nCalcolo denominatore:")
    sol = solve_equation(den) # get equation solution
    if sol:
        print_value(den)
        print("\nValori esistenza:")
        print_existance(den)


def rational_function(num, den):
    if domain(den):  # if domain is not impossible
        numerator(num)
        denominator(den)
        print_sign(num, den)

def gui_return_values(num, den):
    if solve_equation(den): # check domain
        gui_dict = {}
        # degree
        if check_degree(num) == 1:
            gui_dict["grado_num"] = 1
        elif check_degree(num) == 2:
            gui_dict["grado_num"] = 2
        else:
            return False
        if check_degree(den) == 1:
            gui_dict["grado_den"] = 1
        elif check_degree(den) == 2:
            gui_dict["grado_den"] = 2
        else:
            return False
        # solution
        num_sol = solve_equation(num)
        if num_sol:
            gui_dict["solution_num"] = num_sol
        else:
            return False
        den_sol = solve_equation(den)
        if den_sol:
            gui_dict["solution_den"] = den_sol
        else:
            return False
        # existance
        num_exist = get_existance(num)
        gui_dict["existance_num"] = num_exist
        den_exist = get_existance(den)
        gui_dict["existance_den"] = den_exist
        # sign
        gui_dict["sign_num"] = get_sign (num, get_all_solution(num, den))
        gui_dict["sign_den"] = get_sign (den, get_all_solution(num, den))
        gui_dict["sign_all"] = get_all_sign(num, den)
        return gui_dict
    else:
        return False