#!/usr/bin/python3
from equationcontrols.equation_resolver import solve_equation
from functiontype.fractional_rational import rational_function

dom = [1, 2, [3, 2], [2]]
print("non siamo matematici ma abbiamo provato a fare un calcolatore di equazioni (potrebbe non funzionare con alcuni valori)")
print("Questo programma non funziona con la radice quadrata e equazioni maggiori di 2° grado")
print(dom[2][1])  # print 2
print(len(dom))   # print 4
while True:
    print("\n\t0: uscita dal programma\n\t1: calcolo equazione\n\t2: calcolo equazione razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break
    if choice == 1:
        print("\nNon usare spazi e usa lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        equ = input("Inserire equazione: ")
        sol = solve_equation(equ)
        if sol:
            if len(sol) == 1:  # 1° grado
                print("Il valore dell'equazione è:\nx = "+str(sol[0]))
            else:             # 2° grado
                print("I valori dell'equazione sono:\nx1 = {} \nx2 = {}".format(sol[0], sol[1]))
    if choice == 2:
        print("\nNon usare spazi e usa lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        x1 = input("Inserire numeratore: ")
        x2 = input("Inserire il denominatore: ")
        rational_function(x1, x2)
