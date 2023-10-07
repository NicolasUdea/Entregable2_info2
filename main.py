import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import os

''' Se lee el archivo .mat dentro de la carpeta "data" utilizando scipy '''
path = os.path.join('data', 'r01_edfm.mat')
data = sp.io.loadmat(path)
# dict_keys(['__header__', '__version__', '__globals__', 'val'])

ARRAY = data['val']

print(f'''Información del archivo .mat:
    - Tipo de dato: {type(ARRAY)}
    - Dimensiones: {ARRAY.shape}
    - Tamaño: {ARRAY.size}
    - Tipo de dato de los elementos: {ARRAY.dtype}''')

''' El usuario elige la cantidad mínima y máxima de datos que se leerán '''
min = int(input('Ingrese la cantidad mínima de datos que desea leer: '))
max = int(input('Ingrese la cantidad máxima de datos que desea leer: '))

''' El usuario elige el tipo de arreglo quiere visualizar '''
print('''
    1. Arreglo de 1D
    2. Arreglo de 2D
    3. Arreglo de 3D
    4. Arreglo de 4D
    5. Arreglo de 5D
    