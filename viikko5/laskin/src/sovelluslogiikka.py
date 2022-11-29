class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_komento = None

    def miinus(self, arvo, komento):
        self.tulos = self.tulos - arvo
        self.edellinen_komento = komento

    def plus(self, arvo, komento):
        self.tulos = self.tulos + arvo
        self.edellinen_komento = komento

    def nollaa(self, komento):
        self.tulos = 0
        self.edellinen_komento = komento

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        if self.edellinen_komento != None:
            self.edellinen_komento.kumoa()
        self.edellinen_komento = None


class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.syote = 0

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovelluslogiikka.plus(self.syote, self)

    def kumoa(self):
        self.sovelluslogiikka.miinus(self.syote, None)
        self.syote = 0


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.syote = 0

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovelluslogiikka.miinus(self.syote, self)

    def kumoa(self):
        self.sovelluslogiikka.plus(self.syote, None)
        self.syote = 0


class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.edellinen_tulos = 0

    def suorita(self):
        self.edellinen_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa(self)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_tulos)
        self.edellinen_tulos = 0


class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka) -> None:
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.kumoa()
