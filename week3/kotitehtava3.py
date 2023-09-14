'''
Käytetään alla olevaa demonstroimaan Google CoLabissa pandas interactive table ominaisuutta.
Jätetään tämä tähän, jotta opiskelijat voivat itsekin helposti kokeilla miten se
toimi Colabissa.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import data_table
from vega_datasets import data

'''

'''
Viikkotehtävä 3


Alla olevan esimerkkikoodin avulla saat luettua world-data-2023.csv tiedostosta
195 riviä ja 35 saraketta tietoa eri maiden tilanteesta. Tehtävät ovat seuraavat:

1. Muokkaa Pandas data framea siten, että valitset sieltä mielenkiintoisimmat sarakkeet, 
   jotka ovat:
   Country,Land Area, Armed Forces size,Co2-Emissions,GDP,Life expectancy,Population, Total tax rate, Unemployment rate
   Vinkki: Kysy chatGPT:ltä neuvoa, tehtävän eri vaiheissa. Sieltä saat hyviä toimivia esimerkkikoodeja käyttöösi.

2. Taulukossa on NaN lukuja, jotka ovat ongelmiallisia maksimi arvoja haettaessa. Muuta kaikki Nan => 0.
   Taulukossa on myös $ ja % merkkejä, jotka kannattaa muuttaa tyhjiksi merkeiksi ennen laskuoperaatioita.
   Taulukon numerot on esitetty muodossa 3,003,000 eli pilkut pitää muuttaa tyhjiksi merkeiksi.

3. Laske/selvitä sen jälkeen taulukosta
   a) Millä maalla on suurimmat asejoukot
   b) Millä maalla on eniten sotilaita maan kokoon verrattuna.
   c) Millä maalla on eniten sotilaita maan väestöön verrattuna.
   d) Luettele 5 suurinta Co2 päästäjää
   e) Selvitä, mihin maahan sinun kannattaisi mennä töihin valmistuttuasi (saat itse perustella GDP:n Life expectancy, Total tax rate ja Unemployment
      rate lukujen perusteella.)

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#selected_columns = ['Country','Land Area','Armed Forces size','Co2-Emissions','GDP','Life expectancy','Population','Total tax rate','Unemployment']
cols = ['Country','Land Area(Km2)','Armed Forces size','Co2-Emissions','GDP','Life expectancy','Population','Total tax rate','Unemployment rate']

#selected_columns = ["Country"]
df = pd.read_csv('world-data-2023.csv',usecols=cols)
#df = pd.read_csv('c:\\Users\\kajyrkk....world-data-2023.csv',usecols=selected_columns)
#print(df.head())

#print(df.iloc[0:10])
#df[cols[2]] = df[cols[2]].astype('string') 
#print("ennen korjausta = ", df[cols[2]].iloc[0:10])
#df[cols[2]] = df[cols[2]].str.replace(',','') 
#df[cols[2]] = df[cols[2]].fillna('0')
#print("jälkeen korjauksen = ", df[cols[2]].iloc[0:10])

for i in cols:
    #print("indeksi = ", i)
    df[i] = df[i].astype('string')
    df[i] = df[i].str.replace(',','')
    df[i] = df[i].str.replace('%','') 
    df[i] = df[i].str.replace('$','')
    df[i] = df[i].fillna('0') 

for j in range(1,df.shape[1]):
    df[cols[j]] = df[cols[j]].astype(float)

df['teht_b'] = df['Armed Forces size'] / df['Land Area(Km2)']

print("Suurimmat joukot/land size = ",df['Country'].iloc[df['teht_b'].argmax()])

plt.figure(1)
plt.stem(df['teht_b'])
plt.show()

print(df.head())
'''
plt.figure(1)
plt.stem(df[cols[2]].iloc[75:80])
plt.show()

print("Suurimmat sota joukot kuvasta pääteltynä on",df['Country'].iloc[77])
'''




