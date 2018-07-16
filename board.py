import random

from tile import Tile
from transport import Snake


class Board(object):
    X_SIZE = 10
    Y_SIZE = 10
    NO_OF_SNAKES = 10

    def __init__(self):
        self._tiles = Board.generate_tiles()
        self._snakes = Board.generate_snakes()
        self.add_snakes_to_tiles()

    def __repr__(self):
        return "Board(); \n\n Snakes:{}, \n\n Tiles:{}".format(self.snakes, self.tiles)

    @property
    def tiles(self):
        return self._tiles

    @property
    def snakes(self):
        return self._snakes

    def add_snakes_to_tiles(self):
        for snake in self.snakes:
            start_tile = self.tiles[(snake.start_position['x'], snake.start_position['y'])]
            end_tile = self.tiles[(snake.end_position['x'], snake.end_position['y'])]
            start_tile.next_tile = end_tile
            start_tile.has_snake = True

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
    def generate_position():
        return {'x': random.randint(0, Board.X_SIZE - 1), 'y': random.randint(0, Board.Y_SIZE - 1)}

    @staticmethod
    def generate_snakes():
        snakes = []
        for id in range(0, Board.NO_OF_SNAKES):
            start_position = Board.generate_position()
            end_position = Board.generate_position()
            snakes.append(Snake(id, start_position, end_position))
        return tuple(snakes)
