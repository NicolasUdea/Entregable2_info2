import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import os

class Graficadora():
    def __init__(self, path):
        self.__path = path
        self.__data = sp.io.loadmat(self.__path)


    def graficar(self, inicio, fin, arreglo):
        x = np.arange(inicio, fin)
        y = self.__data['val'][arreglo][inicio:fin]
        plt.plot(x, y)
        plt.show()

a = Graficadora(os.path.join('data', 'r01_edfm.mat'))
a.graficar(0, 1000, 0)

