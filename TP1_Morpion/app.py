from morpion import TicTacToe
import random

# Implémentez une fonction opponent_random qui prend en argument une instance de TicTacToe
# et joue un coup au hasard parmi ceux autorisés.
def opponent_random(game: TicTacToe):
    moves = game.allowed_moves()
    # print("Posbile moves: ", len(moves))
    # print(moves)
    game.play(moves[random.randint(0, len(moves)-1)])


# Implémentez une fonction opponent_next qui choisi parmi les coups autorisés. Il choisit en
# priorité un coup qui le fait gagner. Si elle ne peut pas gagner, elle joue préférentiellement un
# coup qui empêche l’adversaire de gagner. Sinon, elle joue au hasard.
def opponent_next(game: TicTacToe):
    for move in range(1, 10):
        if game.play(move):
            if game.has_winner() == game.currentPlayer:
                return
            game.undo(move)

    for move in range(1, 10):
        if move in game.allowed_moves():
            game.play(move)
            if game.has_winner() != game.currentPlayer:
                return

    opponent_random(game)

game = TicTacToe()

print("-- game started")
print(game)
print("==============")

while not game.has_winner() and not game.is_draw():
    opponent_random(game)
    print(game)
    if game.has_winner() or game.is_draw():
        break
    print("==============")

# Affichage du résultat final
if game.has_winner():
    print("Nous avons un gagnant!")
else:
    print("C'est un match nul!")


