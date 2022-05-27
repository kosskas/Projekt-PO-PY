from Silnik.Roslina import Roslina
from Zwierzeta.CyberOwca import CyberOwca


class BarszczSosnowskiego(Roslina):
    sasiad = []

    def __init__(self, posY, posX, wiek=0):
        super().__init__(10)
        self.x = posX
        self.y = posY
        self.szansa_siewu = 3

    def rysowanie(self):
        return "$"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, BarszczSosnowskiego)

    def stworz_nowy(self, nowyY, nowyX):
        return BarszczSosnowskiego(nowyY, nowyX)

    def kolizja(self, atakujacy):
        if isinstance(atakujacy, CyberOwca):
            print(atakujacy.rysowanie(), "je barszcz ale to cyberOwca")
        else:
            print(atakujacy.rysowanie(), "je barszcz i ginie")
            atakujacy.smierc()
        self.smierc()

    def akcja(self):
        self.get_sasiedzi()
        for Org in self.sasiad:
            if Org is not None and not super().porownaj_gatunek(Org) and not isinstance(Org, CyberOwca):
                print(Org.rysowanie(), "gine od barszczu")
                Org.smierc()
        if self.wiek > 1:
            super().akcja()

    def get_sasiedzi(self):
        self.sasiad.clear()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy is 0 and dx is 0:
                    continue
                self.sasiad.append(self.swiat.pobierz_wspolrzedne(self.y + dy, self.x + dx))
