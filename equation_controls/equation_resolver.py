import math
from equation_controls.separate_values import separate_second_degree, separate_first_degree

def check_if_sqrt(val):
    val = val*10
    string_val = str(val)
    if string_val[len(string_val)-1] != "0":
        return True
    else:
        return False

def print_value(equ):
    n = solve_equation(equ)
    if check_degree(equ) == 1:
        print("\nIl valore di x è " + str(n[0]))
    else:
        if n:
            if n[0] == n[1]:
                if check_if_sqrt(n[0]):
                    if n[0] < 0:
                        n_str = "-√" + str( round( pow(n[0], 2) ) )
                    else:
                        n_str = "√" + str( round( pow(n[0], 2) ) )
                    print("\nI valori di x1 e x2 sono " + str(n[0]) + " oppure " + n_str)
                else:
                    print("\nI valori di x1 e x2 sono " + str(n[0]))
            else:
                if check_if_sqrt(n[0]):
                    if n[0] < 0:
                        n1_str = "-√" + str( round( pow(n[0], 2) ) )
                    else:
                        n1_str = "√" + str( round( pow(n[0], 2) ) )
                else:
                    n1_str = n[0]
                if check_if_sqrt(n[1]):
                    if n[1] < 0:
                        n2_str = "-√" + str( round( pow(n[1], 2) ) )
                    else:
                        n2_str = "√" + str( round( pow(n[1], 2) ) )
                else:
                    n2_str = str(n[1])
                if check_if_sqrt(n[0]) and check_if_sqrt(n[1]):
                    print(f"\nIl valore di x1 è {n[0]} oppure {n1_str}\nIl valore di x2 è {n[1]} oppure {n2_str}")
                else:
                    print(f"\nIl valore di x1 è {n1_str}\nIl valore di x2 è {n2_str}")

def first_degree(equ):
    a, b = separate_first_degree(equ)
    x = (-b) / a
    n = [x]
    return n


def second_degree(equ):
    a, b, c = separate_second_degree(equ)
    if check_delta(a, b, c):  # CAMBIARE CALCOLO EQUAZIONE DI SECONDO GRADO (es. x^2 -3)
        x1, x2 = equation(a, b, c)
        n = [x1, x2]
        return n
    else:
        print("\nCalcolo impossibile")
        return False


def check_degree(equ):  # check equation degree
    if 'x^2' in equ:
        n = 2
    elif 'x' in equ:
        n = 1
    else:
        n = 0
    return n


def check_delta(a, b, c):  # check if delta is less than 0
    check = False
    delta = (b * b) - (4 * a * c)
    if delta >= 0:
        check = True
    return check


def equation(a, b, c):
    delta = (b * b) - (4 * a * c)
    delta = math.sqrt(delta)
    n1 = (-b + delta) / (2 * a)
    n2 = (-b - delta) / (2 * a)
    return n1, n2


def solve_equation(equ):
    if check_degree(equ) == 1:
        return first_degree(equ)
    elif check_degree(equ) == 2:
        return second_degree(equ)
