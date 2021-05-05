from equationcontrols.equation_resolver import solve_equation, check_degree


def print_existance(equ):
    val = get_existance(equ)
    if len(val) == 4:
        print('[-∞; {}] V [{}; +∞]'.format(val[1], val[2]))
    else:
        if check_degree(equ) == 1:
            if equ[0] == '-':
                print('[-∞; {}]'.format(val[0]))
            else:
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
    if equ[0] == '-':
        val = [-9999, x1]
    else:
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

def get_sign(equ, all):
    if check_degree(equ) == 1:
        exist = get_existance(equ)
        if exist[1] == 9999:    # [x; +∞]
            pos = all.index(exist[0])
            sign = []
            for i in range(len(all)+1):
                if i <= pos:
                    sign.append('-')
                else:
                    sign.append('+')
        elif exist[0] == -9999: # [-∞; x]
            pos = all.index(exist[1])
            sign = []
            for i in range(len(all)+1):
                if i <= pos:
                    sign.append('+')
                else:
                    sign.append('-')
        return sign
    else:
        exist = get_existance(equ)
        sign = []
        if len(exist) == 4: # [-∞; x1]V[x2;+∞]
            pos1 = all.index(exist[1])
            pos2 = all.index(exist[2])
            for i in range(len(all)+1):
                if i <= pos1 or i > pos2:
                    sign.append('+')
                else:
                    sign.append('-')
        else:               # [x1;x2]
            pos1 = all.index(exist[0])
            pos2 = all.index(exist[1])
            for i in range(len(all)+1):
                if i > pos1 and i <= pos2:
                    sign.append('+')
                else:
                    sign.append('-')
        return sign

def check_sign(sign1, sign2):
    sign = []
    for i in range(len(sign1)):
        if sign1[i] == '+' and sign2[i] == '-' or sign1[i] == '-' and sign2[i] == '+':
            sign.append('-')
        elif sign1[i] == '+' and sign2[i] == '+':
            sign.append('+')
        elif sign1[i] == '-' and sign2[i] == '-':
            sign.append('+')
    return sign


def print_sign(num, den):
    num_exist = get_existance(num)
    den_exist = get_existance(den)
    num_sol = solve_equation(num)
    den_sol = solve_equation(den)
    all_sol = []
    for i in num_sol:
        all_sol.append(i)
    for i in den_sol:
        all_sol.append(i)
    all_sol.sort()
    num_sign = get_sign(num, all_sol)
    den_sign = get_sign(den, all_sol)
    all_sign = check_sign(num_sign, den_sign)
    # print("   ")
    # for i in all_sol:
    #     print(str(i)+" ", end="")
    # print("  ")
    # for i in range(len(all_sign)):
    #     print("-+", end="")
    # print("-\nN ", end="")
    # for i in range(len(num_sign)):
    #     if i <= len(num_sign)-1:
    #         print(str(num_sign[i])+"|", end="")
    #     else:
    #         print(num_sign[i], end="")
    # print("   ")
    # for i in range(len(all_sign)):
    #     print("| ", end="")
    # print("\nD ", end="")
    # for i in range(len(den_sign)):
    #     if i <= len(den_sign)-1:
    #         print(str(den_sign[i])+"|", end="")
    #     else:
    #         print(den_sign[i], end="")
    # print("\n ")
    # for i in all_sign:
    #     print(" "+str(i), end="")
    # print()
    print("\nSegno numeratore:")
    print(num_sign)
    print("\nSegno denominatore:")
    print(den_sign)
    print("Segni equazione: ")
    print(all_sign)