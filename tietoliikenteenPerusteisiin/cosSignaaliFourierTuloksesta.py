import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import lueAaniTiedostosta as tiedosto

# Määrittele äänilaitteen asetukset
#sample_rate = 44100  # Näytteenottotaajuus (Hz)
sample_rate = 8000
duration = 10  # Äänen kesto sekunneissa
volume = 0.5  # Äänen voimakkuus (0.0 - 1.0)

# Luo äänilaitteen hallintakäyttöliittymä
p = pyaudio.PyAudio()


# Käsitellään tässä signaalia, missä on häiriö, hoksattavat asiat:
# 1. importattiin python tiedosto, joka "valmistelee" meille signaalin lukemalla sen CSV-tiedostosta Pandas-kirjaston avulla
# 2. Lasketaan Fourier-muunnos 2000 näytteen yli ja SKAALATAAN tulos N = 2000, miksi olikaan näin?
# 3. Fourier-muunnoksen tuloksesta löytyy 3 piikkiä, mitä taajuuksia ne esittävät? Fourier-muunnoksen resoluutio = Fs / N
# 4. Ja sitten piti vielä muistaa, että mitä ne Fourier-muunnoksen kompleksiluvut meille aikatason signaalista kertoivat:
#    - kompleksiluvun pituus = aikatason kosini signaalin amplitudi
#    - kompleksiluvun vaihe = aikatason kosini signaalin vaihe ajan hetkelle = 0
# 5. Jos tiedetään tarkalleen signaaliin summautunut häiriö, voidaan se "suodattaa" vähentämällä häiriösignaali häiritystä.

plt.figure(1)
plt.subplot(4,1,1),plt.plot(tiedosto.sig),plt.title('aanisignaali aikatasossa')

Fs = 8000
N = 2000

taajuustaso = np.fft.fft(tiedosto.sig[0:N])/N

deltaF = Fs/N
MoneskoPiikkiOn2500Hz = 2500/deltaF
print("häiriö löytyy piikistä = ", MoneskoPiikkiOn2500Hz)
print("taajuustaso[625] =",taajuustaso[625])

Cluku=taajuustaso[625]
# Muodostetaan tuon kompleksiluvun avulla kosini signaali, joka häiritsee ääntä ja vähennetään se

t = np.arange(0,10,1/Fs)  # 10 sekunnin signaalia tehdään, sillä äänisignaalikin on sen mittainen
A = 2*np.abs(Cluku)       # Koska lasketaan vain toisesta "piikistä", niin siksi kertominen kahdella
vaihe = np.angle(Cluku)  

hairio = A*np.cos(2*np.pi*2500*t + vaihe)



plt.subplot(4,1,2),plt.stem(np.abs(taajuustaso)),plt.title('aanisignaali taajuustasossa')
plt.subplot(4,1,3),plt.plot(hairio[0:N]),plt.title('hairio muodostettuna kompleksiluvusta')
plt.subplot(4,1,4),plt.plot(tiedosto.sig[0:N]-hairio[0:N]),plt.title('hairio havitetty vahentamalla')

plt.show()


'''

soitetaan = tiedosto.sig - hairio

buffer_size = len(tiedosto.sig)
buffer = soitetaan.astype(np.float32).tobytes()

# Luo äänentoistoääniprosessi
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=sample_rate,
    output=True
)

# Toista näytejonon sisältö kaiuttimesta
for _ in range(int(sample_rate * duration / buffer_size)):
    stream.write(buffer)

# Sulje äänentoistoprosessi ja vapauta resurssit
stream.stop_stream()
stream.close()
p.terminate()

'''


