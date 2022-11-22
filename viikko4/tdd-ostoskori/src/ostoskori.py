from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self, tuotteet: list[Tuote] = []):
        self.ostos_list = []
        for t in tuotteet:
            self.ostos_list.append(Ostos(t))

    def tavaroita_korissa(self):
        return len(self.ostos_list)

    def hinta(self):
        return 0

    def lisaa_tuote(self, lisattava: Tuote):
        self.ostos_list.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
