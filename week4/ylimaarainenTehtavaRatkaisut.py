import numpy as np

import matplotlib.pyplot as plt

'''
Tehtävät:

1. Tee numpy dataArray, jossa alkiot 0,1,2,..,9 kirjoita nuo alkiot string muodossa
   tiedostoon, jonka nimi on data.txt. Kukin alkio omalle rivilleen. Tarkista syntyneestä
   tiedostosta, että näin todella käy.

2. Lue edellisessä tehtävässä tekemästäsi data.txt tiedostosta seuraavasti:
   - Tee tyhjä python lista, johon sitten for luupilla luet rivin kerrallaan
     tiedostosta ja lisäät tuon rivin listaan append komennon avulla. Näin
     sinun ei tarvitse etukäteen tietää, kuinka monta riviä tiedostosta listaan
     tulee.
   - Muunna for luupin jälkeen python lista numpy string arrayksi
     numPyStringArray = np.array(python_list) komennolla
   - Ja lopuksi muunna numpy string array int arrayksi astype(int) komennon avulla
   - tulosta syntynyt numpy array print komennolla.


3. Tee kaksi numPy array vektoria a ja b, joissa on molemmissa alkiot 1,2,3
   - laske a + b
   - laske a * b
   - laske vektoreiden a ja b matriisikertolasku eli dot product (np.dot(a,b))
   - laske tuo dot product perinteisesti for luupin avulla.
   - dot product kertoo, kuinka paljon kahden vektorin arvot muistuttavat toisiaan = korrelaatio
     kokeile muuttaa a vektorin arvoja, jotta ymmärrät näin olevan. Kokeile saatko paremman
     korrelaatioarvon muuttelemalla arvojen 1,2,3 paikkoja vaikka vektorissa b.

4. Tee kaksi numPy matriiaia a ja b seuraavasti:
    a = np.array([[1,2,3],[-1,-2,-3]])
    b = np.reshape(a,(3,2)).copy() 

    Tulosta matriisit a ja b sekä laske matriisien dot product 
    Selitä itsellesi kynällä ja paperilla, miten dot product lasketaan a ja b matriiseista.

    Ja tee lopulta for luuppitoteutus, jolla lasket tuon saman dot product tuloksen
    Tätä "kykyä" tarvitset projektissa, jos aiot toteuttaa neuroverkon Nordicin piirille
    C-kielessähän ei ole tukea matriisilaskuille vaan joudut toteuttamaan matriisien 
    kertolaskut for-luupein. Ja sitä on tietysti helpompi harjoitella pythonissa.
         
'''

dataArray = np.arange(0,10)
print(dataArray)

with open ("data.txt","w") as WriteFileHandle:
    for i in range(len(dataArray)):
        WriteFileHandle.write(str(dataArray[i])+"\n")


with open ("data.txt","r") as ReadFileHandle:
    luettuArray = []
    indeksi = 0
    for line in ReadFileHandle:
        luettuArray.append(line)

print(luettuArray)
numpyluettuArray = np.array(luettuArray)
print(numpyluettuArray.astype(int))
        
