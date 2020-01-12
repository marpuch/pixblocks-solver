from enum import Enum


class TileType(Enum):
    """
    Different game board tile types
    """
    NOTHING = 1
    EARTH = 2
    CARROT = 3
    RABBIT = 4

    def is_eatable(self):
        return self in (TileType.NOTHING, TileType.CARROT)

    def falls_down(self):
        return self in (TileType.CARROT, TileType.RABBIT)

    def fixed_position(self):
        return self == TileType.EARTH


class Direction(Enum):
    """
    Direction the tile is facing
    """
    LEFT = 1
    RIGHT = 2
    NONE = 3

    def opposite(self):
        if self == Direction.LEFT:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.LEFT
        else:
            return Direction.NONE


class Tile:
    def __init__(self, tile_type=TileType.NOTHING, direction=Direction.NONE):
        self.direction = direction
        self.tile_type = tile_type

    def __str__(self):
        if self.tile_type == TileType.NOTHING:
            return '.'
        elif self.tile_type == TileType.CARROT:
            return 'C'
        elif self.tile_type == TileType.EARTH:
            return 'X'
        elif self.tile_type == TileType.RABBIT:
            if self.direction == Direction.RIGHT:
                return 'E'
            elif self.direction == Direction.LEFT:
                return '3'
            else:
                return '?'
        else:
            return '?'

    @staticmethod
    def from_str(s: str):
        if s == '.':
            return Tile()
        elif s == 'C':
            return Tile(TileType.CARROT)
        elif s == 'X':
            return Tile(TileType.EARTH)
        elif s == 'E':
            return Tile(TileType.RABBIT, Direction.RIGHT)
        elif s == '3':
            return Tile(TileType.RABBIT, Direction.LEFT)
        else:
            raise Exception('Unknown tile {}'.format(s))
