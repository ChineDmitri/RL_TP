from morpion import TicTacToe
import random


game = TicTacToe()


game.play(2)
game.play(5)
game.play(5)

print(game)


def opponent_random(game: TicTacToe):
    moves = game.allowed_moves()
    game.play(moves[random.randint(0, moves.size)])


def opponent_next(game: TicTacToe):
    for move in range(1, 10):
        if game.play(move):
            if game.has_winner() == game.currentPlayer:
                return
            game.undo_move(move)

    for move in range(1, 10):
        if game.is_move_allowed(move):
            game.play(move)
            if game.check_winner() == game.opponent_player:
                game.undo_move(move)
                game.play(move)
                return
            game.undo_move(move)

    opponent_random(game)
