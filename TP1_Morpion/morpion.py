class TicTacToe:
  def __init__(self):
    board = self.create_board()
    self.currentPlayer = True  # True : X; False : O
    self._board = board

# =================================================================
# =================================================================
  def create_board() -> list[list[str]]:
    return [
        [
            None for _ in range(3)
        ] for _ in range(3)
    ]
    
  def reset(self):
    self._board = self.create_board()
    self.currentPlayer = True
# =================================================================
# =================================================================
  def play(self, number: int) -> bool:
    if number < 1 or number > 9:
      print("La case est hors de la grille")
      return False

    row = (number - 1) // 3  # Ligne
    col = (number - 1) % 3   # Colonne

    if self._board[row][col] is not None:
      print("Cette case est déjà occupée")
      return False

    else:
      self._board[row][col] = self.currentPlayer
      self.currentPlayer = not self.currentPlayer
      return False
# =================================================================
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
# =================================================================
# =================================================================
  def display_value(self, cell):
    if cell is None:
        return '.'
    return 'X' if cell else 'O'
# =================================================================
# =================================================================
  def undo(self, row: int, column: int):
    self._board[row][column] = None
# =================================================================
# =================================================================
  def has_winner(self) -> bool:
    last_player = self.currentPlayer

    for row in self._board:
      if row == [last_player, last_player, last_player]: 
        return True
    
    for col in range(3):
      if(self._board[0][col] == last_player and self._board[1][col] == last_player and self._board[2][col] == last_player):
        return True
    
    if(self._board[0][0] == last_player and self._board[1][1] == last_player and self._board[2][2] == last_player):
      return True
    
    if(self._board[0][2] == last_player and self._board[1][1] == last_player and self._board[2][0]):
      return True
    
    return False
# =================================================================
# =================================================================
  def is_draw(self):
    if self.has_winner():
      return False
    
    # Vérifie si existent encore des cases avec None
    for row in self._board:
      if None in row:
        return False
    
    return True
# =================================================================
# =================================================================
  def allowed_moves(self):
    moves = []
    
    for i in range(3):
      for j in range(3):
        if self._board[i][j] is None:
          move_number = i * 3 + j + 1
          moves.append(move_number)

    return moves