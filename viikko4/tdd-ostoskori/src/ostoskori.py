from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in list(self._ostokset.values()))

    def hinta(self):
        return sum(ostos.hinta() for ostos in list(self._ostokset.values()))

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()
        if nimi in self._ostokset:
            self._ostokset[nimi].muuta_lukumaaraa(1)
        else:
            self._ostokset[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self) -> list[Ostos]:
        return list(self._ostokset.values())
