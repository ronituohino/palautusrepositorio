import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuotteet = [Tuote("proteeini", 15), Tuote("kreatiini", 12)]

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.hinta(), self.tuotteet[0].hinta())

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.assertEqual(
            self.kori.hinta(), self.tuotteet[0].hinta() + self.tuotteet[1].hinta()
        )

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.hinta(), 2 * self.tuotteet[0].hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(
        self,
    ):
        tuote = self.tuotteet[1]

        self.kori.lisaa_tuote(tuote)
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        # testataan eri referenssill??
        tuote1 = Tuote("maito", 12)
        tuote2 = Tuote("maito", 12)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_saman_tuotteen_joista_yhden_poistaminen_jattaa_olion(self):
        # testataan eri referenssill??
        tuote1 = Tuote("maito", 12)
        tuote2 = Tuote("maito", 12)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)

        self.kori.poista_tuote(tuote1)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_yhden_tuotteen_poistaminen_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.poista_tuote(self.tuotteet[0])

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
