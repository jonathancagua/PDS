import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

muestra = [ 0.00000000e+00, 9.98458667e-01,-7.82172325e-02,-9.86184960e-01,
  1.54508497e-01, 9.61939766e-01,-2.26995250e-01,-9.26320082e-01,
  2.93892626e-01, 8.80202983e-01,-3.53553391e-01,-8.24724024e-01,
  4.04508497e-01, 7.61249282e-01,-4.45503262e-01,-6.91341716e-01,
  4.75528258e-01, 6.16722682e-01,-4.93844170e-01,-5.39229548e-01,
  5.00000000e-01, 4.60770452e-01,-4.93844170e-01,-3.83277318e-01,
  4.75528258e-01, 3.08658284e-01,-4.45503262e-01,-2.38750718e-01,
  4.04508497e-01, 1.75275976e-01,-3.53553391e-01,-1.19797017e-01,
  2.93892626e-01, 7.36799178e-02,-2.26995250e-01,-3.80602337e-02,
  1.54508497e-01, 1.38150398e-02,-7.82172325e-02,-1.54133313e-03,
  1.83758918e-15, 1.54133313e-03, 7.82172325e-02,-1.38150398e-02,
 -1.54508497e-01, 3.80602337e-02, 2.26995250e-01,-7.36799178e-02,
 -2.93892626e-01, 1.19797017e-01, 3.53553391e-01,-1.75275976e-01,
 -4.04508497e-01, 2.38750718e-01, 4.45503262e-01,-3.08658284e-01,
 -4.75528258e-01, 3.83277318e-01, 4.93844170e-01,-4.60770452e-01,
 -5.00000000e-01, 5.39229548e-01, 4.93844170e-01,-6.16722682e-01,
 -4.75528258e-01, 6.91341716e-01, 4.45503262e-01,-7.61249282e-01,
 -4.04508497e-01, 8.24724024e-01, 3.53553391e-01,-8.80202983e-01,
 -2.93892626e-01, 9.26320082e-01, 2.26995250e-01,-9.61939766e-01,
 -1.54508497e-01, 9.86184960e-01, 7.82172325e-02,-9.98458667e-01,
  5.63708916e-15, 9.98458667e-01,-7.82172325e-02,-9.86184960e-01,
  1.54508497e-01, 9.61939766e-01,-2.26995250e-01,-9.26320082e-01,
  2.93892626e-01, 8.80202983e-01,-3.53553391e-01,-8.24724024e-01,
  4.04508497e-01, 7.61249282e-01,-4.45503262e-01,-6.91341716e-01,
  4.75528258e-01, 6.16722682e-01,-4.93844170e-01,-5.39229548e-01]

len_sample = len(muestra)
print(muestra)
fs = 200
#N = len_sample
#M = len_sample
freq_res_es = fs/len_sample
print(f'muestras {len_sample}')
print(f'1) Resolución espectral {freq_res_es} hz')


t = np.arange(0, len_sample / fs, 1 / fs)
nData = np.arange(0, len_sample, 1)
fData = nData * (fs / len_sample) - (fs / 2)
fig = plt.figure()

# sin zero padding
muestraFFT = np.abs(np.fft.fftshift(np.fft.fft(muestra)) / len_sample ** 2)
signalAxe = fig.add_subplot(2, 1, 1)
plt.plot(t, muestra, 'g-o', linewidth = 1, alpha = 1, label = "muestra")
plt.grid()
plt.title('muestra sin zero padding')
signalFFTAxe = fig.add_subplot(2, 1, 2)
signalFFTAxe.set_xlim(-fs / 2, (fs / 2) - (fs / len_sample))
plt.plot(fData, muestraFFT)
plt.grid()
plt.title('FFT(muestra) sin zero padding')
plt.show()

# With zero padding

t = np.arange(0, (len_sample * 2 ) / fs, 1 / fs)
nData = np.arange(0, len_sample * 2, 1)
fData = nData * (fs / (len_sample * 2)) - (fs / 2)
signalZeroAxe = fig.add_subplot(2, 1, 1)
muestra = np.pad(muestra, (0, len_sample))
muestraFFT = np.abs(np.fft.fftshift(np.fft.fft(muestra)) / len_sample ** 2)
plt.plot(t, muestra, 'g-o', linewidth = 1, alpha = 1, label = "muestra")
plt.grid()
plt.title('muestra con zero padding')
signalZeroFFTAxe = fig.add_subplot(2, 1, 2)
signalZeroFFTAxe.set_xlim(-fs / 2, (fs / 2) - (fs / len_sample))
plt.plot(fData, muestraFFT)
plt.grid()
plt.title('FFT(muestra) con zero padding')

plt.show()
