from src.control.game import Game
import logging


def main():
    game = Game(['......',
                 '.E..C.',
                 'X...C.',
                 'X....X',
                 'XXXXXX'])
    logging.info("Game won? {}".format(game.play()))
    game.trace()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
