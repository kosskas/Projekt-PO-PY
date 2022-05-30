from Silnik.Organizm import Organizm
import random


class Roslina(Organizm):
    szansa_siewu = None

    def __init__(self, s):
        self.sila = s
        self.inicjatywa = 0
        self.wiek = 0
        self.zyje = True

    def akcja(self):
        if not self.wykonal_ruch:
            if  random.randrange(0, 100) <= self.szansa_siewu:
                self.rozmnazanie(self)
            self.wykonal_ruch = True

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Roslina)

    def rysowanie(self):
        pass
