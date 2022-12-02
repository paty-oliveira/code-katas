class Player:
    def __init__(self):
        self.points = 0
        self.ball_win = 0

    def win_point(self):
        self.ball_win += 1
        if self.ball_win <= 2:
            self.points += 15
        elif self.ball_win == 3:
            self.points += 10
        elif self.ball_win >= 4:
            self.points += 0


class TennisGame:

    def __init__(self, playerA: Player, playerB: Player):
        self.playerA = playerA
        self.playerB = playerB

    def score(self):
        player_a_points = self.playerA.points
        player_b_points = self.playerB.points

        if self.playerB.ball_win > self.playerA.ball_win and player_b_points == 40:
            return f"{player_a_points}:A"

        if self.playerA.ball_win > self.playerB.ball_win and player_a_points == 40:
            return f"A:{player_b_points}"

        return f"{player_a_points}:{player_b_points}"
