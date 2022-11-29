KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatus=None):
        if kapasiteetti == None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        if kasvatus == None:
            self.kasvatus = OLETUSKASVATUS
        else:
            self.kasvatus = kasvatus

        self.joukko = []

    def kuuluu(self, n) -> bool:
        return n in self.joukko

    def mahtavuus(self):
        return len(self.joukko)

    def lisaa(self, n) -> bool:
        if not self.kuuluu(n):
            # Jos kapassiteetti tulee täyteen, kasvatetaan
            if self.kapasiteetti - 1 >= self.mahtavuus():
                self.kapasiteetti += self.kasvatus

                uusi_joukko = []
                for i in self.joukko:
                    uusi_joukko.append(i)
                uusi_joukko.append(n)

                self.joukko = uusi_joukko
            else:
                self.joukko.append(n)
            return True
        return False

    def poista(self, n) -> bool:
        if self.kuuluu(n):
            self.joukko.remove(n)
            return True
        return False

    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(a, b):
        uusi = IntJoukko()
        for i in a.to_int_list():
            uusi.lisaa(i)
        for i in b.to_int_list():
            uusi.lisaa(i)
        return uusi

    @staticmethod
    def leikkaus(a, b):
        uusi = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                uusi.lisaa(i)
        return uusi

    @staticmethod
    def erotus(a, b):
        uusi = IntJoukko()
        for i in a.to_int_list():
            if not b.kuuluu(i):
                uusi.lisaa(i)
        return uusi

    def __str__(self):
        sisalto = ", ".join(str(i) for i in self.to_int_list())

        # \u007b = {
        # \u007d = }
        return f"\u007b{sisalto}\u007d"
