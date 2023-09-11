import numpy as np
import matplotlib.pyplot as plt

# Tehdään ensin reaaliarvoinen 2 Hz kosinisignaali
# Määritellään näytetaajuudeksi 100 Hz eli ehditään ottaa 50 näytettä yhdestä cos jaksosta.

Fs = 100
Ts = 1/Fs               # Näyteväli on siis 0.01 sekunttia
t = np.arange(0,1,Ts)   # 0,0.01,0.02,...,0.99 eli 100 kpl näytehetkiä 1 sekunnin ajalta.

realCos = np.cos(2*np.pi*2*t)

# Tehdään kelloa vastaan pyörivä ja kellon suuntaan pyörivat phasor signaalit
# Ja yritetään todistaa, että nämä summaamalla saadaan realCos
j = complex(0,1)
phasor1 = 0.5*np.exp(j*2*np.pi*2*t)
phasor2 = 0.5*np.exp(-j*2*np.pi*2*t)

summa = phasor1.real + phasor2.real
haipyva = phasor1.imag + phasor2.imag


plt.figure(1)
plt.subplot(4,1,1)
plt.plot(t,realCos,'-r')
plt.subplot(4,1,2)
plt.plot(t,phasor1.real,'-b'), plt.title('phasor 1 real part')

plt.subplot(4,1,3)
plt.plot(t,phasor2.real,'-b'), plt.title('phasor 2 real part')

plt.subplot(4,1,4)
plt.plot(t,summa,'-b'), plt.title('phasor 1 real part + phasor 2 real part')


plt.figure(2)
plt.subplot(4,1,1)
plt.plot(t,realCos,'-r')
plt.subplot(4,1,2)
plt.plot(t,phasor1.imag,'-b'), plt.title('phasor 1 imag part')

plt.subplot(4,1,3)
plt.plot(t,phasor2.imag,'-b'), plt.title('phasor 2 imag part')

plt.subplot(4,1,4)
plt.plot(t,haipyva,'-b'), plt.title('phasor 1 imag part + phasor 2 imag part')

plt.show()