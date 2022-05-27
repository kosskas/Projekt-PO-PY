from Zwierzeta.Owca import Owca


#from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego


class CyberOwca(Owca):
    def __init__(self, posY, posX, wiek=0):
        super(Owca, self).__init__(11, 4)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "0"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, CyberOwca)

    def stworz_nowy(self, nowyY, nowyX):
        return CyberOwca(nowyY, nowyX)


    def nowa_pozycja(self):
        barsY, barsX = self.swiat.znajdzBarszcz(self.y, self.x)
        if barsX is None:
            super().nowa_pozycja()
        else:
            if self.x < barsX:
                self.nextX = self.x + 1
            elif self.x > barsX:
                self.nextX = self.x - 1
            if self.y < barsY:
                self.nextY = self.y + 1
            elif self.y > barsY:
                self.nextY = self.y - 1
