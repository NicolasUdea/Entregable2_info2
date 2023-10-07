import scipy.io
import matplotlib.pyplot as plt
import os


def leer_archivo(minimo, maximo, arreglo):
    # Cargar el archivo .mat
    path = os.path.join('data', 'r01_edfm.mat')
    mat = scipy.io.loadmat(path)

    # Extraer el arreglo especificado
    datos = mat[arreglo][minimo:maximo]

    return datos


def visualizar_datos(datos):
    # Crear una figura
    plt.figure()

    # Dibujar los datos
    plt.plot(datos)

    # Mostrar la figura
    plt.show()


minimo = int(input("Por favor ingrese el mínimo de datos a leer: "))
maximo = int(input("Por favor ingrese el máximo de datos a leer: "))
arreglo = input("Por favor ingrese el nombre del arreglo a leer: ")

datos = leer_archivo(minimo, maximo, arreglo)
visualizar_datos(datos)
