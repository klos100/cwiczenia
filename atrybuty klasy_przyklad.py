class Samochod(object):
    kolejny_nr_seryjny = 1  # atrybut klasy
    def __init__(self):  # self to nowo utworzona instancja
        # ustawiamy atrybuty instancji (teraz widzimy, po co nam self)
        self.predkosc = 0
        self.nr_seryjny = self.kolejny_nr_seryjny  # używamy atrybutu klasy "kolejny_nr_seryjny"
        # zwiększamy wartość atrybutu klasy "kolejny_nr_seryjny"
        self.__class__.kolejny_nr_seryjny = self.kolejny_nr_seryjny + 1
        # (^ mamy tu operację przypisania, dlatego dobieramy się
        #  do atrybutu poprzez klasę - by przypisać wartość atrybutowi
        #  klasy, a *nie* przesłonić atrybut klasy atrybutem instancji
        #  o identycznej nazwie)
        print ('nr', self.nr_seryjny)
    def wypisz_predkosc(self):
        print ('nr', self.nr_seryjny, '- predkosc:', self.predkosc, 'km/h')
    def dodaj_gazu(self, o_ile):
        self.predkosc += o_ile
        self.wypisz_predkosc()
    def hamuj(self, o_ile):
        self.predkosc -= o_ile
        self.wypisz_predkosc()


s1 = Samochod()  # -> nr 1
s2 = Samochod()  # -> nr 2
s1.dodaj_gazu(50)  # -> nr 1 - predkosc: 50 km/h
s2.dodaj_gazu(30)  # -> nr 2 - predkosc: 30 km/h
s1.hamuj(28)  # -> nr 1 - predkosc: 22 km/h
s2.hamuj(28)  # -> nr 2 - predkosc: 2 km/h

Samochod.kolejny_nr_seryjny = 100
s3 = Samochod()  # -> nr 100
Samochod.kolejny_nr_seryjny = 0
s4 = Samochod()  # -> nr 0