from tile import Tile
from transport import Snake, Ladder


class Board(object):
    X_SIZE = 10
    Y_SIZE = 10
    NO_OF_SNAKES = 2
    NO_OF_LADDERS = 2

    def __init__(self):
        self._tiles = Board.generate_tiles()
        self._snakes = Board.generate_snakes()
        self._ladders = Board.generate_ladders()
        self.add_snakes_to_tiles()
        self.add_ladders_to_tiles()

    def __repr__(self):
        return "Board(); \n\n Snakes:{}, \n\n Tiles:{}".format(self.snakes, self.tiles)

    @property
    def tiles(self):
        return self._tiles

    @property
    def snakes(self):
        return self._snakes

    @property
    def ladders(self):
        return self._ladders

    def add_transports(self, transports):
        for transport in transports:
            start_tile = self.tiles[(transport.start_position['x'], transport.start_position['y'])]
            end_tile = self.tiles[(transport.end_position['x'], transport.end_position['y'])]
            start_tile.next_tile = end_tile
            start_tile.has_transport = True

    def add_snakes_to_tiles(self):
        self.add_transports(self.snakes)

    def add_ladders_to_tiles(self):
        self.add_transports(self.ladders)

    @staticmethod
    def generate_tiles():
        dx = 1
        x = 0
        y = 0
        tiles = {}
        prev_tile = None
        while not (x == 0 and y == Board.Y_SIZE):
            new_tile = Tile(x, y)
            tiles[(x, y)] = new_tile
            if prev_tile:
                prev_tile.next_tile = new_tile
            prev_tile = new_tile
            x += dx
            if x < 0 or x > Board.X_SIZE - 1:
                dx *= -1
                y += 1
            if x < 0:
                x = 0
            if x > Board.X_SIZE - 1:
                x = Board.X_SIZE - 1
        return tiles

    @staticmethod
    def generate_snakes():
        snakes = []
        for id in range(0, Board.NO_OF_SNAKES):
            start_position, end_position = Snake.generate_positions(Board.X_SIZE, Board.Y_SIZE)
            snakes.append(Snake(id, start_position, end_position))
        return tuple(snakes)

    @staticmethod
    def generate_ladders():
        ladders = []
        for id in range(0, Board.NO_OF_LADDERS):
            start_position, end_position = Ladder.generate_positions(Board.X_SIZE, Board.Y_SIZE)
            ladders.append(Ladder(id, start_position, end_position))
        return tuple(ladders)
