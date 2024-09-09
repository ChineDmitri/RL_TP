# init game tictaktoe for RL
def init_game_tictaktoe():
    board = [
        [
            '' for _ in range(3)
        ] for _ in range(3)
    ]

    return board


game = init_game_tictaktoe()
print(game)