import numpy as np
import matplotlib.pyplot as plt


'''
Tehtävä 1

luo 5 Hz kompleksinen signaali välille 0s - 2s. Käytä näytetaajuutena Fs = 100 Hz
Tulosta kuva 3D-tasoon (cos-komponentti, sin-komponentti ja aika-akseli)

Tehtävä 2

Moduloi edellä luotu kompleksinen signaali kosinihaarassa biteillä 0 1 0 1
ja sini haarassa biteillä 0 0 1 1 ja tulosta samalla tavalla 3D-tasossa


Tehtävä 3
Demoduloi edellä luotu moduloitu kompleksinen signaali ja tulosta samalla
tavalla 3D-tasossa.



Tehtävä 4
Tee CRC-simulaattori. Tee aliohjelma, jolla saat luotua X kpl virheitä Y-mittaiseen inputtina
annettuun bittivektoriin. Ja kun tuo aliohjelma on valmis, niin tee simulointi, missä
luot 100 bittiä pitkän informaatiosignaalin, lisäät siihen 3-bittisen CRC-tarkisteen.
Sen jälkeen kutsut aliohjelmaasi, joka tekee ensin X kpl virheitä koodattuun bittijonoon
Ja lopuksi ajat virheellisen koodatun bittijonon vielä CRC-tarkisteen läpi ja tarkistat
osasiko CRC tunnistaa virheen tapahtuneen. Näitä steppejä toistetaan esim 1000 kertaa
ja sen jälkeen tulostetaan montako kertaa 1000:sta CRC tunnisti oikein.
'''

t = np.arange(0,2,0.01)
j = complex(0,1)
sig = np.exp(j*2*np.pi*5*t)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(t,sig.real,sig.imag,c='red')
plt.show()