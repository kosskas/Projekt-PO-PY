from Swiat import *
from Rosliny import *
from Zwierzeta import *


L = [Owca(1, 1), Owca(2, 2), Owca(1, 0), Wilk(0, 0), Antylopa(4, 4), BarszczSosnowskiego(5, 5), Zolw(3, 4), Trawa(6, 6), Lis(5, 7), CyberOwca(5, 6)]

S = Swiat(10, 10, L)
S.symuluj(15)
