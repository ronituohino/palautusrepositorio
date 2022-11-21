import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()

        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            return [10, 1, 0][tuote_id]

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            return [
                Tuote(0, "maito", 5),
                Tuote(1, "Whey proteiini", 15),
                Tuote(2, "LSN Creatine Monohydrate", 12),
            ][tuote_id]

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodi_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(0)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodi_tilisiirto_kutsutaan_oikeat_argumentit(
        self,
    ):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(0)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 2, "12345", "33333-44455", 5
        )

    def test_kaksi_eri_ostosta_tilisiirto_kutsutaan_oikeat_argumentit(self):
        self.kauppa.lisaa_koriin(0)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jaakko", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "jaakko", 2, "54321", "33333-44455", 20
        )

    def test_kaksi_samaa_ostosta_tilisiirto_kutsutaan_oikeat_argumententit(self):
        self.kauppa.lisaa_koriin(0)
        self.kauppa.lisaa_koriin(0)
        self.kauppa.tilimaksu("pekko", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekko", 2, "11111", "33333-44455", 10
        )

    def test_kaksi_ostosta_toinen_loppunut_tilisiirto_kutsutaan_oikeat_argumentit(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("markku", "1337")

        # summana on ainoastaan tuotteen 1 hinta
        self.pankki_mock.tilisiirto.assert_called_with(
            "markku", 2, "1337", "33333-44455", 15
        )

    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        self.kauppa.lisaa_koriin(0)
        self.kauppa.tilimaksu("joonas", "123")

        self.pankki_mock.tilisiirto.assert_called()

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(0)
        self.kauppa.tilimaksu("joonas", "123")

        # viitegeneraattori on nyt 3, koska toinen ostos joka suoritettu
        # hinta on yhden tuotteen 0 verran (5)
        self.pankki_mock.tilisiirto.assert_called_with(
            "joonas", 3, "123", "33333-44455", 5
        )

    def test_uusi_viitenumero_ostoksilla(self):
        iters = 3
        for i in range(iters):
            self.kauppa.lisaa_koriin(0)
            self.kauppa.tilimaksu("maria", "444")

            self.pankki_mock.tilisiirto.assert_called_with(
                "maria", i + 2, "444", "33333-44455", 5
            )

            # seuraavaan iteraatioon
            if i < iters - 1:
                self.kauppa.aloita_asiointi()

    def test_tuote_voidaan_poistaa_korista(self):
        self.kauppa.lisaa_koriin(0)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(0)

        self.kauppa.tilimaksu("julia", "09090")

        self.pankki_mock.tilisiirto.assert_called_with(
            "julia", 2, "09090", "33333-44455", 15
        )
