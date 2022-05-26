from Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(3, 7)
        self.x = posX
        self.y = posY
        self.wiek = wiek
        self.prevX = self.x
        self.prevY = self.y
        self.nextY = self.y
        self.nextX = self.x

    def rysowanie(self):
        return "L"

    def porownaj_gatunek(self, drugi):
        return isinstance(drugi, Lis)
    
    def stworz_nowy(self, nowyY, nowyX):
        return Lis(nowyY, nowyX)

    def wykonaj_ruch_na(self, kolizyjny):
        if kolizyjny is not None and kolizyjny is not self and kolizyjny.get_sila() > self.sila:
            print("lis")
            self.nextX = self.x
            self.nextY = self.y
        else:
            super().wykonaj_ruch_na(kolizyjny)