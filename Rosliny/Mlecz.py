from Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 10

    def rysowanie(self):
        return "*"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Mlecz)

    def stworz_nowy(self, nowyY, nowyX):
        return Mlecz(nowyY, nowyX)

    def akcja(self):
        for i in range(3):
            self.rozmnazanie(self)
