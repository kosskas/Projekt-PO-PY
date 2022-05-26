from Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(99)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 8

    def rysowanie(self):
        return "%"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, WilczeJagody)

    def stworz_nowy(self, nowyY, nowyX):
        return WilczeJagody(nowyY, nowyX)

    def kolizja(self, atakujacy):
        atakujacy.smierc()
        self.smierc()
