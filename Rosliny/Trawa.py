from Silnik.Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 33

    def rysowanie(self):
        return "#"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Trawa)

    def stworz_nowy(self, nowyY, nowyX):
        return Trawa(nowyY, nowyX)
