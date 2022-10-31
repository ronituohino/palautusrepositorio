import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_etsi_pelaajat_tiimissa(self):
        players = self.statistics.team("EDM")
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_paras_pelaaja(self):
        player = self.statistics.top(1)[0]
        self.assertEqual(player.name, "Gretzky")

    def test_etsi_pelaaja_ei_tulosta(self):
        self.assertEqual(self.statistics.search("Kucherov"), None)

    # def test_parhaat_pelaajat_ylivuoto(self):
    #    players = self.statistics.top(7)
    #    self.assertEqual(players, [])