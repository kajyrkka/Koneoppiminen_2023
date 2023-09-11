import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros((128),dtype=complex)
taajuustaso[3] = complex(1,1);  # Tässä on nyt moduloitu yksi alikantoaalto
taajuustaso[10] = complex(1,1)
taajuustaso[20] =complex(-1,-1)
# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
# Eli tarkoittaa siis sitä, että sinulla on käytettävissäsi 00 => 1+j, 11 => -1-j, 01 => -1+j ja 
# 10 => 1-j vaihtoehdot.



aikataso = np.fft.ifft(taajuustaso[:]);


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(aikataso.real)
plt.title('Moduloidun signaalin kosinihaara')
plt.subplot(2,1,2)
plt.plot(aikataso.imag)
plt.title('Moduloidun signaalin sinihaara')
plt.show()

print(np.fft.fft(aikataso))