class TennisGame:
    scores = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
        4: "Advantage"
    }
    def __init__(self):
        self.points_playerOne = 0
        self.points_playerTwo = 0

    def score(self):
        if self.has_winner():
            return f"{self.player_with_highest_score()} wins"

        if self.is_deuce():
            return "Deuce"

        if self.is_advantage():
            return f"Advantage {self.player_with_highest_score()}"

        else:
            return f"{self.scores[self.points_playerOne]}:{self.scores[self.points_playerTwo]}"

    def playerOne_wins_point(self):
        self.points_playerOne += 1

    def playerTwo_wins_point(self):
        self.points_playerTwo += 1

    def is_deuce(self):
        return self.points_playerOne >= 3 and self.points_playerOne == self.points_playerTwo

    def is_advantage(self):
        if self.points_playerOne >= 4 and self.points_playerOne == self.points_playerTwo + 1:
            return True
        return self.points_playerTwo >= 4 and self.points_playerTwo == self.points_playerOne + 1

    def has_winner(self):
        if self.points_playerTwo >= 4 and self.points_playerTwo >= self.points_playerOne + 2:
            return True
        return self.points_playerOne >= 4 and self.points_playerOne >= self.points_playerTwo + 2

    def player_with_highest_score(self):
        if self.points_playerOne > self.points_playerTwo:
            return "PlayerOne"
        return "PlayerTwo"
