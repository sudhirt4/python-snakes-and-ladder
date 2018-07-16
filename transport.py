import random


class Transport(object):
    def __init__(self, id, start_position, end_position):
        self._id = id
        self._start_position = start_position
        self._end_position = end_position

    def __repr__(self):
        return "Transport(%s, %s, %s))" % (self._id, self._start_position, self._end_position)

    @property
    def start_position(self):
        return self._start_position

    @property
    def end_position(self):
        return self._end_position

    @staticmethod
    def generate_position(max_x, max_y):
        return {'x': random.randint(0, max_x - 1), 'y': random.randint(0, max_y - 1)}


class Snake(Transport):
    @staticmethod
    def generate_positions(max_x, max_y):
        start_position = Transport.generate_position(max_x, max_y)
        end_position = Transport.generate_position(max_x, max_y)
        if start_position['y'] < end_position['y']:
            return Snake.generate_positions(max_x, max_y)
        return start_position, end_position


class Ladder(Transport):
    @staticmethod
    def generate_positions(max_x, max_y):
        start_position = Transport.generate_position(max_x, max_y)
        end_position = Transport.generate_position(max_x, max_y)
        if start_position['y'] > end_position['y']:
            return Ladder.generate_positions(max_x, max_y)
        return start_position, end_position
