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
            return False
        else:
            return True

    def rozmnazanie(self, drugi):
        if self.wiek > 2 and drugi.GetWiek() > 2:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    dziecko = self.swiat.pobierzWspolrzedne(self.x + dy, self.x + dx)
                    if dziecko == None and self.swiat.sprawdzPoprawnoscWspolrzednych(self.y + dy, self.x + dx):
                        dziecko = self.stworzNowy(self.y + dy, self.x + dx)
                        if dziecko != None:
                            self.swiat.dodajOrganizm(dziecko)
                        break

    def smierc(self):
        self.zyje = False

    def nowaTura(self):
        ++self.wiek

    def kolizja(self, atakujacy):
        if self.czyOdbilAtak(atakujacy) == True:
            print(self.rysowanie(),"zabil",atakujacy.rysowanie())
            atakujacy.smierc()
        else:
            print(atakujacy.rysowanie(),"zabil",self.rysowanie())
            self.smierc()
    
    def SetSwiat(self, S):
        self.swiat = S

    def SetSila(self, sila):
        self.sila = sila

    def SetWiek(self, wiek):
        self.wiek = wiek

    def czyZyje(self):
        return self.zyje == True

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