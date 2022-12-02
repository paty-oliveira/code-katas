import unittest
from tennis_game import TennisGame

class TestTennisGame(unittest.TestCase):
    def test_should_return_initial_score(self):
        game = TennisGame()
        actual_score = game.score()
        expected_score = "Love:Love"

        self.assertEqual(expected_score, actual_score)

    def test_should_return_correct_score_when_player_one_wins_one_point(self):
        game = TennisGame()
        game.playerOne_wins_point()
        actual_result = game.score()
        expected_score = "Fifteen:Love"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_player_two_wins_one_point(self):
        game = TennisGame()
        game.playerTwo_wins_point()
        actual_result = game.score()
        expected_score = "Love:Fifteen"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_player_one_wins_two_points(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        actual_result = game.score()
        expected_score = "Thirty:Love"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_both_players_score(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        actual_result = game.score()
        expected_score = "Fifteen:Fifteen"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_player_one_wins_three_points(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        actual_result = game.score()
        expected_score = "Forty:Love"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_both_players_are_deuce(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        actual_result = game.score()
        expected_score = "Deuce"

        self.assertEqual(expected_score, actual_result)

    def test_should_return_correct_score_when_player_one_is_in_advantage(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        actual_result = game.score()

        expected_result = "Advantage PlayerOne"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_correct_score_when_player_two_is_in_advantage(self):
        game = TennisGame()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        game.playerTwo_wins_point()
        actual_result = game.score()

        expected_result = "Advantage PlayerTwo"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_correct_score_when_both_players_have_same_points(self):
        game = TennisGame()
        game.playerTwo_wins_point()
        game.playerOne_wins_point()
        actual_result = game.score()
        expected_result = "Fifteen:Fifteen"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_correct_score_when_player_one_wins(self):
        game = TennisGame()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        game.playerOne_wins_point()
        game.playerOne_wins_point()

        actual_result = game.score()
        expected_result = "PlayerOne wins"

        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()
