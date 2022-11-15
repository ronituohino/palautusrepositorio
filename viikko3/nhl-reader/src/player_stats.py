class PlayerStats:
    def __init__(self, player_reader) -> None:
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(
                lambda player: player.nationality == nationality,
                self.player_reader.players,
            ),
            key=lambda player: player.points,
            reverse=True,
        )
