from Graficadora import *
from funciones import *
from logos import *
import os


def main():
    print(sep())
    print(logo1)
    print(f'Bienvenido a la graficadora de señales.')
    while True:
        print(sep())
        menu = verificarInt('''Seleccione una opción:
        1. Graficar señal
        2. Salir
        > ''')
        print(sep())
        if menu == 1:  # Graficar señal
            tipo = verificarInt('''Seleccione el tipo de señal:
            1. Señal fisiológica (archivo .mat)
            2. Señal de EEG (archivo .csv)
            > ''')
            if tipo == 1:  # Señal fisiológica
                ruta = os.path.join(os.getcwd(), 'data', 'r01_edfm.mat')
                graficadora = Graficadora(ruta)
                print(sep())
                print('Ha seleccionado graficar una señal fisiológica.')
                print(sep())
                min = verificarInt('Ingrese el valor mínimo del rango a graficar: ')
                max = verificarInt('Ingrese el valor máximo del rango a graficar: ')
                arreglo = verificarInt('Ingrese el número de arreglo a graficar: ')
                print(sep())
                graficadora.graficar(min, max, arreglo-1)
                print('Gráfica generada.')
                presionaEnter()


if __name__ == '__main__':
    main()
