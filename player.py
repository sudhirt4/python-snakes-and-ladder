from minion import Minion


class Player(object):
    def __init__(self, id):
        self._id = id
        self._minions = Player.generate_minions()

    @property
    def id(self):
        return self._id

    @property
    def minions(self):
        return self._minions

    @staticmethod
    def generate_minions():
        return tuple(Minion(id) for id in range(1, 5))
