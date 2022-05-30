from Silnik.Roslina import Roslina


class Guarana(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 4

    def rysowanie(self):
        return "@"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Guarana)

    def stworz_nowy(self, nowyY, nowyX):
        return Guarana(nowyY, nowyX)

    def kolizja(self, atakujacy):
        atakujacy.set_sila(atakujacy.get_sila() + 3)
        print(atakujacy.rysowanie(), "zjadlo guarane i zwiekszylo sile do", atakujacy.get_sila())
        self.smierc()
