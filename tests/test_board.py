import unittest
from tictactoe.board import Board, CellOccupiedError
from tictactoe.position import Position


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)

    def test_add_token_successful(self):
        self.board.add_token(Position(2, 1), 'O')
        self.assertEqual(self.board.get_cell(Position(2, 1)).token, 'O')

    def test_add_token_unsuccessful(self):
        self.board.add_token(Position(2, 1), 'O')
        self.assertRaises(CellOccupiedError, self.board.add_token, Position(2, 1), 'O')

    def test_get_winning_token_diagonal_win(self):
        self.board.add_token(Position(0, 0), 'O')
        self.board.add_token(Position(1, 1), 'O')
        self.board.add_token(Position(2, 2), 'O')
        self.assertEqual(self.board.get_winning_token(), 'O')

    def test_get_winning_token_diagonal_no_win(self):
        self.board.add_token(Position(0, 0), 'O')
        self.board.add_token(Position(1, 1), 'O')
        self.board.add_token(Position(2, 2), 'X')
        self.assertIsNone(self.board.get_winning_token())


if __name__ == '__main__':
    unittest.main()
