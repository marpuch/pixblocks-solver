from src.entity.tile import Tile, Direction, TileType


class Board:
    def __init__(self, board: list):
        self.board = []
        for row in board:
            tab = []
            self.board.append(tab)
            for cell in row:
                tab.append(Tile.from_str(cell))
        self.__apply_gravity()

    def __apply_gravity(self):
        for col in range(0, self.width()):
            while self.__apply_gravity_to_column(col):
                print("gravity applied to column {}".format(col))

    def __apply_gravity_to_column(self, col) -> bool:
        last_unmovable = None
        first_empty = None
        for row in range(self.height()-1, 0, -1):
            if self.board[row][col].tile_type.falls_down():
                if last_unmovable is None:
                    self.board[row][col] = Tile()
                elif first_empty is not None:
                    self.board[row][col], self.board[first_empty][col] = \
                        self.board[first_empty][col], self.board[row][col]
                    return True
                else:
                    last_unmovable = row
            elif self.board[row][col].tile_type.fixed_position():
                last_unmovable = row
                first_empty = None
            elif first_empty is None:
                first_empty = row

        return False

    def __str__(self):
        result = []
        for row in self.board:
            for cell in row:
                result.append(str(cell))
            result.append('\n')
        return ''.join(result)

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board)

    def next(self):
        next_board = self.clone()
        rabbits = self.find_rabbits()
        for rabbit in rabbits:
            next_board.__move(*rabbit)
            next_board.__apply_gravity()
        return next_board

    def find_rabbits(self):
        return self.find(TileType.RABBIT)

    def find_carrots(self):
        return self.find(TileType.CARROT)

    def find(self, t):
        result = []
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell.tile_type == t:
                    result.append((x, y))
        return result

    def __move(self, x, y):
        rabbit = self.board[y][x]
        if rabbit.direction == Direction.LEFT:
            if x == 0:
                self.board[y][x] = Tile()
            elif self.board[y][x-1].tile_type.is_eatable():
                self.board[y][x] = Tile()
                self.board[y][x-1] = rabbit
            else:
                rabbit.direction = Direction.RIGHT
        else:
            if x == self.width()-1:
                self.board[y][x] = Tile()
            elif self.board[y][x+1].tile_type.is_eatable():
                self.board[y][x] = Tile()
                self.board[y][x+1] = rabbit
            else:
                rabbit.direction = Direction.LEFT

    def clone(self):
        return Board(str(self).strip().split('\n'))

