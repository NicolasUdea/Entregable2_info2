import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp


class Graficadora:
    def __init__(self, path):
        self.__path = path
        if self.__path.endswith('.csv'):
            self.__data = pd.read_csv(self.__path)
        elif self.__path.endswith('.mat'):
            self.__data = sp.io.loadmat(self.__path)

    def graficar_uno(self, inicio, fin, arreglo):
        with plt.style.context('dark_background'):
            x = np.arange(inicio, fin)
            y = self.__data['val'][arreglo][inicio:fin]
            plt.plot(x, y)
            plt.xlabel('Tiempo (s)', fontsize=14, color='white', fontweight='bold')
            plt.ylabel('Amplitud (mV)', fontsize=14, color='white', fontweight='bold')
            plt.title('Señal fisiológica (NVF-JJG)', fontsize=18, color='white', fontweight='bold')
            plt.axhline(y=self.__data['val'][arreglo].mean(), color='r', linestyle='--')
            plt.show()

    def graficar_todos(self, inicio, fin):
        with plt.style.context('dark_background'):
            x = np.arange(inicio, fin)
            for i in range(len(self.__data['val'])-1):
                y = self.__data['val'][i][inicio:fin]
                plt.plot(x, y + i * 1000)
            plt.xlabel('Tiempo (s)', fontsize=14, color='white', fontweight='bold')
            plt.ylabel('Amplitud (mV)', fontsize=14, color='white', fontweight='bold')
            plt.title('Señal fisiológica', fontsize=18, color='white', fontweight='bold')
            plt.legend(['S1', 'S2', 'S3', 'S4', 'S5'], loc='upper right', fontsize=12)
            plt.show()

    # Gráficar todos los arreglos que el usuario seleccione
    def graficar_varios(self, inicio, fin, arreglo):
        with plt.style.context('dark_background'):
            x = np.arange(inicio, fin)
            for i in arreglo:
                y = self.__data['val'][i][inicio:fin]
                plt.plot(x, y + i * 1000)
            plt.xlabel('Tiempo (s)', fontsize=14, color='white', fontweight='bold')
            plt.ylabel('Amplitud (mV)', fontsize=14, color='white', fontweight='bold')
            plt.title('Señal fisiológica', fontsize=18, color='white', fontweight='bold')
            plt.legend(['S1', 'S2', 'S3', 'S4', 'S5'], loc='upper right', fontsize=12)
            plt.show()


    def graficar_espectro(self, inicio, fin, arreglo):
        espectro = np.fft.fft(self.__data['val'][arreglo][inicio:fin])
        frecuencias = np.fft.fftfreq(len(espectro))
        frecuencias_pos = frecuencias[:len(frecuencias) // 2]
        amplitudes = np.abs(espectro) / len(espectro)
        with plt.style.context('dark_background'):
            plt.plot(frecuencias_pos, amplitudes[:len(amplitudes) // 2])
            plt.xlabel('Frecuencia (Hz)', fontsize=14, color='white', fontweight='bold')
            plt.ylabel('Amplitud (mV)', fontsize=14, color='white', fontweight='bold')
            plt.title('Espectro de frecuencias', fontsize=18, color='white', fontweight='bold')
            plt.show()

    def promedio_datos_csv(self):
        promedio = self.__data.mean()
        return promedio
