import random


from itertools import chain
from board import Board
from player import Player


class Game(object):
    NO_OF_PLAYERS = 4

    def __init__(self):
        self._board = Board()
        self._players = Game.generate_players()
        self._current_turn_player_id = 0
        self._current_roll = 0

    def __repr__(self):
        op_string = ""
        for y in reversed(range(0, Board.Y_SIZE)):
            for x in range(0, Board.X_SIZE):
                op_string += self.tile_to_rowstring(self.board.tiles[(x, y)])
            op_string += "\n"
        return op_string

    @property
    def board(self):
        return self._board

    @property
    def players(self):
        return self._players

    @property
    def current_roll(self):
        return self._current_roll

    @current_roll.setter
    def current_roll(self, value):
        self._current_roll = value

    @property
    def current_turn_player(self):
        return self.players[self._current_turn_player_id]

    def update_turn(self):
        self._current_turn_player_id += 1
        if self._current_turn_player_id > Game.NO_OF_PLAYERS - 1:
            self._current_turn_player_id = 0

    def roll_dice(self):
        roll = random.randint(1, 6)
        current_player = self.current_turn_player
        self.current_roll = roll
        print("Player %d rolled %s" % (current_player.id, roll))

    def get_input_minion(self):
        current_player = self.current_turn_player
        print("Player %d : Which minion do you want to move ?" % current_player.id)
        try:
            minion_id = int(input())
            minion = current_player.minions[minion_id]
            if minion is None:
                raise ValueError("BOom")
            if minion.is_completed:
                raise ValueError("Minion already completed")
        except (ValueError, IndexError):
            print("Invalid input; Please try again.")
            return self.get_input_minion()
        return minion

    def move_minion(self, minion):
        step = self.current_roll
        if minion.x == -1:
            minion.x = 0
        current_tile = self.board.tiles[(minion.x, minion.y)]
        for _ in range(0, step):
            next_tile = current_tile.next_tile
            if next_tile is None:
                minion.is_completed = True
                self.update_turn()
                return
            current_tile = next_tile

        minion.x = current_tile.x
        minion.y = current_tile.y

    def use_turn(self):
        self.roll_dice()
        minion = self.get_input_minion()
        print("User selected minion %s", str(minion.id))
        self.move_minion(minion)
        self.update_turn()

    def tile_to_rowstring(self, tile):
        player_minions = []
        for player in self.players:
            for minion in player.minions:
                if minion.x == tile.x and minion.y == tile.y:
                    player_minions.append({
                        'minion': minion,
                        'player': player
                    })
        tile_string = ''.join("%s:%s " % (pm['player'].id, pm['minion'].id) for pm in player_minions)
        if tile.has_transport:
            return "T(%s%s)" % (tile.next_tile.x, tile.next_tile.y)
        return "( %s ) \t" % tile_string

    @staticmethod
    def generate_players():
        return tuple(Player(id) for id in range(0, Game.NO_OF_PLAYERS))


