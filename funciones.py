def verificarInt(texto):
    while True:
        try:
            num = int(input(texto))
            break
        except ValueError:
            print("Ingrese un número entero.\n")
    return num


def verificarFloat(texto):
    while True:
        try:
            num = float(input(texto))
            break
        except ValueError:
            print("Ingrese un número.\n")
    return num


def presionaEnter():
    input("Presione Enter para continuar...")


def sep():
    return "\n" + ("⬜" * 50) + "\n"
