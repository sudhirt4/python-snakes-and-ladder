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


class Snake(Transport):
    pass


class Ladder(Transport):
    pass
