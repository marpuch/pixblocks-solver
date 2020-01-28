from src.entity.board import Board
import unittest


class TestStringMethods(unittest.TestCase):

    def test_gravity(self):
        board = Board(['......',
                       '.E..C.',
                       'X...C.',
                       'X....X',
                       'XXXXXX'])

        self.assertEqual('......\n'
                         '......\n'
                         'X...C.\n'
                         'XE..CX\n'
                         'XXXXXX\n', str(board))

    def test_free_fall(self):
        board = Board(['......',
                       '.E..C.',
                       'X...C.',
                       'X....X',
                       'X.XXXX'])

        self.assertEqual('......\n'
                         '......\n'
                         'X...C.\n'
                         'X...CX\n'
                         'X.XXXX\n', str(board))

    def test_eating_carrot(self):
        board = Board(['......',
                       '....C.',
                       'X...C.',
                       'X..ECX',
                       'XXXXXX'])

        self.assertEqual('......\n'
                         '....C.\n'
                         'X...C.\n'
                         'X...EX\n'
                         'XXXXXX\n', str(board.next()))

    def test_turning_around(self):
        board = Board(['......',
                       '....C.',
                       'X...C.',
                       'X...EX',
                       'XXXXXX'])

        self.assertEqual('......\n'
                         '....C.\n'
                         'X...C.\n'
                         'X...3X\n'
                         'XXXXXX\n', str(board.next()))



