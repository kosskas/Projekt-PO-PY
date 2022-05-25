from Roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansaSiewu = 10

    def rysowanie(self):
        return "*"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Mlecz)
    
    def stworzNowy(self, nowyY, nowyX):
        return Mlecz(nowyY, nowyX)

    def akcja(self):
        for i in range(3):
            self.rozmnazanie(self)