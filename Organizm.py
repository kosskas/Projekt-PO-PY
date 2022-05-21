class Organizm:
    sila = None
    inicjatywa = None
    wiek = None
    swiat = None
    x = None
    y = None
    zyje = None

    def czyOdbilAtak(self, atakujacy):
        if self.sila < atakujacy.GetSila():
            return True
        else:
            return False

    def rozmnazanie(self, drugi):
        if self.wiek > 2 and drugi.GetWiek() > 2:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    dziecko = self.swiat.pobierzWspolrzedne(self.x + dy, self.x + dx)
                    if dziecko == None and self.swiat.sprawdzPoprawnoscWspolrzednych(y + dy, x + dx):
                        dziecko = self.stworzNowy(y + dy, x + dx)
                        if dziecko != None:
                            self.swiat.dodajOrganizm(dziecko)
                        break

    def smierc(self):
        zyje = False

    def nowaTura(self):
        wiek = wiek + 1

    def kolizja(self, atakujacy):
        if self.czyOdbilAtak(atakujacy) == True:
            Print(self.rysowanie()+" zabil "+atakujacy.rysowanie()+'\n')
            atakujacy.smierc()
        else:
            Print(atakujacy.rysowanie()+" zabil "+self.rysowanie()+'\n')
            self.smierc()
    
    def SetSwiat(self, S):
        self.swiat = S

    def SetSila(self, sila):
        self.sila = sila

    def SetWiek(self, wiek):
        self.wiek = wiek

    def czyZyje(self):
        return self.zyje

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetSila(self):
        return self.sila

    def GetInicjatywa(self):
        return self.inicjatywa

    def GetWiek(self):
        return self.wiek