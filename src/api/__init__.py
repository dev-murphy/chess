from engine import ChessBoard, ACTIVE, CHECKMATE


class ChessAPI:
    def __init__(self, id: str):
        self.id = id
        self.board = ChessBoard()

    def game_status(self):
        status, _ = self.board.get_game_status()
        return status

    def make_move(self, from_square: int, to_square: int, promotion_type: int):
        is_valid = self.board.make_move(from_square, to_square, promotion_type)
        return {
          "valid_move": is_valid,
          "state": self.to_json()
        }

    def reset_game(self):
        self.board.reset_to_starting_position()
        return self.to_json()

    def to_json(self):
        color = 0 if self.board.side_to_move == "white" else 1
        status, draw_reason = self.board.get_game_status()

        # The side that just moved wins on checkmate
        winner = None
        if status == CHECKMATE:
            winner = "black" if self.board.side_to_move == "white" else "white"

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
            "status": status,
            "draw_reason": draw_reason,
            "winner": winner,
            "in_check": self.board.is_in_check(color),
            "legal_moves": self.board.get_legal_moves(color) if status == ACTIVE else {},
            "last_move": last_move,
            "board": self.board.to_board_array(),
            "side_to_move": self.board.side_to_move
        }
