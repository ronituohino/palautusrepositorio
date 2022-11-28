class TennisGame:
    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self._score1 = 0
        self._score2 = 0

    def won_point(self, player: str) -> None:
        if player == self.player1:
            self._score1 += 1
        else:
            self._score2 += 1

    def get_score(self):
        score_text_by_point = ["Love", "Fifteen", "Thirty", "Forty"]
        max_score = max(self._score1, self._score2)

        if self._score1 == self._score2:
            # Players are even
            if max_score < 4:
                return f"{score_text_by_point[self._score1]}-All"
            else:
                return "Deuce"
        else:
            # One of the players is leading
            if max_score < 4:
                return f"{score_text_by_point[self._score1]}-{score_text_by_point[self._score2]}"
            else:
                score_difference = self._score1 - self._score2

                if score_difference == 1:
                    return f"Advantage {self.player1}"
                if score_difference == -1:
                    return f"Advantage {self.player2}"
                if score_difference >= 2:
                    return f"Win for {self.player1}"
                else:
                    return f"Win for {self.player2}"
