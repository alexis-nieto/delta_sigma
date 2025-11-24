import sys
import os
from time import sleep


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():

    #'''
    selection = {
        "category": str,
        "subcategory": int,
    }
    #'''

    while True:

        clear_screen()
        print_menu_main()
        print("")
        option = int(input("? "))

        if option == 1:

            selection["category"] = "diferenciacion"

            while True:
                clear_screen()
                print_menu_1()
                print("")
                option = int(input("? "))

                if option == 0:
                    break
                elif option >= 1 and option <= 24:
                    selection["subcategory"] = option
                    return selection
                else:
                    print("\nOpcion no valida, intente de nuevo...\n")
                    sleep(1)

        elif option == 2:

            selection["category"] = "integracion"

            while True:
                clear_screen()
                print_menu_2()
                print("")
                option = int(input("? "))

                if option == 0:
                    break
                elif option >= 1 and option <= 5:
                    selection["subcategory"] = option
                    return selection
                else:
                    print("\nOpcion no valida, intente de nuevo...\n")
                    sleep(1)

        elif option == 0:
            print("\nAdios\n")
            sys.exit(0)

        else:
            print("\nOpcion no valida, intente de nuevo...\n")
            sleep(1)



def print_menu_main():
    print("\t== Menu ==")
    print("")

    print("• 1. Diferenciacion Numerica")
    print("• 2. Integracion Numerica")
    
    print("• 0. Salir")


def print_menu_1():

    print("\t== Diferenciacion Numerica ==")
    print("")

    print("• Fórmulas de diferencias finitas divididas hacia adelante:")
    print("\t• Primera Derivada:")
    print("\t\t• 1.  Error O(h)")
    print("\t\t• 2.  Error O(h²)")
    print("\t• Segunda Derivada:")
    print("\t\t• 3.  Error O(h)")
    print("\t\t• 4.  Error O(h²)")
    print("\t• Tercera Derivada:")
    print("\t\t• 5.  Error O(h)")
    print("\t\t• 6.  Error O(h²)")
    print("\t• Cuarta Derivada:")
    print("\t\t• 7.  Error O(h)")
    print("\t\t• 8.  Error O(h²)")

    print("• Fórmulas de diferencias finitas divididas hacia atrás:")
    print("\t• Primera Derivada:")
    print("\t\t• 9.  Error O(h)")
    print("\t\t• 10. Error O(h²)")
    print("\t• Segunda Derivada:")
    print("\t\t• 11. Error O(h)")
    print("\t\t• 12. Error O(h²)")
    print("\t• Tercera Derivada:")
    print("\t\t• 13. Error O(h)")
    print("\t\t• 14. Error O(h²)")
    print("\t• Cuarta Derivada:")
    print("\t\t• 15. Error O(h)")
    print("\t\t• 16. Error O(h²)")

    print("• Fórmulas de diferencias finitas divididas centradas:")
    print("\t• Primera Derivada:")
    print("\t\t• 17. Error O(h²)")
    print("\t\t• 18. Error O(h⁴)")
    print("\t• Segunda Derivada:")
    print("\t\t• 19. Error O(h²)")
    print("\t\t• 20. Error O(h⁴)")
    print("\t• Tercera Derivada:")
    print("\t\t• 21. Error O(h²)")
    print("\t\t• 22. Error O(h⁴)")
    print("\t• Cuarta Derivada:")
    print("\t\t• 23. Error O(h²)")
    print("\t\t• 24. Error O(h⁴)")

    print("• 0. Volver")


def print_menu_2():

    print("\t== Integracion Numerica ==")
    print("")

    print("• 1. Regla del Trapecio")
    print("• 2. Regla del Trapecio de Aplicacion Multiple")
    print("• 3. Regla de Simpson 1/3")
    print("• 4. Regla de Simpson 1/3 de Aplicacion Multiple")
    print("• 5. Regla de Simpson 3/8")

    print("• 0. Volver")
