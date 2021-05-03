####### second degree
# 1) -3x^2,+2x,-3
# 2) -3x^2,+2x
# 3) -3x^2,-3
# 4) -3x^2
####### first degree
# 1) +2x,-3
# 2) +2x

def separateFirstDegree(equ):
    split_equ = equ.split(',')
    for i in range(len(split_equ)):
        print(split_equ[i], end="\n")
    a = b = 0
    if(len(split_equ) == 2):
        n1 = split_equ[0]
        n2 = split_equ[1]
        pos = n1.find('x')
        if(pos == 0):  # +1 is implied
            a = 1
        elif(n1[pos-1] == '-'):  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        b = int(n2)
    elif(len(split_equ) == 1):
        n1 = split_equ[0]
        pos = n1.find('x')
        if(pos == 0):  # +1 is implied
            a = 1
        elif(n1[pos-1] == '-'):  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
    return a,b

def separateSecondDegree(equ):
    split_equ = equ.split(',')
    for i in range(len(split_equ)):
        print(split_equ[i], end="\n")
    a = b = c = 0
    if(len(split_equ) == 3):
        n1 = split_equ[0]  # x^2  a
        n2 = split_equ[1]  # x    b
        n3 = split_equ[2]  #      c
        pos = n1.find('x^2')
        if(pos == 0):  # +1 is implied
            a = 1
        elif(n1[pos-1] == '-'): # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        pos = n2.find('x')
        if(pos == 0):
            b = 1
        elif(n2[pos-1] == '-'):
            b = -1
        else:
            b = int(n2[:pos])
        c = int(n3)
    elif(len(split_equ) == 2):
        n1 = split_equ[0]  # x^2  a
        pos = n1.find('x^2')
        if(pos == 0):  # +1 is implied
            a = 1
        elif(n1[pos-1] == '-'): # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        if(split_equ[1].contains('x')):
            n2 = split_equ[1]  # x  b
            pos = n2.find('x')
            if(pos == 0):
                b = 1
            elif(n2[pos-1] == '-'):
                b = -1
            else:
                b = int(n2[:pos])
        else:
            c = int(split_equ[1])
    elif(len(split_equ) == 1):
        a = int(split_equ[0])
    return a,b,c

str = input("eqauzione 1° o 2° grado? ")
n = input("Inserire equazione: ")
if(str == "2"):
    a,b,c = separateSecondDegree(n)
    print("a = {}, b = {}, c = {}".format(a,b,c))
elif(str == "1"):
    a,b = separateFirstDegree(n)
    print("a = {}, b = {}".format(a,b))
else:
    print("Equazione non di 1° o 2° grado")