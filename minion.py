class Minion(object):
    def __init__(self, id):
        self._id = id
        self._x = -1
        self._y = 0
        self._is_completed = False

    def __repr__(self):
        return "Minion({})".format(id)

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    @property
    def is_completed(self):
        return self._is_completed

    @is_completed.setter
    def is_completed(self, val):
        self._is_completed = val
