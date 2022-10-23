import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


signal = np.fft.ifft(np.load('fft_hjs.npy')) 
senal_real = np.real(signal) 
senal_imag = np.imag(signal)
senal_fft = np.fft.fft(signal)
print(senal_fft)
N = len(signal)
fig = plt.figure()
plt.plot(senal_imag, senal_real, 'g-', linewidth = 2, alpha = 1)

fs = 50
ancho_banda = 15
frecuen_corte = int((fs - ancho_banda) / (fs / N))
t = np.arange(0, N / fs, 1 / fs)
nData = np.arange(0, N, 1)
fData = nData * (fs / N) - (fs / 2)
aux = np.abs(np.fft.fftshift(senal_fft) / N ** 2)
senal_fft[int(N / 2) - int(frecuen_corte / 2): int(N / 2)] = 0
senal_fft[int(N / 2): int(N / 2) + int(frecuen_corte / 2)] = 0

senal_real = np.real(np.fft.ifft(senal_fft))
senal_imag = np.imag(np.fft.ifft(senal_fft))
fig = plt.figure()
#--------------------------------
signalAxe = fig.add_subplot(3, 1, 1)
signalAxe.set_title("senal", rotation = 0, fontsize = 10, va = "center")
plt.plot(t, senal_real, 'b-', linewidth = 2, alpha = 1)
plt.plot(t, senal_imag, 'r-', linewidth = 2, alpha = 1)
plt.plot()

signalFFTAxe = fig.add_subplot(3, 1, 2)
signalFFTAxe.set_ylim(0, 0.0004)

signalFFTAxe.set_title("senal fft", rotation = 0, fontsize = 10, va = "center")
plt.plot(fData, np.abs(np.fft.fftshift(senal_fft) / N ** 2), 'b-', linewidth = 3,alpha = 1)
signalFFTAxe.fill_between([-ancho_banda / 2, ancho_banda / 2], 1, -1, facecolor = "red", alpha = 0.2)
plt.grid()
signalAxe = fig.add_subplot(3, 1, 3)
signalAxe.set_title("imagen", rotation = 0, fontsize = 10, va = "center")
plt.plot(senal_imag, senal_real, 'g-', linewidth = 2, alpha = 1)

plt.show()