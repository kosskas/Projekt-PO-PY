from Zwierze import Zwierze
import random


class Antylopa(Zwierze):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(4, 4)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "A"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Antylopa)
    
    def stworzNowy(self, nowyY, nowyX):
        return Antylopa(nowyY, nowyX)

    def nowaPozycja(self):
        dy = random.randrange(-2, 2)
        dx = random.randrange(-2, 2)
        if self.swiat.sprawdzPoprawnoscWspolrzednych(self.y + dy, self.x + dx):
            self.nextX = self.x + dx
            self.nextY = self.y + dy
            self.prevX = self.x
            self.prevY = self.y
    
    def kolizja(self, atakujacy):
        if random.randrange(0, 100) <= 50:
            self.nowaPozycja()
            kolizyjny = self.swiat.pobierzWspolrzedne(self.nextY, self.nextX)
            if kolizyjny is not None and kolizyjny is not self:
                super().kolizja(atakujacy)
            else:
                self.x = self.nextX
                self.y = self.nextY
        else:
            super().kolizja(atakujacy)
