from Organizm import Organizm
import random

class Roslina(Organizm):
    szansaSiewu = None

    def __init__(self, s):
        self.sila = s
        self.inicjatywa = 0
        self.wiek = 0
        self.zyje = True


    def akcja(self):
        if not self.wykonalRuch:
            if random.randrange(0, 100) <= self.szansaSiewu:
                self.rozmnazanie(self)
            self.wykonalRuch = True

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Roslina)

    def rysowanie(self):
        pass
