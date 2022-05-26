from Zwierze import Zwierze
import random


class Zolw(Zwierze):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(3, 7)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "Z"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Zolw)

    def stworz_nowy(self, nowyY, nowyX):
        return Zolw(nowyY, nowyX)

    def nowa_pozycja(self):
        if random.randrange(0, 100) <= 25:
            super().nowa_pozycja()
        else:
            self.nextX = self.x
            self.nextY = self.y
    
    def kolizja(self, atakujacy):
        if atakujacy.get_sila() < 5:
            atakujacy.wycofaj_sie()
        else:
            self.smierc()
