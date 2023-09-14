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
'''
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("data np.array() komennolla = ", data)

toinenTapa = np.arange(1,10,1)
toinenTapa = np.reshape(toinenTapa,(3,3))
print("data toisella tavalla generoituna = ", toinenTapa)

'''
2. Tee aliohjelma, joka ottaa parametrina tehtävässä 1 muodostetun arrayn
   ja palauttaa rivin 1 ja rivin 2 alkioiden erotuksen sekä rivin 2 ja rivin 3 erotuksen
   eli tuloksena tulee kaksirivinen Numpy taulukko, jonka alkiot ovat
   3,3,3
   3,3,3
'''
def aliohjelma(d):
    
    koko = d.shape
    tulos = np.zeros(  ((koko[0]-1),koko[1])   )
    print("tulos ennen prosessointia =", tulos)
    for rivit in range(1,koko[0]):
        tulos[rivit-1][:] = d[rivit][:] - d[rivit-1][:]
    print("tulos prosessoinnin jälkeen = ", tulos)
    return tulos




aliohjelma(data)


'''
3. 3D-avaruudessa kahden pisteen välinen etäisyys lasketaan seuraavasti
   etäisyys = sqrt( (x1-x2)^2  + (y1-y2)^2  +  (z1-z2)^2)
   Tee aliohjelma, joka laskee kahden 3D-avaruuden pisteen välisen etäisyyden
   ja laita tämä testattuasi talteen ensi jakson K-means algoritmin toteutusta
   varten.
'''

def etaisyys3Davaruudessa(p1,p2):
    xEro = p1[0]-p2[0]
    yEro = p1[1]-p2[1]
    zEro = p1[2]-p2[2]
    tulos = np.sqrt( np.power((xEro),2) + np.power((yEro),2) + np.power((zEro),2)  )
    return tulos

print("neliöjuuri 3 = ", np.sqrt(3))
print("1,1,1 ja 2,2,2 pisteiden etaisyys = ", etaisyys3Davaruudessa(np.ones(3),2*np.ones(3)))


'''
4. Tee python ohjelma, jolla saat muodostettua 3D-avaruuden pisteitä 100 kpl
   Numpy taulukkoon (jossa siis 100 kpl rivejä ja kullakin rivillä 3 (x,y,z) pistettä)
   pisteiden x,y,z arvot vaihtelevat välillä 0-1000 satunnaisesti.

'''

taulukko = np.random.randint(0,1024,(100,3))
print(taulukko)

'''
5. Tee yksi tunnettu 3D-avaruuden piste esim 10,20,30. Tee aliohjelma, joka
   laskee tuon tunnetun pisteen etäisyyden kaikkiin 100 satunnaisesti arpomaasi 3D
   avaruuden pisteeseen ja tulostaa pisteen, jonka etäisyys on lähinnä tuota tunnettua
   pistettä.

'''

p = np.array([10,20,30])

minimi = 1000000
paikka = -1
riveja = taulukko.shape[0]
for i in range(riveja):
    etaisyys = etaisyys3Davaruudessa(taulukko[i][:],p)
    if(etaisyys < minimi):
        minimi = etaisyys
        paikka = i

print("minimietäisyys löytyi riviltä ", paikka)
print("Ja tuo etäisyys = ", minimi)


