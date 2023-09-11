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

3. 3D-avaruudessa kahden pisteen välinen etäisyys lasketaan seuraavasti
   etäisyys = sqrt( (x1-x2)^2  + (y1-y2)^2  +  (z1-z2)^2)
   Tee aliohjelma, joka laskee kahden 3D-avaruuden pisteen välisen etäisyyden
   ja laita tämä testattuasi talteen ensi jakson K-means algoritmin toteutusta
   varten.
'''

def etaisyys(p1,p2):
    return np.sqrt(np.power((p2[0]-p1[0]),2) +  np.power((p2[1]-p1[1]),2) + np.power((p2[2]-p1[2]),2) )

data = np.zeros((2,3))
data[0][:]=np.ones(3)
data[1][:]=2*np.ones(3)

print(data)
print("neliöjuuri 3 on = ", np.sqrt(3))
print(etaisyys(data[0][:],data[1][:]))