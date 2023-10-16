from Graficadora import *
from funciones import *
from logos import *
from time import sleep
import os


def main():
    print(sep())
    print(logo1)
    print(f'Bienvenido a la graficadora de señales "BioSignal".')
    sleep(4)
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
                print('Ha seleccionado "señal fisiológica".')
                print(sep())
                sleep(4)
                num_graficas = verificarInt('''Seleccione una opción:
                1. Graficar una sola sola señal.
                2. Graficar todas las señales.
                3. Graficar varias señales.
                4. Ver espectro de frecuencias.
                > ''')
                if num_graficas == 1:  # Graficar una sola señal
                    inicio = verificarInt('Ingrese el valor mínimo del rango a graficar: ')
                    final = verificarInt('Ingrese el valor máximo del rango a graficar: ')
                    while True:
                        arreglo = verificarInt('Ingrese el número de arreglo a graficar: ')
                        if arreglo > 5 or arreglo < 1:
                            print('Seleccione uno de los 5 arreglos disponibles.')
                        else:
                            break
                    print(sep())
                    graficadora.graficar_uno(inicio, final, arreglo - 1)
                    print('''Gráfica generada.
                    La línea roja punteada representa el promedio de los datos.''')
                    presionaEnter()
                elif num_graficas == 2:  # Graficar todas las señales
                    inicio = verificarInt('Ingrese el valor mínimo del rango a graficar: ')
                    final = verificarInt('Ingrese el valor máximo del rango a graficar: ')
                    print(sep())
                    graficadora.graficar_todos(inicio, final)
                    print('Gráfica generada.')
                    presionaEnter()
                elif num_graficas == 3:  # Graficar varias señales
                    inicio = verificarInt('Ingrese el valor mínimo del rango a graficar: ')
                    final = verificarInt('Ingrese el valor máximo del rango a graficar: ')
                    print(sep())
                    while True:
                        arreglo = input('Ingrese los arreglos a graficar separados por comas: ')
                        arreglo = arreglo.split(',')
                        try:
                            arreglo = [int(i) - 1 for i in arreglo]
                            break
                        except ValueError:
                            print('Ingrese valores válidos.')
                    graficadora.graficar_varios(inicio, final, arreglo)
                    print('Gráfica generada.')
                    presionaEnter()
                elif num_graficas == 4:  # Ver espectro de frecuencias
                    inicio = verificarInt('Ingrese el valor mínimo del rango a graficar: ')
                    final = verificarInt('Ingrese el valor máximo del rango a graficar: ')
                    while True:
                        arreglo = verificarInt('Ingrese el número de arreglo a graficar: ')
                        if arreglo > 5 or arreglo < 1:
                            print('Seleccione uno de los 5 arreglos disponibles.')
                        else:
                            break
                    print(sep())
                    graficadora.graficar_espectro(inicio, final, arreglo - 1)
                    print('Gráfica generada.')
                    presionaEnter()
                else:
                    print('Seleccione una opción válida.')
            elif tipo == 2:  # Señal de EEG
                ruta = os.path.join(os.getcwd(), 'data', 'csv_file.csv')
                graficadora = Graficadora(ruta)
                print(sep())
                print('Ha seleccionado "señal de EEG".')
                print(sep())
                sleep(4)
                menu2 = verificarInt('''Seleccione una opción:
                1. Promedio de datos.
                2. Gráfica de puntos utilizando el promedio como eje X.
                3. Gráfica utilizando la longitud de la misma columna como eje X.
                4. Gráfica de los datos pares.
                5. Gráfica con función seno.
                > ''')





if __name__ == '__main__':
    main()
