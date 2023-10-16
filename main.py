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
                5. Salir.
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
                elif num_graficas == 5:  # Salir
                    print('Saliendo...')
                    sleep(2)
                    break
                else:
                    print('Seleccione una opción válida.')
            elif tipo == 2:  # Señal de EEG
                ruta = os.path.join(os.getcwd(), 'data', 'csv_data.csv')
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
                6. Salir.
                > ''')
                if menu2 == 1:  # Promedio de datos
                    print(sep())
                    print('Ha seleccionado "promedio de datos".')
                    print(sep())
                    sleep(4)
                    for i in range(len(graficadora.promedio_datos_csv())):
                        print(f'El promedio de la columna {i + 1} es: {graficadora.promedio_datos_csv()[i]}')
                    presionaEnter()
                elif menu2 == 2:  # Gráfica de puntos utilizando el promedio como eje X
                    print(sep())
                    print('Ha seleccionado "gráfica de puntos utilizando el promedio como eje X".')
                    print(sep())
                    sleep(4)
                    while True:
                        columna = verificarInt('Ingrese el número de columna a graficar: ')
                        if columna > 5 or columna < 1:
                            print('Seleccione una columna válida.')
                        else:
                            if columna == 1:
                                columna = 'Dato_1'
                            elif columna == 2:
                                columna = 'Dato_2'
                            elif columna == 3:
                                columna = 'Dato_3'
                            elif columna == 4:
                                columna = 'Dato_4'
                            elif columna == 5:
                                columna = 'Dato_5'
                            break
                    graficadora.graficar_puntos_promedio(columna)
                    print('Gráfica generada.')
                    presionaEnter()
                elif menu2 == 3:  # Gráfica utilizando la longitud de la misma columna como eje X
                    print(sep())
                    print('Ha seleccionado "gráfica utilizando la longitud de la misma columna como eje X".')
                    print(sep())
                    sleep(4)
                    while True:
                        columna = verificarInt('Ingrese el número de columna a graficar: ')
                        if columna > 5 or columna < 1:
                            print('Seleccione una columna válida.')
                        else:
                            if columna == 1:
                                columna = 'Dato_1'
                            elif columna == 2:
                                columna = 'Dato_2'
                            elif columna == 3:
                                columna = 'Dato_3'
                            elif columna == 4:
                                columna = 'Dato_4'
                            elif columna == 5:
                                columna = 'Dato_5'
                            break
                    graficadora.graficar_longitud(columna)
                    print('Gráfica generada.')
                    presionaEnter()
                elif menu2 == 4:  # Graficar únicamente los datos pares, los demás, definir como 0 en gráfica de puntos.
                    print(sep())
                    print('Ha seleccionado "gráfica de los datos pares".')
                    print(sep())
                    sleep(4)
                    while True:
                        columna = verificarInt('Ingrese el número de columna a graficar: ')
                        if columna > 5 or columna < 1:
                            print('Seleccione una columna válida.')
                        else:
                            if columna == 1:
                                columna = 'Dato_1'
                            elif columna == 2:
                                columna = 'Dato_2'
                            elif columna == 3:
                                columna = 'Dato_3'
                            elif columna == 4:
                                columna = 'Dato_4'
                            elif columna == 5:
                                columna = 'Dato_5'
                            break
                    graficadora.graficar_pares(columna)
                    print('Gráfica generada.')
                    presionaEnter()
                elif menu2 == 5:  # Gráfica con función seno
                    print(sep())
                    print('Ha seleccionado "gráfica con función seno".')
                    print(sep())
                    sleep(4)
                    while True:
                        columna = verificarInt('Ingrese el número de columna a graficar: ')
                        if columna > 5 or columna < 1:
                            print('Seleccione una columna válida.')
                        else:
                            if columna == 1:
                                columna = 'Dato_1'
                            elif columna == 2:
                                columna = 'Dato_2'
                            elif columna == 3:
                                columna = 'Dato_3'
                            elif columna == 4:
                                columna = 'Dato_4'
                            elif columna == 5:
                                columna = 'Dato_5'
                            break
                    graficadora.graficar_seno(columna)
                    print('Gráfica generada.')
                    presionaEnter()
                elif menu2 == 6:  # Salir
                    print('Saliendo...')
                    sleep(2)
                    break
                else:
                    print('Seleccione una opción válida.')
            else:
                print('Seleccione una opción válida.')
        elif menu == 2:  # Salir
            print('Saliendo...')
            sleep(2)
            print(logo2)
            break
        else:
            print('Seleccione una opción válida.')


if __name__ == '__main__':
    main()
