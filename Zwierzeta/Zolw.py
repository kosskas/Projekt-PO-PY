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

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Zolw)
    
    def stworzNowy(self, nowyY, nowyX):
        return Zolw(nowyY, nowyX)

    def nowaPozycja(self):
        if random.randrange(0, 100) <= 25:
            super().nowaPozycja
        else:
            self.nextX = self.x
            self.nextY = self.y