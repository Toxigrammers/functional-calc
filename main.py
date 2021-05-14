from function_type.check_sign import print_existance
from equation_controls.equation_resolver import solve_equation, print_value
from function_type.fractional_rational import rational_function
# from gui.gui import start_gui

print("""
 /$$$$$$$$                          /$$    /$$                         /$$$$$$$                            /$$                           
| $$_____/                         | $$   |__/                        | $$__  $$                          | $$                           
| $$   /$$   /$$/$$$$$$$  /$$$$$$$/$$$$$$  /$$ /$$$$$$ /$$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$$ /$$$$$$| $$/$$    /$$/$$$$$$  /$$$$$$ 
| $$$$| $$  | $| $$__  $$/$$_____|_  $$_/ | $$/$$__  $| $$__  $$      | $$$$$$$//$$__  $$/$$_____//$$__  $| $|  $$  /$$/$$__  $$/$$__  $$
| $$__| $$  | $| $$  \ $| $$       | $$   | $| $$  \ $| $$  \ $$      | $$__  $| $$$$$$$|  $$$$$$| $$  \ $| $$\  $$/$$| $$$$$$$| $$  \__/
| $$  | $$  | $| $$  | $| $$       | $$ /$| $| $$  | $| $$  | $$      | $$  \ $| $$_____/\____  $| $$  | $| $$ \  $$$/| $$_____| $$      
| $$  |  $$$$$$| $$  | $|  $$$$$$$ |  $$$$| $|  $$$$$$| $$  | $$      | $$  | $|  $$$$$$$/$$$$$$$|  $$$$$$| $$  \  $/ |  $$$$$$| $$      
|__/   \______/|__/  |__/\_______/  \___/ |__/\______/|__/  |__/      |__/  |__/\_______|_______/ \______/|__/   \_/   \_______|__/   
-----------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                        
""" )
print("non siamo matematici ma abbiamo provato a fare un calcolatore di funzioni (potrebbe non funzionare con alcuni valori)")
print("Questo programma non funziona con la radice quadrata e equazioni maggiori di 2° grado")
while True:
    # gui = int(input("1: cli\t2: gui"))
    # if gui == 2:
    #     start_gui()
    print("\n\t0: uscita dal programma\n\t1: calcolo equazione\n\t2: calcolo equazione razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break
    if choice == 1:
        print("\nUsare lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        equ = input("Inserire equazione: ")
        sol = solve_equation(equ)
        if sol:
            print_value(equ)
            print("Esistenza equa
            zione:")
            print_existance(equ)
    if choice == 2:
        print("\nUsare lo spazio per separare i valori\nEsempio di equazione: -x^2 +3x -2")
        x1 = input("Inserire numeratore: ")
        x2 = input("Inserire il denominatore: ")
        rational_function(x1, x2)