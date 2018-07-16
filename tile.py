class Tile(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._next_tile = None
        self._has_transport = False

    def __repr__(self):
        return "Tile(%s, %s))" % (self.x, self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def next_tile(self):
        return self._next_tile

    @next_tile.setter
    def next_tile(self, value):
        self._next_tile = value

    @property
    def has_transport(self):
        return self._has_transport

    @has_transport.setter
    def has_transport(self, value):
        self._has_transport = value
