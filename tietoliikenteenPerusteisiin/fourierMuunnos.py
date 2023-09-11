import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)

sig = 10*np.cos(2*np.pi*20*t)

taajuustaso = np.fft.fft(sig)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(sig)
plt.subplot(2,1,2)
plt.show())
plt.show()