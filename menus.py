import sys
import os
from time import sleep
from solver import solver_differentiation


def indent(n_spaces: int) -> str:
    return " " * n_spaces


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu_main():

    while True:

        clear_screen()
        print_menu_main()
        print("")

        option = int(input("? "))

        if option == 0:
            print("\nAdiós...\n")
            sleep(1)
            sys.exit(0)

        elif option == 1:

            menu_differenciation()

        elif option == 2:

           menu_integration()

        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def menu_differenciation():

    while True:
        clear_screen()
        print_menu_differenciation()
        print("")
        option = int(input("? "))

        if option == 0:
            break

        elif option >= 1 and option <= 24:
            solver_differentiation(option)
            sleep(999)
            
        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def menu_integration():

    while True:
        clear_screen()
        print_menu_integration()
        print("")
        option = int(input("? "))

        if option == 0:
            break

        elif option >= 1 and option <= 5:
            solver_integration(option)
            sleep(999)

        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def print_menu_main():
    print(f"{indent(2)}== Menu ==")
    print("")

    print("• 1. Diferenciación Numérica")
    print("• 2. Integración Numérica")
    
    print("• 0. Salir")


def print_menu_differenciation():

    print(f"{indent(2)}== Diferenciación Numérica ==")
    print("")

    print("• Fórmulas de diferencias finitas divididas hacia adelante:")
    print(f"{indent(2)}• Primera Derivada:")
    print(f"{indent(4)}• 1.  Error O(h)")
    print(f"{indent(4)}• 2.  Error O(h²)")
    print(f"{indent(2)}• Segunda Derivada:")
    print(f"{indent(4)}• 3.  Error O(h)")
    print(f"{indent(4)}• 4.  Error O(h²)")
    print(f"{indent(2)}• Tercera Derivada:")
    print(f"{indent(4)}• 5.  Error O(h)")
    print(f"{indent(4)}• 6.  Error O(h²)")
    print(f"{indent(2)}• Cuarta Derivada:")
    print(f"{indent(4)}• 7.  Error O(h)")
    print(f"{indent(4)}• 8.  Error O(h²)")

    print("• Fórmulas de diferencias finitas divididas hacia atrás:")
    print(f"{indent(2)}• Primera Derivada:")
    print(f"{indent(4)}• 9.  Error O(h)")
    print(f"{indent(4)}• 10. Error O(h²)")
    print(f"{indent(2)}• Segunda Derivada:")
    print(f"{indent(4)}• 11. Error O(h)")
    print(f"{indent(4)}• 12. Error O(h²)")
    print(f"{indent(2)}• Tercera Derivada:")
    print(f"{indent(4)}• 13. Error O(h)")
    print(f"{indent(4)}• 14. Error O(h²)")
    print(f"{indent(2)}• Cuarta Derivada:")
    print(f"{indent(4)}• 15. Error O(h)")
    print(f"{indent(4)}• 16. Error O(h²)")

    print("• Fórmulas de diferencias finitas divididas centradas:")
    print(f"{indent(2)}• Primera Derivada:")
    print(f"{indent(4)}• 17. Error O(h²)")
    print(f"{indent(4)}• 18. Error O(h⁴)")
    print(f"{indent(2)}• Segunda Derivada:")
    print(f"{indent(4)}• 19. Error O(h²)")
    print(f"{indent(4)}• 20. Error O(h⁴)")
    print(f"{indent(2)}• Tercera Derivada:")
    print(f"{indent(4)}• 21. Error O(h²)")
    print(f"{indent(4)}• 22. Error O(h⁴)")
    print(f"{indent(2)}• Cuarta Derivada:")
    print(f"{indent(4)}• 23. Error O(h²)")
    print(f"{indent(4)}• 24. Error O(h⁴)")

    print("• 0. Volver")


def print_menu_integration():

    print(f"{indent(2)}== Integración Numérica ==")
    print("")

    print("• 1. Regla del Trapecio")
    print("• 2. Regla del Trapecio de Aplicación Múltiple")
    print("• 3. Regla de Simpson 1/3")
    print("• 4. Regla de Simpson 1/3 de Aplicación Múltiple")
    print("• 5. Regla de Simpson 3/8")

    print("• 0. Volver")
