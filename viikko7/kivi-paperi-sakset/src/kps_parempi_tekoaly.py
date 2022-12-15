from tekoaly_parannettu import TekoalyParannettu
from pelitehdas import KPS


class KPSParempiTekoaly(KPS):
    def pelaa(self):
        self.tekoaly = TekoalyParannettu(10)
        super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
