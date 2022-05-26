from Zwierze import Zwierze


class Czlowiek(Zwierze):
    czas_trwania = None
    czy_aktywna_umj = None
    czas_oczekiw = None
    czy_moze_uzyc = None
    def __init__(self, posY, posX, wiek=0):
        super().__init__(5, 4)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x
        self.czas_oczekiw = 0
        self.czas_trwania = 0
        self.czy_aktywna_umj = False
        self.czy_moze_uzyc = True

    def rysowanie(self):
        return "C"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Czlowiek)

    def stworz_nowy(self, nowyY, nowyX):
        return None

    def nowa_tura(self):
        if self.czy_aktywna_umj:
            self.czas_trwania = self.czas_trwania - 1
            self.sila = self.sila - 1
            if self.czas_trwania is 0:
                print("Zdolnosc przestala dzialac")
                self.czy_aktywna_umj = False
        elif not self.czy_moze_uzyc:
            self.czas_oczekiw = self.czas_oczekiw - 1
            if self.czas_oczekiw is 0:
                print("Zdolnosc gotowa do uzycia")
                self.czy_moze_uzyc = True
        super().nowa_tura()

    def wypij_magiczny_eliksir(self):
        self.czas_oczekiw = 5
        self.czas_trwania = 5
        self.czy_aktywna_umj = True
        self.czy_moze_uzyc = False
        self.sila = 10

    def nowa_pozycja(self):
        return super().nowa_pozycja()