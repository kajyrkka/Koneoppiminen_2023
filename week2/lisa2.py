import numpy as np
import matplotlib.pyplot as plt
'''
Lisätehtävät, kun Courseran viikkojen 2 ja 3 tehtävät on suoritettu ja
kaikki Courseran viikkojen 2 ja 3 tentit läpäisty:

1. Tee kaksiuloitteinen Numpy array (kysy apua chat-GPT:ltä tai googlesta),
    missä on seuraavat alkiot
    1,2,3
    4,5,6
    7,8,8

2. Tee aliohjelma, joka ottaa parametrina tehtävässä 1 muodostetun arrayn
   ja palauttaa rivin 1 ja rivin 2 alkioiden erotuksen sekä rivin 2 ja rivin 3 erotuksen
   eli tuloksena tulee kaksirivinen Numpy taulukko, jonka alkiot ovat
   3,3,3
   3,3,3
    
'''
taulukko = np.array([[1,2,3],[4,5,6],[7,8,9]])

tulos = np.zeros((2,3))

#tulos[0][0:2] = taulukko[1][:] - taulukko[0][:]
#tulos[1][:] = taulukko[2][:] - taulukko[1][:]

for i in range(0,10,2):
    print(i)
    #tulos[i][:] = taulukko[i+1][:] - taulukko[i][:]

print(tulos)




'''
def erotus(t):
    print(t.size)
    print(t.shape)
    s = t.shape
    rivit = s[0]
    sarakkeet = s[1]
    tulos = np.zeros((rivit-1,sarakkeet))
    print(tulos)
    print(rivit)
    for I in range(1,rivit):
        #print(t[I][0:3]-t[I-1][0:3])
        tulos[I-1][0:3] = t[I][0:3]-t[I-1][0:3]
    return tulos

taulukko = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("tulos =", erotus(taulukko))

'''