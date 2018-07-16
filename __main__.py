from game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        game.use_turn()
        print(game)
