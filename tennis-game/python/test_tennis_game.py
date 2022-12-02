import unittest
from tennis_game import TennisGame, Player


class TestTennisGame(unittest.TestCase):

    def test_should_return_initial_score(self):
        playerA = Player()
        playerB = Player()
        game = TennisGame(playerA, playerB)
        actual_score = game.score()
        expected_sore = "0:0"

        self.assertEqual(expected_sore, actual_score)

    def test_should_return_a_correct_score_when_the_playerA_wins_a_point(self):
        playerA = Player()
        playerB = Player()
        game = TennisGame(playerA, playerB)
        playerA.win_point()
        actual_score = game.score()
        expected_score = "15:0"

        self.assertEqual(expected_score, actual_score)

    def test_should_return_a_correct_score_when_the_playerB_wins_a_point(self):
        playerA = Player()
        playerB = Player()
        game = TennisGame(playerA, playerB)
        playerB.win_point()
        actual_result = game.score()
        expected_result = "0:15"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_correct_score_when_both_players_score_the_same_number_of_points(self):
        playerA = Player()
        playerB = Player()
        game = TennisGame(playerA, playerB)
        playerB.win_point()
        playerB.win_point()
        playerA.win_point()
        playerA.win_point()
        actual_result = game.score()
        expected_result = "30:30"

        self.assertEqual(expected_result, actual_result)


    def test_should_return_correct_score_when_one_player_scores_the_maximum_points(self):
        playerA = Player()
        playerB = Player()
        game = TennisGame(playerA, playerB)
        playerA.win_point()
        playerB.win_point()
        playerA.win_point()
        playerA.win_point()
        actual_result = game.score()
        expected_result = "40:15"

        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()
