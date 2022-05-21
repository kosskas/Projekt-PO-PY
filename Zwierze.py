from Organizm import Organizm
import random

class Zwierze(Organizm):
    nextX = None
    nextY = None
    prevX = None
    prevY = None

    def __init__(self, s, i):
        self.sila = s
        self.inicjatywa = i
        self.wiek = 0
        self.zyje = True
        self.prevX = self.x
        self.prevY = self.y
        self.nexyY = self.y
        self.nextX = self.x

    def akcja(self):
        self.nowaPozycja()
        kolizyjny = self.swiat.pobierzWspolrzedne(self.nextY, self.nextX)
        self.wykonajRuchNa(kolizyjny)
        self.x = self.nextX
        self.y = self.nextY
        print(self.rysowanie(), self.y, self.y)

    def wykonajRuchNa(self, kolizyjny):
        if kolizyjny != None and kolizyjny != self:
            if self.porownajGatunek(kolizyjny) == True:
                self.rozmnazanie(kolizyjny)
                self.nextX = self.x
                self.nextY = self.y
            else:
                kolizyjny.kolizja(self)

    def nowaPozycja(self):
        dx = -1
        dy = -1
        dy = random.randrange(-1, 1)
        dx = random.randrange(-1, 1)
        if self.swiat.sprawdzPoprawnoscWspolrzednych(self.y + dy, self.x + dx) == True:
            self.nextX = self.x + dx
            self.nextY = self.y + dy
            self.prevX = self.x
            self.prevY = self.y

    def wycofajSie(self):
        self.nextX = self.prevX
        self.nextY = self.prevY

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Zwierze)
