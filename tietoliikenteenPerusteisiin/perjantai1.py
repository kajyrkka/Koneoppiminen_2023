import numpy as np
# pip install numpy
import matplotlib.pyplot as plt
# pip install matplotlib

Fs = 100  # Näytetaajuus
Ts = 1/Fs # Näyteväli
t = np.arange(0,1,Ts)

# A*Cos(2*pi*f*t + vaihe)
A = 1
f = 3
vaihe = 0

realCos = A*np.cos(2*np.pi*f*t + vaihe)
realSin = A*np.sin(2*np.pi*f*t + vaihe)

# pyörivaä phasor signaali on muotoa
# ph1 = A*exp(j*(2*pi*f*t + vaihe))
j = complex(0,1)
positPhasor = (A/2) * np.exp(j*(2*np.pi*f*t + vaihe))
negatPhasor = (A/2) * np.exp(-j*(2*np.pi*f*t + vaihe))

plt.figure(1)
plt.subplot(3,2,1)
plt.plot(t,realCos),plt.title('realCos')

plt.subplot(3,2,2)
plt.plot(positPhasor.real,positPhasor.imag),plt.title('positPhasor')

plt.subplot(3,2,3)
plt.plot(t,positPhasor.real),plt.title('PositPhasor.real')
plt.subplot(3,2,4)
plt.plot(t,positPhasor.imag),plt.title('PositPhasor.imag')

plt.subplot(3,2,5)
plt.plot(t,negatPhasor.real),plt.title('NegatPhasor.real')
plt.subplot(3,2,6)
plt.plot(t,negatPhasor.imag),plt.title('NegatPhasor.imag')


plt.show()