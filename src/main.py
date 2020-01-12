from src.entity.board import Board
from src.control.game import Game


def main():
    game = Game(['......',
                 '.E..C.',
                 'X...C.',
                 'X....X',
                 'XXXXXX'])
    game.play()


if __name__ == '__main__':
    main()
