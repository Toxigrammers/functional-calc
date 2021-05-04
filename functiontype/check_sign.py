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
from equationcontrols.equation_resolver import solve_equation, check_degree


def print_existance(equ):
    val = get_existance(equ)
    if len(val) == 4:
        print('[-∞; {}] V [{}; +∞]'.format(val[1], val[2]))
    else:
        if check_degree(equ) == 1:
            print('[{}; +∞]'.format(val[0]))
        else:
            print('[{}; {}]'.format(val[0], val[1]))


def assign_value(equ):
    sol = solve_equation(equ)
    if check_degree(equ) == 1:
        return sol[0]
    else:
        parable_sign = '+'
        if equ[0] == '-':
            parable_sign = '-'
        return sol[0], sol[1], parable_sign


def first_degree_values(equ):
    x1 = assign_value(equ)
    val = [x1, 9999]
    return val


def second_degree_values(equ):
    x1, x2, parab = assign_value(equ)
    if x1 > x2:
        if parab == '+':
            val = [-9999, x2, x1, 9999]
        else:
            val = [x2, x1]
    else:
        if parab == '+':
            val = [-9999, x1, x2, 9999]
        else:
            val = [x1, x2]
    return val


def get_existance(equ):
    if check_degree(equ) == 1:
        return first_degree_values(equ)
    else:
        return second_degree_values(equ)


def check_sign(sign1, sign2):
    True


def print_sign(num, den):
    num_exist = get_existance(num)
    den_exist = get_existance(den)
