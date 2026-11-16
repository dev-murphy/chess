from .bitboard import FILE_A, FILE_B, FILE_G, FILE_H

""" Generate moves for a knight and a king on every position on the board """
KNIGHT_ATTACKS = [0] * 64
KING_ATTACKS = [0] * 64

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
    KNIGHT_ATTACKS[sq] = n_attacks

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
    KING_ATTACKS[sq] = k_attacks
    
precomputed_leaper_moves()