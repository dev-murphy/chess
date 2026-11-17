from .bitboard import FILE_A, FILE_B, FILE_G, FILE_H, RANK_2, RANK_7

""" Generate moves for a knight and a king on every position on the board """
KNIGHT_ATTACKS = [0] * 64
KING_ATTACKS = [0] * 64
FULL_BOARD = 0xFFFFFFFFFFFFFFFF

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
    def get_pawn_attacks(cls, sq: int, color: int, occupied: int, enemy_occupied: int) -> int:
         """ Generate single pushes, double pushes and diagonal captures for a given pawn"""
         targets = 0
         bitboard = 1 << sq
     
         if color == 0: # for white pawns
             single_push = (bitboard << 8) & ~occupied
             targets |= single_push
       
             # Double push if the pawn is in its starting position and there is no piece there
             if single_push and (bitboard & RANK_2):
                 targets |= (bitboard << 16) & ~occupied
     
             # Captures - use mask to prevent warping the board
             targets |= (bitboard << 7 & ~FILE_H) & enemy_occupied
             targets |= (bitboard << 9 & ~FILE_A) & enemy_occupied
         else: # for black pawns
             single_push = (bitboard >> 8) & ~occupied
             targets |= single_push
     
             # Double push check (same as above but inverted)
             if single_push and (bitboard & RANK_7):
                 targets |= (bitboard >> 16) & ~occupied
     
             # Captures (same as above, just inverted)
             targets |= (bitboard >> 7 & ~FILE_A) & enemy_occupied
             targets |= (bitboard >> 9 & ~FILE_H) & enemy_occupied
     
         return targets & FULL_BOARD
   
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