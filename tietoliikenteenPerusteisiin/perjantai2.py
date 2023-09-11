import numpy as np
import matplotlib.pyplot as plt

Fs = 100  # Näytetaajuus
Ts = 1/Fs # Näyteväli
t = np.arange(0,1,Ts)
A = 1
f = 2
vaihe = (np.pi)/2

j = complex(0,1)
Phasor = A * np.exp(j*(2*np.pi*f*t ))
kertoja = A * np.exp(-j*(2*np.pi*5*t + vaihe))
vaiheKertoja = A * np.exp(j*(vaihe))
print("vaiheKertojan arvo = ",vaiheKertoja)
tulo = Phasor*kertoja
tuloVaihekorjattu = Phasor*vaiheKertoja

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,Phasor.real),plt.title('cos osa')

plt.subplot(2,1,2)
plt.plot(t,tuloVaihekorjattu.real),plt.title('vaihekorjattu')

plt.show()