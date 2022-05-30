from Silnik.Roslina import Roslina
import random

class Mlecz(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 5

    def rysowanie(self):
        return "*"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Mlecz)

    def stworz_nowy(self, nowyY, nowyX):
        return Mlecz(nowyY, nowyX)

    def akcja(self):
        if not self.wykonal_ruch:
            if  random.randrange(0, 100) <= self.szansa_siewu:
                for i in range(3):
                    self.rozmnazanie(self)
            self.wykonal_ruch = True
