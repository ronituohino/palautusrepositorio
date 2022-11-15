import requests
from player import Player


class PlayerReader:
    def __init__(self, url) -> None:
        response = requests.get(url).json()
        players = []

        for player_dict in response:
            player = Player(
                player_dict["name"],
                player_dict["nationality"],
                player_dict["team"],
                player_dict["goals"],
                player_dict["assists"],
            )

            players.append(player)

        self.players = players
