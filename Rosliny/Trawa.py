from Roslina import Roslina

class Trawa(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansaSiewu = 33

    def rysowanie(self):
        return "#"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Trawa)
    
    def stworzNowy(self, nowyY, nowyX):
        return Trawa(nowyY, nowyX)