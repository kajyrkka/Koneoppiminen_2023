import numpy as np
import matplotlib.pyplot as plt

#  Testataan pitääkö paikkansa, että sakarapulssi on summa siniaalloista.

def sakara(Fs,lkm):
    Ts = 1/Fs
    t = np.arange(0,5,Ts)
    summa = np.zeros(len(t))
    for i in range(1,lkm+1):
        #print(i)
        summa = summa + (1/(2*i-1))*np.sin(2*np.pi*(2*i-1)*t)
    return t,summa



if __name__ == '__main__':
    t,tulos = sakara(1000,30)
    plt.figure(1)
    plt.plot(t,tulos)
    plt.show()





