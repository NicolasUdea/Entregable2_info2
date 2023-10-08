import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


class Graficadora:
    def __init__(self, path):
        self.__path = path
        self.__data = sp.io.loadmat(self.__path)

    def graficar(self, inicio, fin, arreglo):
        with plt.style.context('dark_background'):
            x = np.arange(inicio, fin)
            y = self.__data['val'][arreglo][inicio:fin]
            plt.plot(x, y)
            plt.xlabel('Tiempo (s)', fontsize=14, color='white', fontweight='bold')
            plt.ylabel('Amplitud (mV)', fontsize=14, color='white', fontweight='bold')
            plt.title('Señal fisiológica', fontsize=18, color='white', fontweight='bold')
            plt.show()
