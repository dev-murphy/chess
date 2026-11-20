from .bitboard import FILE_A, FILE_B, FILE_G, FILE_H, RANK_2, RANK_7, SQ
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.engine import ChessBoard

""" Generate moves for a knight and a king on every position on the board """
KNIGHT_ATTACKS = [0] * 64
KING_ATTACKS = [0] * 64
FULL_BOARD = 0xFFFFFFFFFFFFFFFF

# Castling rights bitmasks
WK_CASTLE = 1  # 0b0001: White Kingside  (O-O)
WQ_CASTLE = 2  # 0b0010: White Queenside (O-O-O)
BK_CASTLE = 4  # 0b0100: Black Kingside  (O-O)
BQ_CASTLE = 8  # 0b1000: Black Queenside (O-O-O)

CASTLING_RIGHTS_MASK = [0b1111] * 64
CASTLING_RIGHTS_MASK[SQ["E1"]] &= ~(WK_CASTLE | WQ_CASTLE)
CASTLING_RIGHTS_MASK[SQ["H1"]] &= ~WK_CASTLE
CASTLING_RIGHTS_MASK[SQ["A1"]] &= ~WQ_CASTLE
CASTLING_RIGHTS_MASK[SQ["E8"]] &= ~(BK_CASTLE | BQ_CASTLE)
CASTLING_RIGHTS_MASK[SQ["H8"]] &= ~BK_CASTLE
CASTLING_RIGHTS_MASK[SQ["A8"]] &= ~BQ_CASTLE

NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST = range(8)
RAY_ATTACKS = [[0] * 64 for _ in range(8)]

class MoveGenerator:
    @staticmethod
    def precomputed_leaper_moves():
        for sq in range(64):
            bitboard = 1 << sq
        
            # Thses are all the possible attacks for the knight to make for a specific square
            # interestingly, the moves are mirrored horizontally
            n_attacks = 0
            n_attacks |= (bitboard & ~FILE_A & ~FILE_B) << 6
            n_attacks |= (bitboard & ~FILE_A) << 15
            n_attacks |= (bitboard & ~FILE_H) << 17
            n_attacks |= (bitboard & ~FILE_G & ~FILE_H) << 10
            n_attacks |= (bitboard & ~FILE_G & ~FILE_H) >> 6
            n_attacks |= (bitboard & ~FILE_H) >> 15
            n_attacks |= (bitboard & ~FILE_A) >> 17
            n_attacks |= (bitboard & ~FILE_A & ~FILE_B) >> 10
            KNIGHT_ATTACKS[sq] = n_attacks & FULL_BOARD
        
            # These are the king moves 
            k_attacks = 0
            k_attacks |= (bitboard & ~FILE_A) << 7
            k_attacks |= bitboard << 8
            k_attacks |= (bitboard & ~FILE_H) << 9
            k_attacks |= (bitboard & ~FILE_H) << 1
            k_attacks |= (bitboard & ~FILE_H) >> 7
            k_attacks |= bitboard >> 8
            k_attacks |= (bitboard & ~FILE_A) >> 9
            k_attacks |= (bitboard & ~FILE_A) >> 1
            KING_ATTACKS[sq] = k_attacks & FULL_BOARD

    @staticmethod
    def precomputed_rays():
         deltas = [
             (1,0),   # North
             (1,1),   # North East
             (0,1),   # East,
             (-1,1),  # South East
             (-1,0),  # South
             (-1,-1), # South West
             (0, -1), # West
             (1,-1),  # Nort West
         ]
         
         for sq in range(64):
             start_rank, start_file = sq // 8, sq % 8
             for direction, (rank_delta, file_delta) in enumerate(deltas):
                 ray = 0
                 rank, file = start_rank + rank_delta, start_file + file_delta
                 while 0 <= rank < 8 and 0 <= file < 8:
                     ray |= 1 << (rank * 8 + file)
                     rank += rank_delta
                     file += file_delta
                 RAY_ATTACKS[direction][sq] = ray

    @classmethod
    def get_pawn_attacks(cls, sq: int, color: int, occupied: int, enemy_occupied: int, en_passant_square: int | None) -> int:
         """ Generate single pushes, double pushes and diagonal captures for a given pawn"""
         targets = 0
         bitboard = 1 << sq

         # If en_passant is active, add it to the valid capture targets
         capture_targets = enemy_occupied
         if en_passant_square is not None:
            capture_targets |= (1 << en_passant_square)

         if color == 0: # for white pawns
             single_push = (bitboard << 8) & ~occupied
             targets |= single_push
       
             # Double push if the pawn is in its starting position and there is no piece there
             if single_push and (bitboard & RANK_2):
                 targets |= (bitboard << 16) & ~occupied
     
             # Captures - use mask to prevent warping the board
             targets |= (bitboard << 7 & ~FILE_H) & capture_targets
             targets |= (bitboard << 9 & ~FILE_A) & capture_targets
         else: # for black pawns
             single_push = (bitboard >> 8) & ~occupied
             targets |= single_push
     
             # Double push check (same as above but inverted)
             if single_push and (bitboard & RANK_7):
                 targets |= (bitboard >> 16) & ~occupied
     
             # Captures (same as above, just inverted)
             targets |= (bitboard >> 7 & ~FILE_A) & capture_targets
             targets |= (bitboard >> 9 & ~FILE_H) & capture_targets
     
         return targets & FULL_BOARD

    @classmethod
    def get_king_moves(cls, board: ChessBoard, sq: int, color: int):
        own_occupied = board.white_occupied if color == 0 else board.black_occupied
        targets = KING_ATTACKS[sq] & ~own_occupied
        enemy_color = 1 if color == 0 else 0

        if color == 0 and sq == SQ["E1"] and not board.is_in_check(color):
            if (board.castling_rights & WK_CASTLE) and not (board.all_occupied & ((1 << SQ["F1"]) | (1 << SQ["G1"]))):
                if not board.is_square_attacked(SQ["F1"], enemy_color):
                    targets |= (1 << SQ["G1"])

            if (board.castling_rights & WQ_CASTLE) and not (board.all_occupied & ((1 << SQ["B1"]) | (1 << SQ["C1"]) | (1 << SQ["D1"]))):
                if not board.is_square_attacked(SQ["C1"], enemy_color):
                    targets |= (1 << SQ["C1"])

        elif color == 1 and sq == SQ["E8"] and not board.is_in_check(color):
            if (board.castling_rights & BK_CASTLE) and not (board.all_occupied & ((1 << SQ["F8"]) | (1 << SQ["G8"]))):
                if not board.is_square_attacked(SQ["F8"], enemy_color):
                    targets |= (1 << SQ["G8"])
            if (board.castling_rights & BQ_CASTLE) and not (board.all_occupied & ((1 << SQ["B8"]) | (1 << SQ["C8"]) | (1 << SQ["D8"]))):
                if not board.is_square_attacked(SQ["D8"], enemy_color):
                   targets |= (1 << SQ["C8"])

        return targets 
    
    @staticmethod   
    def get_ray_attacks(sq: int, occupied: int, rank_delta: int, file_delta: int) -> int:
         """ Generate ray attack (file_delta, rank_delta) stopping at the first collision """
         attacks = 0
         rank, file = sq // 8, sq % 8
         rank += rank_delta
         file += file_delta
   
         while 0 <= rank < 8 and 0 <= file < 8:
             target_square = rank * 8 + file
             target_bit = 1 << target_square
             attacks |= target_bit
             if occupied & target_bit:
                 break
             rank += rank_delta
             file += file_delta
   
         return attacks
     
    @classmethod
    def get_sliding_attacks(cls, sq: int, piece_type: int, occupied: int) -> int:
        """ Generate pseudo-legal target squares for Rook, Bishop and Queen """
        attacks = 0

         # For Queens / Bishops
        if piece_type in (2, 4):
            for rank_delta, file_delta in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                attacks |= cls.get_ray_attacks(sq, occupied, rank_delta, file_delta)

        if piece_type in (3, 4):
            for rank_delta, file_delta in [(1,0), (-1,0), (0,1), (0,-1)]:
                attacks |= cls.get_ray_attacks(sq, occupied, rank_delta, file_delta)

        return attacks

    @classmethod
    def get_pseudo_legal_moves(cls, board, sq: int) -> int:
        """ Return a bitboard with all the pseudo-legal moves for a pieces on a specific square """
        color, piece_type = board.get_piece_at(sq)
        if color is None or color != (0 if board.side_to_move == "white" else 1):
            return 0 # No piece was selected or it is not your turn to move

        own_occupied = board.white_occupied if color == 0 else board.black_occupied
        enemy_occupied = board.black_occupied if color == 0 else board.white_occupied

        # 0: Pawns, 1: Knights, 2: Bishop, 3: Rooks, 4: Queen, 5:   
        if piece_type == 0: 
            return cls.get_pawn_attacks(sq, color, board.all_occupied, enemy_occupied)
        elif piece_type == 1:
            return KNIGHT_ATTACKS[sq] & ~own_occupied
        elif piece_type in (2, 3, 4):
            return cls.get_sliding_attacks(sq, piece_type, board.all_occupied) & ~own_occupied
        elif piece_type == 5:
            return KING_ATTACKS[sq] & ~own_occupied
        return 0

MoveGenerator.precomputed_leaper_moves()