from Zwierze import Zwierze

class Owca(Zwierze):
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
        return "O"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Owca)
    
    def stworzNowy(self, nowyY, nowyX):
        return Owca(nowyY, nowyX)