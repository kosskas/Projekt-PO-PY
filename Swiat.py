from Organizm import Organizm
import datetime
import random
import sys
class Swiat:
    plansza = []
    wymX = None
    wymY = None
    orgaznizmy = []
    tura = 0
    seed = 0

    def __init__(self, Y, X, L, ziarno = 0, runda = 0):
        self.wymX = X
        self.wymY = Y
        for y in range(Y):
            wiersz = []
            for x in range(X):
                wiersz.append("")
            self.plansza.append(wiersz)


        self.orgaznizmy = L
        self.dodajOrganizmy(L)
        self.seed = random.seed(2)
        tura = 0

    def rysujSwiat(self):
        self.wyczyscMape()
        self.naniesOrganizmyNaMape()
        self.rysujMape()

    def dodajOrganizmy(self, L):
        self.orgaznizmy = L
        for N in self.orgaznizmy:
            N.SetSwiat(self)

    def naniesOrganizmyNaMape(self):
        print("test")
        for N in self.orgaznizmy:
            if N.czyZyje() == True:
                print(N.rysowanie(), N.GetY(), N.GetX())
                #self.plansza[1][1] = N.rysowanie()

    def wyczyscMape(self):
        self.plansza = []
        for y in range(self.wymY):
            wiersz = []
            for x in range(self.wymX):
                wiersz.append("")
            self.plansza.append(wiersz)

    def rysujMape(self):
        print(self.plansza)

    def symuluj(self):
        pass

    def zapiszSwiat(self):
        with open('zapis.txt', 'w') as f:
            print("[stan]", file=f)
            print("MAPA",self.wymY,self.wymX, file=f)
            print("SEED",self.seed, file=f)
            print("TURA",self.tura, file=f)
            print("[org]", file=f)
            for N in self.orgaznizmy:
                print(N.rysowanie(),N.GetY(),N.GetX(),N.GetWiek(), file=f)
            print("[org]", file=f)
            print("[stan]", file=f)

    def GetX(self):
        return self.wymX

    def GetY(self):
        return self.wymY

    def sprawdzPoprawnoscWspolrzednych(self, y, x):
        return x < self.wymX and x >= 0 and y < self.wymY and y >= 0

    def wykonajTure(self):
        ++self.tura
        self.zwolnijMiejsce()
        for N in self.orgaznizmy:
            N.nowaTura()
            if N.GetWiek() > -1:
                N.akcja()

    def pobierzWspolrzedne(self, y, x):
        for N in self.orgaznizmy:
            if N.GetY() == y and N.GetX() == x and N.czyZyje():
                return N
        return None

    def dodajOrganizm(self, nowy):
        nowy.SetSwiat(self)
        self.orgaznizmy.append(nowy)

    def zwolnijMiejsce(self):
        self.orgaznizmy = [N for N in self.orgaznizmy if N.czyZyje()]