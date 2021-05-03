import functiontype
print("Questo programma non funziona con equazioni razionali e equazioni maggiori di 2° grado")
while True:
    print("\t0: uscita dal programma\n\t1: seleziona funzione di tipo razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break;
    if choice == 1:
        x1 = input("Inserire numeratore separa i valori dell'equazione con una virgola")
        x2 = input("Inserire il denominatore separa i valori dell'equazione con una virgola")
        rationalFunction(x1, x2)
