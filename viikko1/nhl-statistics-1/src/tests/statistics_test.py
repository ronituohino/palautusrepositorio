import unittest
from statistics import Statistics
from statistics import SortBy
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
        player = self.statistics.top(3)[0]
        self.assertEqual(player.name, "Gretzky")

    def test_etsi_pelaaja_ei_tulosta(self):
        self.assertEqual(self.statistics.search("Kucherov"), None)

    def test_paras_pelaaja_points(self):
        player1 = self.statistics.top(3, SortBy.POINTS)[0]
        player2 = self.statistics.top(3)[0]
        self.assertEqual(player1.name, player2.name)
        self.assertEqual(player1.name, "Gretzky")

    def test_paras_pelaaja_goals(self):
        player = self.statistics.top(3, SortBy.GOALS)[0]
        self.assertEqual(player.name, "Lemieux")

    def test_paras_pelaaja_assists(self):
        # myös paras pelaaja
        player1 = self.statistics.top(3, SortBy.ASSISTS)[0]
        self.assertEqual(player1.name, "Gretzky")

        # eri kuin toiseksi paras pelaaja pisteiden perusteella
        player2 = self.statistics.top(3, SortBy.ASSISTS)[1]
        self.assertEqual(player2.name, "Yzerman")