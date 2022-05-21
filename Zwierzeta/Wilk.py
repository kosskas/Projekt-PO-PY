from Zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(9, 5)
        self.x = posX
        self.y = posY
        self.wiek = wiek

    def rysowanie(self):
        return "W"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Wilk)
    
    def stworzNowy(self, nowyY, nowyX):
        return Wilk(nowyY, nowyX)


