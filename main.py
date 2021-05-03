from python.functionalcalc.equationcontrols.equationresolver import solveEquation
import functiontype
import equationcontrols

print("Questo programma non funziona con la radice quadrata e equazioni maggiori di 2° grado")
while True:
    print("\n\t0: uscita dal programma\n\t1: calcolo equazione\n\t2: calcolo equazione razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break
    if choice == 1:
        print("\nNon usare spazi e usa la virgola per separare i valori\nEsempio di equazione: -x^2,+3x,-2")
        equ = input("Inserire equazione: ")
        sol = solveEquation(equ)
        if sol != False:
            if len(sol) == 1: # 1° grado
                print("Il valore dell'equazione è:\nx = "+str(sol[0]))
            else:             # 2° grado
                print("I valori dell'equazione sono:\nx1 = {} \nx2 = {}".format(sol[0],sol[1]))
    if choice == 2:
        print("\nNon usare spazi e usa la virgola per separare i valori\nEsempio di equazione: -x^2,+3x,-2")
        x1 = input("Inserire numeratore: ")
        x2 = input("Inserire il denominatore: ")
        rationalFunction(x1, x2)
