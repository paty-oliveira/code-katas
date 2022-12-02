class Player:
    MOVEMENTS_POINTS = {
        1: 15,
        2: 15,
        3: 10
    }

    def __init__(self):
        self.points = 0
        self.ball_win = 0

    def win_point(self):
        self.ball_win += 1
        self.points += self.MOVEMENTS_POINTS[self.ball_win]


class TennisGame:

    def __init__(self, playerA: Player, playerB: Player):
        self.playerA = playerA
        self.playerB = playerB

    def score(self):
        player_a_points = str(self.playerA.points)
        player_b_points = str(self.playerB.points)

        return f"{player_a_points}:{player_b_points}"
