import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
'''
Graﬁque las siguientes señales lado a lado con su respectivo espectro en frecuencias:  
1) Senoidal. 
2) Cuadrada. 
3) Triangular 
4) Delta en t=0. 
Indicando en cada caso los siguientes parámetros (si corresponde) : 
1) Frecuencia. B) Amplitud. C) Potencia promedio. D) Fs. E) N. 5) 
Pegue el link a un pdf con los códigos, gráficos y comentarios.
'''

N = 200
fs = 200
f0 = 25
fase = 1.58
amp = 3

td = np.linspace(0, N, N, endpoint=False)/fs
#y = amp * np.sin((2 * np.pi * f0 * td) + fase) #senoidal
#y = amp * sc.square(2 * np.pi * f0 * td)#cuadrada
#y = amp * sc.sawtooth(2 * np.pi * f0 * td, width=0.5) #triangular

y = np.zeros((N, )) #delta
y[0] = 1#delta

freq = np.linspace(0, N, N, endpoint=False)
fft = np.abs(1/N * np.fft.fft(y))**2
plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.plot(td, y)
plt.subplot(1, 2, 2)
plt.plot(freq, fft)
plt.show()