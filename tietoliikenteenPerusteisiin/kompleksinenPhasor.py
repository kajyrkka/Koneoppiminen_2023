import numpy as np
import matplotlib.pyplot as plt

# Tietoliikenteessä käytetään ns kompleksista phasor signaalia
# joka pitää sisällään cosini ja sini signaalit, joiden mukana
# tyypillisesti informaatiosignaali "kannetaan"


Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
A = 1
f = 4
phase = (np.pi)/4

j = complex(0,1)


phasor = np.exp(j*(2*np.pi*f*t+phase))
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(phasor.real,phasor.imag)
plt.subplot(3,1,2)
plt.plot(t,phasor.real)
plt.subplot(3,1,3)
plt.plot(t,phasor.imag)
plt.show()


