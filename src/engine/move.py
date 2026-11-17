from .bitboard import SQUARES

class Move:
  def __init__(self, from_square: int, to_square: int, own_piece: str, enemy_piece: str | None):
      self.from_square = from_square
      self.to_square = to_square
      self.own_piece = own_piece
      self.enemy_piece = enemy_piece

  def get_rank_and_file(self):
      return [SQUARES[self.from_square], SQUARES[self.to_square]]

  def chess_notation(self):
      piece = self.own_piece.upper()
      from_name, to_name = (s.lower() for s in self.get_rank_and_file())
      prefix = "" if piece == "P" else piece
      if self.enemy_piece is None:
          return f"{prefix}{to_name}"
      return f"{from_name[0] if piece == 'P' else prefix}x{to_name}"
      
  def __str__(self):
    return f"{self.get_rank_and_file()[0]} -> {self.get_rank_and_file()[1]}, {self.own_piece} {self.enemy_piece}"
  