import random
import sys
import time
from datetime import datetime
from Zwierzeta import *
from Rosliny import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Swiat(QMainWindow):
    plansza = []
    wymX = None
    wymY = None
    orgaznizmy = []
    tura = 0
    seed = 0
    elemMapy = []
    label = None
    pressY, pressX = None, None
    btn_Y, btn_X =  100, 50
    sterowanie = None
    dodawanie = None
    ruch = [0, 0]
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    dodaj = []
    text = None

    def __init__(self, Y, X):
        super().__init__()       
        print("Poruszanie na WSAD")
        self.wymX = X
        self.wymY = Y 
        self.dodaj_organizmy(self.dodaj_bazowe_organizmy())
        self.inicjuj_gre(int(time.time() * 256), 0)
        self.inicjuj_okno()
        self.keyPressed.connect(self.ruch_czlowieka)

    def inicjuj_gre(self, ziarno, runda):
        self.plansza = []
        self.tura = runda
        
        self.seed = ziarno
        random.seed(ziarno)

        for y in range(self.wymY):
            wiersz = []
            for x in range(self.wymX):
                wiersz.append("")
            self.plansza.append(wiersz)

    def rysuj_swiat(self):
        self.wyczysc_mape()
        self.nanies_organizmy_na_mape()

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

    def zapisz_swiat(self):
        with open('zapis.txt', 'w') as f:
            print("[stan]", file=f)
            print("MAPA",file=f)
            print(self.wymY, file=f)
            print(self.wymX, file=f)
            print("SEED", file=f)
            print(self.seed, file=f)
            print("TURA", file=f)
            print(self.tura, file=f)
            print("[org]", file=f)
            for N in self.orgaznizmy:
                print(N.rysowanie(), file=f)
                print(N.get_Y(), file=f)
                print(N.get_X(), file=f)
                print(N.get_wiek(), file=f)
            print("[org]", file=f)
            print("[stan]", file=f)

    def wczytaj_swiat(self):
        with open("zapis.txt") as f:
            lines = []
            for line in f:
                lines.append(line)
            self.wczytaj_gre(lines)

    def wczytaj_gre(self, gra):
        L = []
        y, x = None, None
        ziarno, runda = 0, 0
        posX, posY, wiek = None, None, None
        for i in range(0, len(gra)):
            if gra[i] == "MAPA\n":
                y = int(gra[i+1])
                x = int(gra[i+2])
            if gra[i] == "SEED\n":
                ziarno = int(gra[i+1])
            if gra[i] == "TURA\n":
                runda = int(gra[i+1])
            if gra[i] == "W\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Wilk(posY, posX, wiek))
            if gra[i] == "O\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Owca(posY, posX, wiek))
            if gra[i] == "L\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Lis(posY, posX, wiek))
            if gra[i] == "A\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Antylopa(posY, posX, wiek))
            if gra[i] == "Z\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Zolw(posY, posX, wiek))
            if gra[i] == "C\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Czlowiek(posY, posX, wiek))
            if gra[i] == "Ó\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(CyberOwca(posY, posX, wiek))
            if gra[i] == "$\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(BarszczSosnowskiego(posY, posX, wiek))
            if gra[i] == "%\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(WilczeJagody(posY, posX, wiek))
            if gra[i] == "#\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Trawa(posY, posX, wiek))
            if gra[i] == "*\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Mlecz(posY, posX, wiek))
            if gra[i] == "@\n":
                posY = int(gra[i+1])
                posX = int(gra[i+2])
                wiek = int(gra[i+3])
                L.append(Guarana(posY, posX, wiek))
        if y is not None and x is not None and L:
            self.dodaj_organizmy(L)
            self.tura = runda
            self.seed = ziarno
            self.wymY = y
            self.wymX = x
            self.inicjuj_gre(ziarno, runda)

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
            if N.get_wiek() > 1 and N.czy_zyje():
                N.akcja()

    def nowa_tura(self):
        self.wykonaj_ture()
        self.rysuj_swiat()

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
        L = [Czlowiek(0,0), Owca(1,0), Owca(0,1), BarszczSosnowskiego(4,0), BarszczSosnowskiego(3, 4),
             Lis(5,4), Lis(4,3), Zolw(7,7), Zolw(1,9), Owca(7,8), Trawa(7,2), Mlecz(8,5), Guarana(2,7),
             Antylopa(8,3), Antylopa(6,7), Antylopa(8,7), Antylopa(2,2), WilczeJagody(5,7), Wilk(3,6),
             Wilk(3,5), CyberOwca(9,7)]
        return L

    def koloruj_guzik(self, y, x):
        org = self.plansza[y][x]
        if org == '$': #BarszczSosnowskiego d
            return "#84AC50"
        elif org == '%': #WilczeJagody
            return "#9249A9"
        elif org == '*': #Mlecz d
            return "#ECF174"
        elif org == '#': #Trawa d
            return "#0DA416"#"#42EE13"
        elif org == '@': #Guarana d
            return "#E85B2E" 
        elif org == 'O': #Owca d
            return "#E7E7DB"
        elif org == 'Ó': #cyberowca d
            return "#AFA799"
        elif org == 'A': #antylopa d
            return "#BE8D0B"  
        elif org == 'L': #lis d
            return "#EB7E10"
        elif org == 'C': #czlowiek d
            return "#139ABE"
        elif org == 'W': #wilk d
            return "#3B3A3A"
        elif org == 'Z': #zolw d
            return "#888A88"

    #///////////////////////////

    def aktualizuj_mape(self):
        for y in range(self.wymY):
            for x in range(self.wymX):
                self.elemMapy[y][x].setText(self.plansza[y][x])
                self.elemMapy[y][x].setStyleSheet("background-color: "+str(self.koloruj_guzik(y, x)))

    def inicjuj_okno(self):
        self.setGeometry(100, 100, 1280, 980) 
        self.setWindowTitle("Symulator swiata")
        self.inicjuj_guziki()
        self.show()

    def inicjuj_guziki(self):
        self.inicjuj_mape()
        self.inicjuj_nowa_tura_guzik()
        self.inicjuj_zapisz_guzik()
        self.inicjuj_wczytaj_guzik()
        self.inicjuj_dodawanie_guziki()

    def inicjuj_mape(self):
        for i in range(self.wymY):
            tmp = []
            for j in range(self.wymX):
                tmp.append(QPushButton(self))
            self.elemMapy.append(tmp)
        x = 40
        y = 40
        for i in range(self.wymY):
            for j in range(self.wymX):
                self.elemMapy[i][j].setGeometry(y*i+20,
												x*j+20,
												40, 40)
                self.elemMapy[i][j].setContentsMargins(0, 0, 0, 0)
                self.elemMapy[i][j].clicked.connect(self.dodaj_organizm_akcja)

    def inicjuj_nowa_tura_guzik(self):
        nowaTura = QPushButton("Nowa Tura", self)
        nowaTura.setGeometry(self.wymY*40+50, 20, self.btn_Y, self.btn_X)
        nowaTura.clicked.connect(self.nowa_tura_akcja)
    
    def inicjuj_zapisz_guzik(self):
        zapisz = QPushButton("Zapisz", self)
        zapisz.setGeometry(self.wymY*40+50+self.btn_Y ,20, self.btn_Y, self.btn_X)
        zapisz.clicked.connect(self.zapisz_gre_akcja)

    def inicjuj_wczytaj_guzik(self):
        wczytaj = QPushButton("Wczytaj", self)
        wczytaj.setGeometry(self.wymY*40+50+2*self.btn_Y ,20, self.btn_Y, self.btn_X)
        wczytaj.clicked.connect(self.wczytaj_gre_akcja)


    def inicjuj_dodawanie_guziki(self):
        self.dodawanie = { "Wilk" : QPushButton("Wilk", self), "Antylopa" : QPushButton("Antylopa", self), "CyberOwca" : QPushButton("CyberOwca", self),
                           "Owca": QPushButton("Owca", self), "Lis": QPushButton("Lis", self),  "Zolw" : QPushButton("Zolw", self),
                           "BarszczSosnowskiego" : QPushButton("BarszczSosnowskiego", self), "Guarana" : QPushButton("Guarana", self),
                           "Mlecz" : QPushButton("Mlecz", self), "Trawa" : QPushButton("Trawa", self), "WilczeJagody" :  QPushButton("WilczeJagody", self)}

        y, x= 150, 50
        posY = self.wymY*40+50+self.btn_Y
        posX = 150
        self.text = QLabel("test", self)
        self.text.setGeometry(posY ,posX-x, y, x)
        for B in self.dodawanie:
            self.dodawanie[B].setGeometry(posY ,posX, y, x)
            self.dodawanie[B].clicked.connect(self.dodaj_konkretny_organizm_akcja)
            posX+=x


    def dodaj_organizm_akcja(self):
        button = self.sender()
        for i in range(self.wymY):
            for j in range(self.wymX):
                if self.elemMapy[i][j] == button and self.plansza[i][j] == " ":
                    self.dodaj = [i, j]
                    self.text.setText("Dodaj na "+str(self.dodaj))
                    return
                else:
                    self.dodaj = [-1, -1]
                    self.text.setText("Nie mozna tu postawic")

    def dodaj_konkretny_organizm_akcja(self):
        button = self.sender()
        if self.dodaj == [-1, -1]:
            print("Nie")
            return
        for B in self.dodawanie:
            if self.dodawanie[B] == button:
                Org = globals()[B]
                nowy = Org(self.dodaj[0], self.dodaj[1])
                self.dodaj_organizm(nowy)
                self.rysuj_swiat()
                self.aktualizuj_mape()
                self.dodaj = [-1, -1]
                return


    def zapisz_gre_akcja(self):
        self.zapisz_swiat()
        self.setWindowTitle("Zapisano ture "+str(self.tura))

    def wczytaj_gre_akcja(self):
        self.wczytaj_swiat()
        self.rysuj_swiat()
        self.aktualizuj_mape()
        self.setWindowTitle("Wczytano ture "+str(self.tura))

    def nowa_tura_akcja(self):
        self.nowa_tura()
        self.aktualizuj_mape()
        self.setWindowTitle("Symulator swiata - tura "+str(self.tura))

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event)

    def ruch_czlowieka(self, event):
        if event.key() == QtCore.Qt.Key_W:
            print("Gora")
            self.ruch = [-1, 0]
        elif event.key() == QtCore.Qt.Key_S:
            print("Dol")
            self.ruch = [1, 0]
        elif event.key() == QtCore.Qt.Key_A:
            print("Lewo")
            self.ruch = [0, -1]
        elif event.key() == QtCore.Qt.Key_D:
            print("Prawo")
            self.ruch = [0, 1]
        elif event.key() == QtCore.Qt.Key_U:
            print("Ult")
            self.ruch = ["u", "u"]