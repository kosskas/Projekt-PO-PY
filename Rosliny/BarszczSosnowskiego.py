from Roslina import Roslina
from Zwierzeta.CyberOwca import CyberOwca

class BarszczSosnowskiego(Roslina):
    sasiad = []

    def __init__(self, posY, posX, wiek=0):
        super().__init__(10)
        self.x = posX
        self.y = posY
        self.szansaSiewu = 3

    def rysowanie(self):
        return "$"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, BarszczSosnowskiego)
    
    def stworzNowy(self, nowyY, nowyX):
        return BarszczSosnowskiego(nowyY, nowyX)

    def kolizja(self, atakujacy):
        print(atakujacy.rysowanie(), "je barszcz i ginie")
        atakujacy.smierc()
        self.smierc()

    def akcja(self):
        self.GetSasiedzzi()
        for Org in self.sasiad:
            if Org is not None and not super().porownajGatunek(Org) and not isinstance(Org, CyberOwca):
                print(Org.rysowanie(), "gine od barszczu")
                Org.smierc()
        if self.wiek > 1:
            super().akcja()

    def GetSasiedzzi(self):
        self.sasiad.clear()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy is 0 and dx is 0:
                    continue
                self.sasiad.append(self.swiat.pobierzWspolrzedne(self.y + dy, self.x + dx))