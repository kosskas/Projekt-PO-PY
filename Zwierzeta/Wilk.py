from Silnik.Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(9, 5)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "W"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Wilk)

    def stworz_nowy(self, nowyY, nowyX):
        return Wilk(nowyY, nowyX)
