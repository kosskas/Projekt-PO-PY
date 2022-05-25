from Zwierzeta.Owca import Owca
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego


class CyberOwca(Owca):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(11, 4)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "0"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, CyberOwca)
    
    def stworzNowy(self, nowyY, nowyX):
        return CyberOwca(nowyY, nowyX)

    def znajdzBarszcz(self):
        dl = 10000
        barsY, barsX = None, None
        for N in self.swiat.orgaznizmy:
            if isinstance(N, BarszczSosnowskiego):
                dist = (self.x - N.GetX())**2 + (self.y - N.GetY())**2
                if dist < dl:
                    dl = dist
                    barsY =  N.GetY()
                    barsX =  N.GetX()
        return barsY, barsX

    def nowaPozycja(self):
         barsY, barsX = self.znajdzBarszcz()
         if barsX is None:
             super().nowaPozycja()
         else:
             if self.x < barsX:
                 self.nextX = self.x + 1
             elif self.x > barsX:
                 self.nextX = self.x - 1
             if self.y < barsY:
                 self.nextY = self.y + 1
             elif self.y > barsY:
                 self.nextY = self.y - 1
