from equation_controls.equation_resolver import solve_equation, check_degree, check_if_sqrt

def print_existance(equ):
    val = get_existance(equ)
    if val == '+':
        print("All positive")
    elif val == '-':
        print("All negative")
    elif len(val) == 4:
        n1 = val[1]
        n2 = val[2]
        if check_if_sqrt(n1):
            if n1 < 0:
                n1_str = f"-√ {str( round( pow(n1, 2)))}"
            else:
                n1_str = f"√ {str( round( pow(n1, 2)))}"
        else:
            n1_str = str(n1)
        if check_if_sqrt(n2):
            if n2 < 0:
                n2_str = f"-√ + {str( round( pow(n2, 2)))}"
            else:
                n2_str = "√" + str( round( pow(n2, 2)))
        else:
            n2_str = str(n2)
        print(f"[-∞; {n1_str}] V [{n2_str}; +∞]")
    else:
        if check_degree(equ) == 1:
            if equ[0] == "-":
                print(f"[-∞; {val[1]}]")
            else:
                print(f"[{val[0]}; +∞]")
        else:
            sol = solve_equation(equ)
            if sol[0] == sol[1]:
                if equ[0] == "-":
                    n = val[1]
                    if check_if_sqrt(n):
                        if sol[0] < 0:
                            n_str = f"-√ {str( round( pow(n, 2)))}"
                        else:
                            n_str = f"√ {str( round( pow(n, 2)))}"
                    else:
                        n_str = str(n)
                    print(f"[-∞; {n_str}]")
                else:
                    n = val[0]
                    if check_if_sqrt(n):
                        if sol[0] < 0:
                            n_str = f"-√ {str( round( pow(n, 2)))}"
                        else:
                            n_str = f"√ {str( round( pow(n, 2)))}"
                    else:
                        n_str = str(n)
                    print(f"[{n_str}; +∞]")
            else:
                n1 = val[0]
                if check_if_sqrt(n1):
                    if n1 < 0:
                        n1_str = f"-√ + {str( round( pow(n1, 2)))}"
                    else:
                        n1_str = f"√ + {str( round( pow(n1, 2)))}"
                else:
                    n1_str = str(n1)
                n2 = val[1]
                if check_if_sqrt(n2):
                    if n2 < 0:
                        n2_str =  f"-√ + {str( round( pow(n2, 2)))}"
                    else:
                        n2_str =  f"√ + {str( round( pow(n2, 2)))}"
                else:
                    n2_str = str(n2)
                print(f"[{n1_str}; {n2_str}]")


def assign_value(equ):
    sol = solve_equation(equ)
    if check_degree(equ) == 1:
        return sol[0]
    else:
        parable_sign = '+'
        if equ[0] == '-':
            parable_sign = '-'
        if sol:
            return sol[0], sol[1], parable_sign
        else: 
            print("calcolo impossibile")


def first_degree_values(equ):
    x1 = assign_value(equ)
    if equ[0] == '-':
        val = [-9999, x1]  # [-∞; n]
    else:
        val = [x1, 9999]   # [n; +∞]
    return val


def second_degree_values(equ):
    x1, x2, parab = assign_value(equ)
    if x1 == x2:
        if equ[0] == '-':
            val = '-'  # tutto negativo
        else:
            val = '+'   # tutto positive
    else:
        if x1 > x2:
            if parab == '+':
                val = [-9999, x2, x1, 9999]  # [-∞; n2]V[n1; +∞]
            else:
                val = [x2, x1]               # [n2; n1]
        else:
            if parab == '+':
                val = [-9999, x1, x2, 9999]  # [-∞; n1]V[n2; +∞]
            else:
                val = [x1, x2]               # [n1; n2]
    return val


def get_existance(equ):
    if check_degree(equ) == 1:
        return first_degree_values(equ)
    else:
        return second_degree_values(equ)

def get_sign(equ, all):
    exist = get_existance(equ)
    sign = []
    if exist == '+':
        for i in range(len(all)+1):
            sign.append('+')
    elif exist == '-':
        for i in range(len(all)+1):
            sign.append('-')
    elif exist[1] == 9999:    # [x; +∞]
        pos = all.index(exist[0]) # find position of value in solution list
        for i in range(len(all)+1):
            if i <= pos: # if index is less than the value position append '-' else append '+'
                sign.append('-')
            else:       
                sign.append('+')
    elif exist[0] == -9999: # [-∞; x]
        pos = all.index(exist[1]) # find position of value in solution list
        for i in range(len(all)+1):
            if i <= pos: # if index is less than the value position append '+' else append '-'
                sign.append('+')
            else:
                sign.append('-')
    elif len(exist) == 4: # [-∞; x1]V[x2;+∞]
        pos1 = all.index(exist[1]) # find positions of values in solution list
        pos2 = all.index(exist[2])
        for i in range(len(all)+1):
            if i <= pos1 or i > pos2: # if index is not between the two values position append '+' else append '-'
                sign.append('+')
            else:
                sign.append('-')
    else:               # [x1;x2]
        pos1 = all.index(exist[0]) # find positions of values in solution list
        pos2 = all.index(exist[1])
        for i in range(len(all)+1):
            if i > pos1 and i <= pos2: # if index is between the two values position append '+' else append '-'
                sign.append('+')
            else:
                sign.append('-')
    return sign

def check_sign(sign1, sign2):
    sign = []
    for i in range(len(sign1)):
        if sign1[i] == '+' and sign2[i] == '-' or sign1[i] == '-' and sign2[i] == '+': # if signs are '-' and '+' gives '-'
            sign.append('-')
        elif sign1[i] == '+' and sign2[i] == '+': # if signs are both positive gives '+'
            sign.append('+')
        elif sign1[i] == '-' and sign2[i] == '-': # if signs are both negative gives '+'
            sign.append('+')
    return sign


def print_sign(num, den):
    num_exist = get_existance(num)
    den_exist = get_existance(den)
    num_sol = solve_equation(num)
    den_sol = solve_equation(den)
    all_sol = []
    if check_degree(num) == 2:
        if num_sol[0] == num_sol[1]:
            num_sol.pop(0)
    if check_degree(den) == 2:
        if den_sol[0] == den_sol[1]:
            den_sol.pop(0)
    for i in num_sol:
        all_sol.append(i)
    for i in den_sol:
        all_sol.append(i)
    all_sol.sort()   # sort all values
    num_sign = get_sign(num, all_sol)
    den_sign = get_sign(den, all_sol)
    all_sign = check_sign(num_sign, den_sign)
    print("\nSegno numeratore:")
    print(num_sign)
    print("\nSegno denominatore:")
    print(den_sign)
    print("\nSegni equazione: ")
    print(all_sign)