def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nEntrada inválida. Por favor ingrese un número entero.\n")


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nEntrada inválida. Por favor ingrese un número.\n")
