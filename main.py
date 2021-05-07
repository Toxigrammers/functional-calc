from functiontype.check_sign import print_existance
from functiontype.fractional_rational import rational_function

print("""
 /$$$$$$$$                          /$$    /$$                         /$$$$$$$                            /$$                           
| $$_____/                         | $$   |__/                        | $$__  $$                          | $$                           
| $$   /$$   /$$/$$$$$$$  /$$$$$$$/$$$$$$  /$$ /$$$$$$ /$$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$$ /$$$$$$| $$/$$    /$$/$$$$$$  /$$$$$$ 
| $$$$| $$  | $| $$__  $$/$$_____|_  $$_/ | $$/$$__  $| $$__  $$      | $$$$$$$//$$__  $$/$$_____//$$__  $| $|  $$  /$$/$$__  $$/$$__  $$
| $$__| $$  | $| $$  \ $| $$       | $$   | $| $$  \ $| $$  \ $$      | $$__  $| $$$$$$$|  $$$$$$| $$  \ $| $$\  $$/$$| $$$$$$$| $$  \__/
| $$  | $$  | $| $$  | $| $$       | $$ /$| $| $$  | $| $$  | $$      | $$  \ $| $$_____/\____  $| $$  | $| $$ \  $$$/| $$_____| $$      
| $$  |  $$$$$$| $$  | $|  $$$$$$$ |  $$$$| $|  $$$$$$| $$  | $$      | $$  | $|  $$$$$$$/$$$$$$$|  $$$$$$| $$  \  $/ |  $$$$$$| $$      
|__/   \______/|__/  |__/\_______/  \___/ |__/\______/|__/  |__/      |__/  |__/\_______|_______/ \______/|__/   \_/   \_______|__/                                                                                                                                           
""" )
print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
print("non siamo matematici ma abbiamo provato a fare un calcolatore di funzioni (potrebbe non funzionare con alcuni valori)")
print("Questo programma non funziona con la radice quadrata e equazioni maggiori di 2° grado")
while True:
    print("\n\t0: uscita dal programma\n\t1: calcolo equazione\n\t2: calcolo equazione razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break
    if choice == 1:
        print("\nUsare lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        equ = input("Inserire equazione: ")
        sol = solve_equation(equ)
        if sol:
            if len(sol) == 1:  # 1° grado
                print("Il valore dell'equazione è:\nx = "+str(sol[0]))
                print("Valori esistenza:")
                print_existance(equ)
            else:             # 2° grado
                print("I valori dell'equazione sono:\nx1 = {} \nx2 = {}".format(sol[0], sol[1]))
                # DA MIGLIORARE RISOLUZIONE DI EQUAZIONI COME x^2 -3
            print("Esistenza equazione:")
            print_existance(equ)
    if choice == 2:
        print("\nUsare lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        x1 = input("Inserire numeratore: ")
        x2 = input("Inserire il denominatore: ")
        rational_function(x1, x2)
        # DA SISTEMARE CALCOLO NUM = x-1, DEN = x^2 -4x +4