from src.entity.board import Board
import logging


class Game:

    def __init__(self, board: list):
        self.last_board = Board(board)
        self.game_log = {str(self.last_board): None}

    def play(self):
        while True:

            carrots = self.last_board.find_carrots()
            if not carrots:
                return True

            rabbits = self.last_board.find_rabbits()
            if not rabbits:
                return False

            self.last_board = self.last_board.next()
            board_str = str(self.last_board)

            if board_str in self.game_log.keys():
                return False

            self.game_log.update({board_str: None})

    def trace(self):
        if not logging.getLogger().isEnabledFor(logging.INFO):
            return
        for game in self.game_log.keys():
            logging.info("\n" + game)

