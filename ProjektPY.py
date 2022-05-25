from Rosliny import *
from Zwierzeta import *
from Swiat import Swiat



L = [Owca(1, 1), Owca(2,2), Owca(1, 0), Wilk(0, 0), Antylopa(4, 4), BarszczSosnowskiego(5, 5), Zolw(3, 4), Trawa(6, 6), CyberOwca(6, 9)]

S = Swiat(10, 10, L)
S.symuluj(15)
