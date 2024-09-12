import random

from morpion_v2 import TicTacToe


def opponent_random(game: TicTacToe) -> int:
    allowed_moves = game.allowed_moves()
    game.play(random.choice(allowed_moves))
    game.next_player()
    # return random.choice(allowed_moves)


def opponent_next(game: TicTacToe) -> bool:
    allowed_moves = game.allowed_moves()
    if len(allowed_moves) == 0:
        print("MATCH NULL")
        return None

    # Vérifier si on peut gagner
    for move in allowed_moves:
        game.play(move)
        if game.has_winner():
            # game.undo((move-1)//3, (move-1)%3)
            return game.currentPlayer
        game.undo((move-1)//3, (move-1) % 3)

    # Vérifier si on doit bloquer l'adversaire
    game.next_player()  # Simuler le tour de l'adversaire
    for move in allowed_moves:
        # Je change joueur
        # Je jeux avec lui et je reviens sur moi
        game.play(move)
        # game.currentPlayer = not game.currentPlayer
        # je verifie si il a gagné
        if game.has_winner():
            # si il a gagné je fait undo et je revien sur moi
            game.undo((move-1)//3, (move-1)%3)
            # game.currentPlayer = not game.currentPlayer  # Rétablir le joueur actuel
            game.next_player() # revenir sur le joueur actuel
            game.play(move)
            game.next_player()
            return game.currentPlayer
        # game.currentPlayer = not game.currentPlayer
        game.undo((move-1)//3, (move-1) % 3)
    # game.currentPlayer = not game.currentPlayer  # Rétablir le joueur actuel

    game.next_player() # revenir sur le joueur actuel
    game.play(random.choice(allowed_moves))
    game.next_player()
    return game.currentPlayer
    # Sinon, jouer au hasard
    # return random.choice(allowed_moves)


def play_game():
    game = TicTacToe()
    print(f"Joueur {'X' if game.currentPlayer else 'O'} jeu...", game.currentPlayer)
    opponent_random(game)
    print(game)
    print("==============")
    while not game.has_winner():
      print(f"Joueur {'X' if game.currentPlayer else 'O'} jeu...", game.currentPlayer)
      opponent_next(game)
      print(game)
      print("==============")

    print(f"Joueur {'O' if game.currentPlayer else 'X'} gagne!")
    # game.play(move)
    # print(f"Joueur {'X' if game.currentPlayer else 'O'} joue {move}")
    # print(game)

    # if game.has_winner():
    #     print(f"Joueur {'O' if game.currentPlayer else 'X'} gagne!")
    #     break
    # elif game.is_draw():
    #     print("Match nul!")
    #     break


# Faire jouer les deux IA ensemble
print("Partie entre opponent_random (X) et opponent_next (O):")
play_game()
