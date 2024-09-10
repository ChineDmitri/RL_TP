import random

from morpion import TicTacToe


def opponent_random(game: TicTacToe) -> int:
    allowed_moves = game.allowed_moves()
    game.play(random.choice(allowed_moves))
    # return random.choice(allowed_moves)

def opponent_next(game: TicTacToe) -> int:
    allowed_moves = game.allowed_moves()
    
    # Vérifier si on peut gagner
    for move in allowed_moves:
        game.play(move)
        if game.has_winner():
            # game.undo((move-1)//3, (move-1)%3)
            return
        game.undo((move-1)//3, (move-1)%3)
    
    # Vérifier si on doit bloquer l'adversaire
    game.currentPlayer = not game.currentPlayer  # Simuler le tour de l'adversaire
    for move in allowed_moves:
        game.play(move)
        if game.has_winner():
            game.undo((move-1)//3, (move-1)%3)
            # game.currentPlayer = not game.currentPlayer  # Rétablir le joueur actuel
            game.play(move)
            return
        game.undo((move-1)//3, (move-1)%3)
    # game.currentPlayer = not game.currentPlayer  # Rétablir le joueur actuel
    
    game.play(random.choice(allowed_moves))
    # Sinon, jouer au hasard
    # return random.choice(allowed_moves)

def play_game():
    game = TicTacToe()
    opponent_random(game)
    while not game.has_winner():
        opponent_next(game)
        print(f"Joueur {'X' if game.currentPlayer else 'O'} jeu...")
        print(game)
        print("==============")
        opponent_random(game)

    print(f"Joueur {'X' if game.currentPlayer else '0'} gagne!")    
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