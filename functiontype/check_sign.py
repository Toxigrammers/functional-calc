####
# x^2 -3x > 0
# x1 = 0 | x2 = 3
# [-∞;0]V[3;+∞]
# [[-9999,0],[3,9999]]
####
# 2x -6 > 0
# x1 = 3
# [3;+∞]
# [3;9999]
from equationcontrols import equation_resolver

x1 = x2 = 0
parable_sign = '+'

def assign_value(equ):
    sol = solve_equation(equ)
    if check_degree(equ) == 1:
        x1 = sol[0]
    else:
        x1 = sol[0]
        x2 = sol[1]
        if equ[0] == '-':
            parable_sign = '-'

def first_degree_values():
    val = [x1,9999]
    return val

def second_degree_values():
    True

def get_existance(equ):
    assign_value(equ)
    if check_degree(equ) == 1:
        return first_degree_values()
    else:
        return second_degree_values()