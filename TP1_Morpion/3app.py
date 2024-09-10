from morpion import TicTacToe
import random

def opponent_random(game: TicTacToe):
  allowed_moves = game.allowed_moves()
  game.play(random.choice(allowed_moves))

def opponent_next(game: TicTacToe):
  allowed_moves = game.allowed_moves()

  # Vérifier si l'adersaire peut gagner
  for move in allowed_moves:
    row = (move-1) // 3
    col = (move-1) % 3

    # Simuler le coup de l'adversaire
    game._board[row][col] = not game.currentPlayer
    if game.has_winner():
      game.undo(row, col)
      return move

    game.undo(row, col)


  # Bloquer le jouer actuel s'il peut gagner
  for move in allowed_moves:
    row = (move-1) // 3
    col = (move-1) % 3

    game._board[row][col] = game.currentPlayer
    if game.has_winner():
      game.undo(row, col)
      return move
    
    game.undo(row, col)

  return random.choice(allowed_moves)

def play_game():
    game = TicTacToe()
    currentPlayer = True  # True: X joue en premier

    print("Début du jeu:")
    print(game)

    while not game.has_winner() and not game.is_draw():
        if currentPlayer:
            print("\nJoueur X (IA) joue:")
            move = opponent_next(game)  # Joueur X joue
            game.play(move)
        else:
            print("\nJoueur O (IA) joue:")
            move = opponent_next(game)  # Joueur O joue
            game.play(move)

        print(game)
        currentPlayer = not currentPlayer  # Changement de joueur

    if game.has_winner():
        winner = "X" if not currentPlayer else "O"  # Le joueur actuel est inversé à la fin
        print(f"\nLe joueur {winner} a gagné!")
    else:
        print("\nMatch nul!")

# Démarrer la partie entre deux IA
play_game()