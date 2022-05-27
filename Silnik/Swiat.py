import random
import sys
from Zwierzeta import *
from Rosliny import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QFrame, QGridLayout, QSplitter, QMainWindow
#event listener po wcisnieciu n z w 
class Swiat(QWidget):
    plansza = []
    wymX = None
    wymY = None
    orgaznizmy = []
    tura = 0
    seed = 0
    elemMapy = {}
    label = None

    def __init__(self, Y, X, ziarno=0, runda=0):
        super().__init__()       
        self.wymX = X
        self.wymY = Y 
        for y in range(Y):
            wiersz = []
            for x in range(X):
                wiersz.append("")
            self.plansza.append(wiersz)
        self.dodaj_organizmy(self.dodaj_bazowe_organizmy())
        self.seed = random.seed(2)
        self.tura = 0
        self.inicjuj_okno()

    def rysuj_swiat(self):
        self.wyczysc_mape()
        self.nanies_organizmy_na_mape()
        self.rysuj_mape()

    def dodaj_organizmy(self, L):
        self.orgaznizmy = L
        for N in self.orgaznizmy:
            N.set_swiat(self)

    def nanies_organizmy_na_mape(self):
        for N in self.orgaznizmy:
            if N.czy_zyje():
                self.plansza[N.get_Y()][N.get_X()] = N.rysowanie()

    def wyczysc_mape(self):
        self.plansza = []
        for y in range(self.wymY):
            wiersz = []
            for x in range(self.wymX):
                wiersz.append(" ")
            self.plansza.append(wiersz)

    def rysuj_mape(self):
        for y in self.plansza:
            print(*y, sep=" ")

    def symuluj(self, iter):
        self.show()
    

        #for i in range(iter):
        #    self.rysuj_swiat()
        #    print("Tura", self.tura)
        #    self.wykonaj_ture()

    def zapisz_swiat(self):
        with open('zapis.txt', 'w') as f:
            print("[stan]", file=f)
            print("MAPA", self.wymY, self.wymX, file=f)
            print("SEED", self.seed, file=f)
            print("TURA", self.tura, file=f)
            print("[org]", file=f)
            for N in self.orgaznizmy:
                print(N.rysowanie(), N.get_Y(), N.get_X(), N.get_wiek(), file=f)
            print("[org]", file=f)
            print("[stan]", file=f)

    def get_X(self):
        return self.wymX

    def get_Y(self):
        return self.wymY

    def sprawdz_poprawnosc_wspolrzednych(self, y, x):
        return self.wymX > x >= 0 and self.wymY > y >= 0

    def wykonaj_ture(self):
        self.tura = self.tura + 1
        self.zwolnij_miejsce()
        for N in self.orgaznizmy:
            N.nowa_tura()
            if N.get_wiek() > -1:
                N.akcja()

    def pobierz_wspolrzedne(self, y, x):
        for N in self.orgaznizmy:
            if N.get_Y() == y and N.get_X() == x and N.czy_zyje():
                return N
        return None

    def dodaj_organizm(self, nowy):
        nowy.set_swiat(self)
        self.orgaznizmy.append(nowy)

    def zwolnij_miejsce(self):
        self.orgaznizmy = [N for N in self.orgaznizmy if N.czy_zyje()]

    
    def znajdzBarszcz(self, x, y):
        dl = 10000
        barsY, barsX = None, None
        for N in self.orgaznizmy:
            if isinstance(N, BarszczSosnowskiego):
                dist = (x - N.get_X()) ** 2 + (y - N.get_Y()) ** 2
                if dist < dl:
                    dl = dist
                    barsY = N.get_Y()
                    barsX = N.get_X()
        return barsY, barsX
    
    def dodaj_bazowe_organizmy(self):
            L = [Owca(1, 1), Owca(2, 2), Owca(1, 0), Wilk(0, 0), Antylopa(4, 4),
         BarszczSosnowskiego(5, 5), Zolw(3, 4), Trawa(6, 6), Lis(5, 7), CyberOwca(5, 6)]
            return L

    #///////////////////////////

    def inicjuj_okno(self):
        self.setGeometry(100, 100, 100, 100)   
        
        mapa = QGridLayout()
        self.label = QLabel("yhtyyyyyyyyyyyyyyyyy");
        
        mapa.setContentsMargins(0, 0, 0, 0)
        

        mapa.setSpacing(0)
        for i in range(self.wymY):
            for j in range(self.wymX):
                self.elemMapy[(i, j)] = QPushButton("")
                self.elemMapy[(i, j)].setGeometry(50, 50, 50, 50)
                self.elemMapy[(i, j)].setFixedSize(40, 40)
                self.elemMapy[(i, j)].setContentsMargins(0, 0, 0, 0)
                self.elemMapy[(i, j)].clicked.connect(self.button_clicked)
                mapa.addWidget(self.elemMapy[(i, j)], i, j)
        self.setLayout(mapa)
        
        
    def button_clicked(self):
            print("clicked")
            self.label.setText("you pressed the button")
