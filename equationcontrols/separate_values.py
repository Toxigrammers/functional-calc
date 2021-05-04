def separate_first_degree(equ):
    split_equ = equ.split(' ')
    a = b = 0
    if len(split_equ) == 2:
        n1 = split_equ[0]
        n2 = split_equ[1]
        pos = n1.find('x')
        if pos == 0 or n1[pos - 1] == '+':  # +1 is implied
            a = 1
        elif n1[pos - 1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        b = int(n2)
    elif len(split_equ) == 1:
        n1 = split_equ[0]
        pos = n1.find('x')
        if pos == 0 or n1[pos - 1] == '+':  # +1 is implied
            a = 1
        elif n1[pos - 1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
    return a, b


def separate_second_degree(equ):
    split_equ = equ.split(' ')
    a = b = c = 0
    if len(split_equ) == 3:
        n1 = split_equ[0]  # x^2  a
        n2 = split_equ[1]  # x    b
        n3 = split_equ[2]  # c
        pos = n1.find('x^2')
        if pos == 0 or n1[pos - 1] == '+':  # +1 is implied
            a = 1
        elif n1[pos - 1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        pos = n2.find('x')
        if n2[pos - 1] == '+':
            b = 1
        elif n2[pos - 1] == '-':
            b = -1
        else:
            b = int(n2[:pos])
        c = int(n3)
    elif len(split_equ) == 2:
        n1 = split_equ[0]  # x^2  a
        pos = n1.find('x^2')
        if pos == 0 or n1[pos - 1] == '+':  # +1 is implied
            a = 1
        elif n1[pos - 1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        if 'x' in split_equ[1]:
            n2 = split_equ[1]  # x  b
            pos = n2.find('x')
            if n2[pos - 1] == '+':
                b = 1
            elif n2[pos - 1] == '-':
                b = -1
            else:
                b = int(n2[:pos])
        else:
            c = int(split_equ[1])
    elif len(split_equ) == 1:
        a = int(split_equ[0])
    return a, b, c
