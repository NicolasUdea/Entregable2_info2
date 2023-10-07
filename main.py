import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import os

''' Se lee el archivo .mat dentro de la carpeta "data" utilizando scipy '''
path = os.path.join('data', 'r01_edfm.mat')
data = sp.io.loadmat(path)
# dict_keys(['__header__', '__version__', '__globals__', 'val'])

x = np.arange(1000)
y = data['val'][0][0:1000]

plt.plot(x, y)
plt.show()
