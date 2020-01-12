from src.entity.board import Board


class Game:

    def __init__(self, board: list):
        self.last_board = Board(board)
        self.game_log = dict.fromkeys(str(self.last_board))

    def play(self):
        while True:

            carrots = self.last_board.find_carrots()
            if not carrots:
                print('WON!')
                break

            rabbits = self.last_board.find_rabbits()
            if not rabbits:
                print('LOST!')
                break

            self.last_board = self.last_board.next()
            board_str = str(self.last_board)

            if board_str in self.game_log.keys():
                print('Situation repeated. LOST!')
                break

            self.game_log.update(board_str=None)
            print(board_str)

