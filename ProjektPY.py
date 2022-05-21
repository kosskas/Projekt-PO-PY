from Organizm import Organizm
from Zwierze import Zwierze
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Swiat import Swiat


L = [Owca(1, 1), Owca(2,2), Owca(1, 0), Wilk(0, 0)]

S = Swiat(3, 3, L)
S.rysujSwiat()
S.wykonajTure()
S.rysujSwiat()
