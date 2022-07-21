import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def grafica_seno(frecuencia, f_muestreo, desfase, muestras, amplitud):
    n = np.arange(muestras)
    print("frecuencia = ", frecuencia)
    sn = amplitud * np.sin((2 * np.pi * frecuencia * n / f_muestreo) + desfase)
    return (sn + amplitud)/2


def grafica_triangular(frecuencia, f_muestreo, desfase, muestras, amplitud):
    triangulo_def = 0.5  # esto define q es triangulo
    n = np.arange(muestras)
    sn = amplitud * signal.sawtooth((2 * np.pi * frecuencia * n / f_muestreo) + desfase, triangulo_def)
    return (sn + amplitud)/2

def grafica_cuadrada(frecuencia, f_muestreo, desfase, muestras, amplitud):
    cuadrada_def = 0.5
    n = np.arange(muestras)
    sn = amplitud * signal.square((2 * np.pi * frecuencia * n / f_muestreo) + desfase, cuadrada_def)
    return (sn + amplitud)/2

# ejemplo 2
seno = grafica_seno(1000, 100000, 0, 1000, 1)
triangular = grafica_triangular(1000, 100000, 0, 1000, 1)
cuadrada = grafica_cuadrada(1000, 100000, 0, 1000, 1)

plt.title('EJEMPLO 2')
plt.plot(seno, label='seno')
plt.plot(triangular, label='triangular')
plt.plot(cuadrada, label='cuadrada')
plt.grid()
plt.legend()
plt.ylabel('Magnitud')
plt.show()

# ejemplo 2.1
frecuencia_sample = 1000
frecuencia = 0.1 * frecuencia_sample
seno = grafica_seno(frecuencia, frecuencia_sample, 0, 1000, 1)
frecuencia = 1.1 * frecuencia_sample
seno_2 = grafica_seno(frecuencia, frecuencia_sample, 0, 1000, 1)

plt.title('EJEMPLO 2.1')
plt.plot(seno,color='green', label='seno')
plt.plot(seno_2,color='red', label='seno 2')
plt.grid()
plt.legend()
plt.ylabel('Magnitud')
plt.show()

# ejemplo 2.2
frecuencia_sample = 1000
frecuencia = 0.49 * frecuencia_sample
seno = grafica_seno(frecuencia, frecuencia_sample, 0, 1000, 1)
frecuencia = 0.51 * frecuencia_sample
seno_2 = grafica_seno(frecuencia, frecuencia_sample, 0, 1000, 1)

plt.title('EJEMPLO 2.1')
plt.plot(seno,color='green', label='seno')
plt.plot(seno_2,color='red', label='seno 2')
plt.grid()
plt.legend()
plt.ylabel('Magnitud')
plt.show()
