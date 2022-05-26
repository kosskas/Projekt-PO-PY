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


    def akcja(self):
        if not self.wykonal_ruch:
            self.nowa_pozycja()
            kolizyjny = self.swiat.pobierz_wspolrzedne(self.nextY, self.nextX)
            self.wykonaj_ruch_na(kolizyjny)
            self.x = self.nextX
            self.y = self.nextY
            self.wykonal_ruch = True

    def wykonaj_ruch_na(self, kolizyjny):
        if kolizyjny is not None and kolizyjny != self:
            if self.porownaj_gatunek(kolizyjny):
                self.rozmnazanie(kolizyjny)
                self.nextX = self.x
                self.nextY = self.y
            else:
                kolizyjny.kolizja(self)

    def nowa_pozycja(self):
        dy = random.randrange(-1, 1)
        dx = random.randrange(-1, 1)
        if self.swiat.sprawdz_poprawnosc_wspolrzednych(self.y + dy, self.x + dx):
            self.nextX = self.x + dx
            self.nextY = self.y + dy
            self.prevX = self.x
            self.prevY = self.y

    def wycofaj_sie(self):
        self.nextX = self.prevX
        self.nextY = self.prevY

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Zwierze)

    def rysowanie(self):
        pass
