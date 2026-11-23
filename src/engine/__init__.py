from collections import Counter

from .bitboard import Bitboard, SQ, RANK_2, RANK_7, FILE_A, FILE_H
from .move_generator import CASTLING_RIGHTS_MASK, KNIGHT_ATTACKS, KING_ATTACKS, MoveGenerator
from .move import Move

PIECE_MAPS =["PNBRQK","pnbrqk"]
PROMOTION_PIECES = "nbrq"

# Squares where (rank + file) is even, i.e. a1, c1, ... (the dark squares)
DARK_SQUARES = sum(1 << sq for sq in range(64) if (sq // 8 + sq % 8) % 2 == 0)

# Game status values returned by `get_game_status`
ACTIVE = "active"
CHECKMATE = "checkmate"
STALEMATE = "stalemate"
DRAW = "draw"

# Reasons for a draw (other than stalemate)
INSUFFICIENT_MATERIAL = "insufficient_material"
THREEFOLD_REPETITION = "threefold_repetition"
FIFTY_MOVE_RULE = "fifty_move_rule"

class ChessBoard:
    def __init__(self):
        """
        Initialise a dictionary for the pieces bitboard following FEN notation.
        [lowercase = Black, uppercase = White]
        p = Pawn, r = Rook, b = Bishop, n = Knight, q = Queen, k = King
        """
        self.pieces = {
            "p": 0,
            "r": 0,
            "b": 0,
            "n": 0,
            "q": 0,
            "k": 0,
            "P": 0,
            "R": 0,
            "B": 0,
            "N": 0,
            "Q": 0,
            "K": 0,
        }

        # Initialize the occupancy bitboard
        self.white_occupied = 0
        self.black_occupied = 0
        self.all_occupied = 0

        # Special move flags
        self.en_passant_sq = None
        self.castling_rights = 0b1111

        # Implement side to move
        self.side_to_move = "white"

        # Move log
        self.move_log = []

        # Draw tracking: half-moves since the last capture or pawn move
        # and how many times each position has occurred
        self.halfmove_clock = 0
        self.position_history: Counter = Counter()

        # Reset to starting position
        self.reset_to_starting_position()

    def white_pieces(self):
        return [
            self.pieces["P"],
            self.pieces["N"],
            self.pieces["B"],
            self.pieces["R"],
            self.pieces["Q"],
            self.pieces["K"],
        ]

    def black_pieces(self):
        return [
            self.pieces["p"],
            self.pieces["n"],
            self.pieces["b"],
            self.pieces["r"],
            self.pieces["q"],
            self.pieces["k"],
        ]

    def reset_to_starting_position(self):
        self.move_log = []
        self.castling_rights = 0b1111
        self.en_passant_sq = None
        self.side_to_move = "white"
        
        self.pieces["p"] = RANK_7
        self.pieces["r"] = (1 << SQ["A8"]) | (1 << SQ["H8"])
        self.pieces["n"] = (1 << SQ["B8"]) | (1 << SQ["G8"])
        self.pieces["b"] = (1 << SQ["C8"]) | (1 << SQ["F8"])
        self.pieces["q"] = 1 << SQ["D8"]
        self.pieces["k"] = 1 << SQ["E8"]

        self.pieces["P"] = RANK_2
        self.pieces["R"] = (1 << SQ["A1"]) | (1 << SQ["H1"])
        self.pieces["N"] = (1 << SQ["B1"]) | (1 << SQ["G1"])
        self.pieces["B"] = (1 << SQ["C1"]) | (1 << SQ["F1"])
        self.pieces["Q"] = 1 << SQ["D1"]
        self.pieces["K"] = 1 << SQ["E1"]

        self.update_occupancies()

        self.halfmove_clock = 0
        self.position_history = Counter({self.position_key(): 1})
        
    def update_occupancies(self):
        self.white_occupied = 0
        for b in self.white_pieces():
            self.white_occupied |= b

        self.black_occupied = 0
        for b in self.black_pieces():
            self.black_occupied |= b

        self.all_occupied = self.white_occupied | self.black_occupied

    def get_piece_at(self, sq: int) -> tuple[int, int] | tuple[None, None]:
        """ Returns the pieces at the specific squares """
        mask = 1 << sq
        for piece_type, bitboard in enumerate(self.white_pieces()):
            if bitboard & mask: return (0, piece_type)

        for piece_type, bitboard in enumerate(self.black_pieces()):
            if bitboard & mask: return (1, piece_type)

        return (None, None)

    """ MOVE VALIDATION CHECKS """

    def is_square_attacked(self, sq: int, attacker_color: int) -> bool:
        """ Checks if square is being attacked by enemy piece """
        attacker_pieces = self.white_pieces() if attacker_color == 0 else self.black_pieces()

        # Check Knight attacks back from sq
        if KNIGHT_ATTACKS[sq] & attacker_pieces[1]:
            return True

        # Check King attacks back from sq
        if KING_ATTACKS[sq] & attacker_pieces[5]:
            return True

        pawn_mask = 1 << sq
        if attacker_color == 0:
            if ((pawn_mask >> 7) & ~FILE_A & attacker_pieces[0]) or \
               ((pawn_mask >> 9) & ~FILE_H & attacker_pieces[0]):
                  return True
        else:
            if ((pawn_mask << 7) & ~FILE_H & attacker_pieces[0]) or \
               ((pawn_mask << 9) & ~FILE_A & attacker_pieces[0]):
                  return True

        # Check sliding pieces attacks back from square
        bishop_queen_attacks = MoveGenerator.get_sliding_attacks(sq, 2, self.all_occupied)
        if bishop_queen_attacks & (attacker_pieces[2] | attacker_pieces[4]):
            return True

        rook_queen_attacks = MoveGenerator.get_sliding_attacks(sq, 3, self.all_occupied)
        if rook_queen_attacks & (attacker_pieces[3] | attacker_pieces[4]):
            return True

        return False

    def is_in_check(self, color: int) -> bool:
        """ Check if the king of (white|black) is currently in check """
        king_bitboard = self.white_pieces()[5] if color == 0 else self.black_pieces()[5]
        if king_bitboard == 0:
            return False
        king_square, _ = Bitboard.pop_lsb(king_bitboard)
        enemy_color = 1 if color == 0 else 0
        return self.is_square_attacked(king_square, enemy_color)

    def force_move(self, from_square: int, to_square: int, promotion_type: int):
        """ Unconditionally update bitboard without validating check rules """
        color, piece_type = self.get_piece_at(from_square)
        if color is None or piece_type is None: return

        own_pieces = PIECE_MAPS[0] if color == 0 else PIECE_MAPS[1]
        enemy_pieces = PIECE_MAPS[1] if color == 0  else PIECE_MAPS[0]
        own_piece = own_pieces[piece_type]

        from_mask = 1 << from_square
        to_mask = 1 << to_square

        # Check if there is an enemy piece and add it to move log
        c, p_t = self.get_piece_at(to_square)
        enemy_piece = None
        if (c is not None or c != color) and p_t is not None:
            enemy_piece = enemy_pieces[p_t]

        for enemy_type in range(6):
            self.pieces[enemy_pieces[enemy_type]] &= ~to_mask

        # En passant capture
        if piece_type == 0 and to_square == self.en_passant_sq:
            captured_pawn_sq = to_square - 8 if color == 0 else to_square + 8
            enemy_piece = enemy_pieces[piece_type]
            self.pieces[enemy_pieces[piece_type]] &= ~(1 << captured_pawn_sq)

        # Promotion 
        self.pieces[own_pieces[piece_type]] &= ~from_mask
        is_promotion = (piece_type == 0) and (to_square >= 56 or to_square <= 7)
        if is_promotion:
            promo = PROMOTION_PIECES[promotion_type]
            promo = promo.upper() if color == 0 else promo
            self.pieces[promo] |= to_mask
        else:
            self.pieces[own_pieces[piece_type]] |= to_mask

        if piece_type == 5 and abs(to_square - from_square) == 2:
            # White Kingside
            if to_square == SQ["G1"]:
                self.pieces[own_pieces[3]] ^= (1 << SQ["H1"]) | (1 << SQ["F1"])
            elif to_square == SQ["C1"]:
                self.pieces[own_pieces[3]] ^= (1 << SQ["A1"]) | (1 << SQ["D1"])
            elif to_square == SQ["G8"]:
                self.pieces[own_pieces[3]] ^= (1 << SQ["H8"]) | (1 << SQ["F8"])
            elif to_square == SQ["C8"]:
                self.pieces[own_pieces[3]] ^= (1 << SQ["A8"]) | (1 << SQ["D8"])

        if piece_type == 0 and abs(to_square - from_square) == 16:
            self.en_passant_sq = (from_square + to_square) // 2
        else:
            self.en_passant_sq = None

        self.castling_rights &= CASTLING_RIGHTS_MASK[from_square]
        self.castling_rights &= CASTLING_RIGHTS_MASK[to_square]

        # Fifty-move rule: any pawn move or capture resets the clock
        if piece_type == 0 or enemy_piece is not None:
            self.halfmove_clock = 0
        else:
            self.halfmove_clock += 1

        self.move_log.append(Move(from_square, to_square, own_piece, enemy_piece))
        self.update_occupancies()
        
    def is_valid_move(self, from_square: int, to_square: int) -> bool:
        """
        Validates if move from `from_square` to `to_square` is completely legal:
          1. Validates pseudo-legality (piece mechanics).
          2. Simulates move to ensure King is not exposed to check.
        """
        color, piece_type = self.get_piece_at(from_square)
        current_color = 0 if self.side_to_move == "white" else 1

        # Not this piece's turn
        if color != current_color or piece_type is None:
            return False

        # 1. Pseudo-legal check
        pseudo_moves = MoveGenerator.get_pseudo_legal_moves(self, from_square)
        if not (pseudo_moves & (1 << to_square)):
            return False

        own_pieces = PIECE_MAPS[0] if color == 0 else PIECE_MAPS[1]
        enemy_pieces = PIECE_MAPS[1] if color == 0 else PIECE_MAPS[0]

        from_mask = 1 << from_square
        to_mask = 1 << to_square
        move_mask = from_mask | to_mask

        # Check if an enemy piece is captured on square
        captured_type = None
        captured_mask = to_mask
        if piece_type == 0 and to_square == self.en_passant_sq:
            captured_type = 0
            captured_mask = 1 << (to_square - 8 if color == 0 else to_square + 8)
        else:
            for enemy_type in range(6):
                if self.pieces[enemy_pieces[enemy_type]] & to_mask:
                    captured_type = enemy_type
                    break

        # MAKE MOVE-IN-PLACE 
        self.pieces[own_pieces[piece_type]] ^= move_mask
        if captured_type is not None:
            self.pieces[enemy_pieces[captured_type]] ^= captured_mask
        self.update_occupancies()

        in_check = self.is_in_check(current_color)

        self.pieces[own_pieces[piece_type]] ^= move_mask
        if captured_type is not None:
            self.pieces[enemy_pieces[captured_type]] ^= captured_mask
            
        self.update_occupancies()
        return not in_check

    def make_move(self, from_square: int, to_square: int, promotion_type: int):
        """ Execute move if valid and toggle turn. Return True on success. """
        if self.is_game_over():
            return False
        if not self.is_valid_move(from_square, to_square):
            return False
        self.force_move(from_square, to_square, promotion_type)
        self.side_to_move = "black" if self.side_to_move == "white" else "white"
        self.position_history[self.position_key()] += 1
        return True
    
    def get_legal_moves(self, color: int) -> dict[str, list[list[int]]]:
        """ Returns all legal moves for `color` formatted for Vue: {'row,col': [[to_r, to_c], ...]} """
        legal_moves = {}
        own_pieces = self.white_pieces() if color == 0 else self.black_pieces()

        # Loop over all of the 6 piece types (Pawn, Rook, Bishop, Knight, Queen, King)
        for piece_type in range(6):
            bitboard = own_pieces[piece_type]

            # Pop each piece of this type from its bitboard 
            while bitboard:
                from_square, bitboard = Bitboard.pop_lsb(bitboard)
                from_r, from_c = divmod(from_square, 8)

                # Get all pseudo-legal target squares for this piece
                pseudo_moves = MoveGenerator.get_pseudo_legal_moves(self, from_square)
                valid_targets = []

                # Test each square until we find ONE legal move
                while pseudo_moves:
                    to_square, pseudo_moves = Bitboard.pop_lsb(pseudo_moves)
                    if self.is_valid_move(from_square, to_square):
                        to_r, to_c = divmod(to_square, 8)
                        valid_targets.append([to_r, to_c])

                if valid_targets:
                    legal_moves[f"{from_r},{from_c}"] = valid_targets

        return legal_moves

    def is_checkmate(self) -> bool:
        """ Return True if the current color is in check and has no legal moves. """
        current_color = 0 if self.side_to_move == "white" else 1
        return self.is_in_check(current_color) and not bool(self.get_legal_moves(current_color))
    
    def is_stalemate(self) -> bool:
        """ Return True if the current color is not in check and no legal moves. """
        current_color = 0 if self.side_to_move == "white" else 1
        return not self.is_in_check(current_color) and not bool(self.get_legal_moves(current_color))

    """ DRAW RULES """

    def _can_capture_en_passant(self) -> bool:
        """ True if the side to move has a legal en passant capture available """
        if self.en_passant_sq is None:
            return False

        ep = self.en_passant_sq
        white_to_move = self.side_to_move == "white"
        pawns = self.pieces["P"] if white_to_move else self.pieces["p"]

        # Squares a capturing pawn could stand on (left and right of the target file)
        candidates = []
        if ep % 8 != 0:
            candidates.append(ep - 9 if white_to_move else ep + 7)
        if ep % 8 != 7:
            candidates.append(ep - 7 if white_to_move else ep + 9)

        return any(
            0 <= sq < 64 and pawns & (1 << sq) and self.is_valid_move(sq, ep)
            for sq in candidates
        )

    def position_key(self) -> tuple:
        """
        Identify a position for threefold repetition: piece placement, side to move,
        castling rights and en passant (only if a capture is actually possible).
        """
        ep = self.en_passant_sq if self._can_capture_en_passant() else None
        return (self.to_fen_board(), self.side_to_move, self.castling_rights, ep)

    def is_threefold_repetition(self) -> bool:
        """ Return True if the current position has occurred at least three times """
        return self.position_history[self.position_key()] >= 3

    def is_fifty_move_rule(self) -> bool:
        """ Return True if 50 moves by each side passed without a capture or pawn move """
        return self.halfmove_clock >= 100

    def is_insufficient_material(self) -> bool:
        """
        Return True if neither side can possibly checkmate:
          - King vs King
          - King + Bishop vs King, King + Knight vs King
          - Kings and bishops only, with every bishop on the same square color
        """
        white, black = self.white_pieces(), self.black_pieces()

        # Any pawn, rook or queen means mate is still possible
        if any(side[t] for side in (white, black) for t in (0, 3, 4)):
            return False

        knights = white[1] | black[1]
        bishops = white[2] | black[2]
        minor_count = knights.bit_count() + bishops.bit_count()

        # K vs K, or a single minor piece on the board
        if minor_count <= 1:
            return True

        # Only bishops left, all on the same color squares
        if knights == 0:
            return bishops & DARK_SQUARES == 0 or bishops & ~DARK_SQUARES == 0

        return False

    def get_game_status(self) -> tuple[str, str | None]:
        """
        Return (status, draw_reason).
        status is one of: active, checkmate, stalemate, draw.
        draw_reason is set only when status is draw.
        """
        current_color = 0 if self.side_to_move == "white" else 1

        if not self.get_legal_moves(current_color):
            return (CHECKMATE, None) if self.is_in_check(current_color) else (STALEMATE, None)

        if self.is_insufficient_material():
            return DRAW, INSUFFICIENT_MATERIAL

        if self.is_threefold_repetition():
            return DRAW, THREEFOLD_REPETITION

        if self.is_fifty_move_rule():
            return DRAW, FIFTY_MOVE_RULE

        return ACTIVE, None

    def is_game_over(self) -> bool:
        return self.get_game_status()[0] != ACTIVE

    def to_fen_board(self):
        rows = []
        for rank in range(7, -1, -1):
            row, empty = "", 0
            for file in range(8):
                color, piece_type = self.get_piece_at(rank * 8 + file)
                if color is None or piece_type is None:
                    empty += 1
                    continue
                if empty:
                    row += str(empty)
                    empty = 0
                row += PIECE_MAPS[color][piece_type]
            if empty: 
                row += str(empty)
            rows.append(row)
        return "/".join(rows)

    def to_board_array(self):
        board_arr = ["."] * 64
        for sq in range(64):
            color, piece_type = self.get_piece_at(sq)
            if piece_type is not None and color is not None:
                board_arr[sq] = PIECE_MAPS[color][piece_type]
        return board_arr
    
    def display(self):
        """ Prints the complete chess board with unicode character """
        symbols = {
            (0, 0): "♙", (0, 1): "♘", (0, 2): "♗", (0, 3): "♖", (0, 4): "♕", (0, 5): "♔",
            (1, 0): "♟", (1, 1): "♞", (1, 2): "♝", (1, 3): "♜", (1, 4): "♛", (1, 5): "♚"
        }
        grid = [["." for _ in range(8)] for _ in range(8)]
        for color, pieces in [(1,self.black_pieces()), (0, self.white_pieces())]:
            for piece_type, bitboard in enumerate(pieces):
                temp_bitboard = bitboard
                while temp_bitboard:
                    sq, temp_bitboard = Bitboard.pop_lsb(temp_bitboard)
                    rank, file = sq // 8, sq % 8
                    grid[rank][file] = symbols[(color, piece_type)]
                  
        print("\n  +-----------------+")
        for rank in range(7, -1, -1):
            print(f"{rank + 1} | " + " ".join(grid[rank]))
        print("  +-----------------+")
        print("    a b c d e f g h\n")