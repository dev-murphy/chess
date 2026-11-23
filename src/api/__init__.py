from engine import ChessBoard

class ChessAPI:
    def __init__(self, id: str):
        self.id = id
        self.board = ChessBoard()

    def game_status(self):
        if self.board.is_checkmate():
            return "checkmate"

        if self.board.is_stalemate():
            return "stalemate"

        return "active" 
        
    def make_move(self, from_square: int, to_square: int, promotion_type: int):
        is_valid = self.board.make_move(from_square, to_square, promotion_type)
        return {
          "valid_move": is_valid,
          "state": self.to_json()
        }

    def reset_game(self):
        return self.board.reset_to_starting_position()

    def to_json(self):
        color = 0 if self.board.side_to_move == "white" else 1

        last_move = None
        if self.board.move_log:
            last = self.board.move_log[-1]
            last_move = {
              "from": list(divmod(last.from_square,8)),
              "to": list(divmod(last.to_square, 8))
            }

        return {
            "game_id": self.id,
            "turn": self.board.side_to_move,
            "status": self.game_status(),
            "in_check": self.board.is_in_check(color),
            "legal_moves": self.board.get_legal_moves(color),
            "last_move": last_move,
            "board": self.board.to_board_array(),
            "side_to_move": self.board.side_to_move
        }