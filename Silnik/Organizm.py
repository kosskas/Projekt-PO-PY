class Organizm:
    sila = None
    inicjatywa = None
    wiek = None
    swiat = None
    x = None
    y = None
    zyje = None
    wykonal_ruch = None

    def czy_odbil_atak(self, atakujacy):
        if self.sila < atakujacy.get_sila():
            return False
        else:
            return True

    def rozmnazanie(self, drugi):
        if self.wiek > 2 and drugi.get_wiek() > 2:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    dziecko = self.swiat.pobierz_wspolrzedne(self.x + dy, self.x + dx)
                    if dziecko is None and self.swiat.sprawdz_poprawnosc_wspolrzednych(self.y + dy, self.x + dx):
                        dziecko = self.stworz_nowy(self.y + dy, self.x + dx)
                        if dziecko is not None:
                            self.swiat.dodaj_organizm(dziecko)
                            return
                        break

    def smierc(self):
        self.zyje = False

    def nowa_tura(self):
        self.wiek = self.wiek + 1
        self.wykonal_ruch = False

    def kolizja(self, atakujacy):
        if self.czy_odbil_atak(atakujacy):
            print(self.rysowanie(),"[",self.get_sila(), "] zabil ", atakujacy.rysowanie(),"[",atakujacy.get_sila(),"]")
            atakujacy.smierc()
        else:
            print(atakujacy.rysowanie(),"[",atakujacy.get_sila(), "] zabil ", self.rysowanie(),"[",self.get_sila(),"]")
            self.smierc()



    def __lt__(self, inny):
        if self.inicjatywa < inny.inicjatywa:
            return True
        elif self.inicjatywa == inny.inicjatywa:
            return self.wiek < inny.wiek
        else:
            return False

    def set_swiat(self, S):
        self.swiat = S

    def set_sila(self, sila):
        self.sila = sila

    def set_wiek(self, wiek):
        self.wiek = wiek

    def czy_zyje(self):
        if self.zyje:
            return True
        else:
            return False

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_sila(self):
        return self.sila

    def get_inicjatywa(self):
        return self.inicjatywa

    def get_wiek(self):
        return self.wiek

    def stworz_nowy(self, param, param1):
        pass

    def rysowanie(self):
        pass
