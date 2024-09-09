class TicTacToe:
  def __init__(self):
    board = [
        [
            None for _ in range(3)
        ] for _ in range(3)
    ]

    self._player = True  # True : X; False : O

    self._board = board

# =================================================================

  def play(self, number: int):
    if number < 1 or number > 9:
      print("La case est hors de la grille")
      return

    row = (number - 1) // 3  # Ligne
    col = (number - 1) % 3   # Colonne

    if self._board[row][col] is not None:
      print("Cette case est déjà occupée")

    else:
      self._board[row][col] = self._player
      self._player = not self._player

# =================================================================

  def __str__(self):
      return '\n'.join(
          [
              ' '.join(
                  [self.display_value(cell) for cell in row]
              )
              for row in self._board
          ]
      )

  def display_value(self, cell):
    if cell is None:
        return '.'
    return 'X' if cell else 'O'

  def undo(row: int, column: int):
    self._board[row][column] = ""

  def has_winner():
    return True

  def is_draw():
    print("Match nul")
