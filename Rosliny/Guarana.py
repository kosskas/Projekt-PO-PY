from Roslina import Roslina

class Guarana(Roslina):
    def __init__(self, posY, posX, wiek=0):
        super().__init__(0)
        self.x = posX
        self.y = posY
        self.szansaSiewu = 8

    def rysowanie(self):
        return "&"

    def porownajGatunek(self, drugi):
        return isinstance(drugi, Guarana)
    
    def stworzNowy(self, nowyY, nowyX):
        return Guarana(nowyY, nowyX)

    def kolizja(self, atakujacy):
        print(atakujacy.rysowanie(),"zjadlo guarane i zwiekszylo sile do",atakujacy.GetSila())
        atakujacy.SetSila(atakujacy.GetSila() + 3)
        self.smierc()