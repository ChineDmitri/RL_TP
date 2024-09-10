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
# def opponent_next(game: TicTacToe):
#     for move in range(1, 10):
#         if game.play(move):
#             if game.has_winner() == game.currentPlayer:
#                 return
#             game.undo(move)

#     for move in range(1, 10):
#         if move in game.allowed_moves():
#             game.play(move)
#             if game.has_winner() != game.currentPlayer:
#                 return

#     opponent_random(game)


# def opponent_next(game):
#     # 1. Vérifier si l'opposant peut gagner
#     for move in game.allowed_moves():
#         game.play(move)
#         if game.has_winner():
#             game.undo(move)
#             return move
#         game.undo(move)
    
#     # 2. Vérifier si le joueur peut gagner et le bloquer
#     current_player = game.current_player
#     game.current_player = 'X' if current_player == 'O' else 'O'
#     for move in game.allowed_moves():
#         game.play(move)
#         if game.has_winner():
#             game.undo(move)
#             game.current_player = current_player
#             return move
#         game.undo(move)
#     game.current_player = current_player

#     # 3. Si aucune des conditions ci-dessus n'est remplie, jouer au hasard
#     return random.choice(game.allowed_moves())


def opponent_next(game):
    opponent = game.currentPlayer
    player = 'X' if opponent == 'O' else 'O'

    # 1. Vérifier si l'opposant peut gagner
    for move in game.allowed_moves():
        game.play(move)
        if game.has_winner():
            game.undo(move)
            return move
        game.undo(move)
    
    # 2. Vérifier si le joueur peut gagner et le bloquer
    game.current_player = player
    for move in game.allowed_moves():
        game.play(move)
        if game.has_winner():
            game.undo(move)
            game.current_player = opponent
            return move
        game.undo(move)
    game.current_player = opponent

    # 3. Si aucune des conditions ci-dessus n'est remplie, jouer au hasard
    return random.choice(game.allowed_moves())

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


