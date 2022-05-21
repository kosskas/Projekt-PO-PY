from Organizm import Organizm
from Zwierze import Zwierze
from Zwierzeta.Owca import Owca

test = Organizm()
zw = Zwierze(3, 444)

owca = Owca(1, 2)

test.SetWiek(335)

print("Projekt\n")
print(test.GetWiek())
print(zw.GetInicjatywa())
print(owca.rysowanie())
