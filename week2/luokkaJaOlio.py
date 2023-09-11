
# Luokan määrittely
class Henkilo:
    # Luokan konstruktori
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    # Metodi luokan tietojen tulostamiseen
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Ikä: {self.ika}")
        print("nimi =",self.nimi)

    def tarkista_tiedot(self,nimi,ika):
        tiedotOikein = False
        if((nimi == self.nimi) & (ika==self.ika)):
            tiedotOikein = True
        print("tiedot on ", tiedotOikein)



# Luokan käyttö
henkilo1 = Henkilo("Matti", 30)
henkilo2 = Henkilo("Maija", 25)

# Kutsutaan metodia tulosta_tiedot
henkilo1.tulosta_tiedot()
henkilo2.tulosta_tiedot()
henkilo1.tarkista_tiedot("Matti",30)

