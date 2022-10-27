from environment.TicTacToe import TicTacToe, REWARD_WIN, REWARD_LOSE, REWARD_DRAW, REWARD_NEUTRAL
import unittest


class TicTacToeTestGameOutcome(unittest.TestCase):
    def test_vertical_win_player1_case1(self):
        game = TicTacToe()
        moves = [0, 8, 3, 7, 6]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_vertical_win_player1_case2(self):
        game = TicTacToe()
        moves = [1, 8, 4, 2, 7]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_vertical_win_player1_case3(self):
        game = TicTacToe()
        moves = [2, 0, 5, 7, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player1_case1(self):
        game = TicTacToe()
        moves = [0, 8, 1, 7, 2]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player1_case2(self):
        game = TicTacToe()
        moves = [3, 8, 4, 2, 5]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player1_case3(self):
        game = TicTacToe()
        moves = [6, 0, 7, 1, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_vertical_win_player2_case1(self):
        game = TicTacToe()
        moves = [1, 0, 2, 3, 4, 6]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_vertical_win_player2_case2(self):
        game = TicTacToe()
        moves = [0, 1, 2, 4, 5, 7]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_vertical_win_player2_case3(self):
        game = TicTacToe()
        moves = [2, 0, 5, 7, 8]
        moves = [0, 2, 1, 5, 7, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player2_case1(self):
        game = TicTacToe()
        moves = [0, 8, 1, 7, 2]
        moves = [3, 0, 8, 1, 7, 2]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player2_case2(self):
        game = TicTacToe()
        moves = [3, 8, 4, 2, 5]
        moves = [0, 3, 8, 4, 2, 5]

        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_horizontal_win_player2_case3(self):
        game = TicTacToe()
        moves = [6, 0, 7, 1, 8]
        moves = [4, 6, 0, 7, 1, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_diagonal_win_player1_case1(self):
        game = TicTacToe()
        moves = [6, 0, 4, 1, 2]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_diagonal_win_player1_case2(self):
        game = TicTacToe()
        moves = [0, 2, 4, 1, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_WIN)
        self.assertEqual(game.get_reward(1), REWARD_LOSE)
        self.assertTrue(game.is_game_over())

    def test_diagonal_win_player1_case1(self):
        game = TicTacToe()
        moves = [5, 6, 0, 4, 1, 2]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_diagonal_win_player1_case2(self):
        game = TicTacToe()
        moves = [5, 0, 2, 4, 1, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_LOSE)
        self.assertEqual(game.get_reward(1), REWARD_WIN)
        self.assertTrue(game.is_game_over())

    def test_draw(self):
        game = TicTacToe()
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_DRAW)
        self.assertEqual(game.get_reward(1), REWARD_DRAW)
        self.assertTrue(game.is_game_over())

    def test_game_not_ended(self):
        game = TicTacToe()
        moves = [0, 1]
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_reward(0), REWARD_NEUTRAL)
        self.assertEqual(game.get_reward(1), REWARD_NEUTRAL)
        self.assertFalse(game.is_game_over())


class TicTacToeTestAvalibleMoves(unittest.TestCase):
    def test_get_moves_case1(self):
        game = TicTacToe()
        moves = []
        for i in moves:
            game.move(i)
        self.assertEqual(game.get_moves(), [0, 1, 2, 3, 4, 5, 6, 7, 8])


class TicTacToeTestValidMoves(unittest.TestCase):
    def test_invalid_move_case1(self):
        game = TicTacToe()
        moves = [0]
        for i in moves:
            game.move(i)
        self.assertEqual(game.is_valid_move(0), False)

    def test_invalid_move_case2(self):
        game = TicTacToe()
        moves = [0, 1, 2, 6, 8, 6]
        for i in moves:
            game.move(i)
        self.assertEqual(game.is_valid_move(2), False)

    def test_valid_move_case1(self):
        game = TicTacToe()
        moves = [0]
        for i in moves:
            game.move(i)
        self.assertEqual(game.is_valid_move(1), True)

    def test_valid_move_case2(self):
        game = TicTacToe()
        moves = [0, 1, 2, 6, 8, 6]
        for i in moves:
            game.move(i)
        self.assertEqual(game.is_valid_move(7), True)


if __name__ == "__main__":
    unittest.main()
