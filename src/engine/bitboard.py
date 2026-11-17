# Square index mapping: 0 = A1, 7 = H1, 56 = A8, 63 = H8
SQUARES = [
  "A1","B1","C1","D1","E1","F1","G1","H1",
  "A2","B2","C2","D2","E2","F2","G2","H2",
  "A3","B3","C3","D3","E3","F3","G3","H3",
  "A4","B4","C4","D4","E4","F4","G4","H4",
  "A5","B5","C5","D5","E5","F5","G5","H5",
  "A6","B6","C6","D6","E6","F6","G6","H6",
  "A7","B7","C7","D7","E7","F7","G7","H7",
  "A8","B8","C8","D8","E8","F8","G8","H8",
]

# Quick square lookup (e.g. SQ['E4'] => 24)
SQ = {name: index for index, name in enumerate(SQUARES)}

# Pre-computed mask for files and ranks
FILE_A = 0x0101010101010101
FILE_B = FILE_A << 1
FILE_C = FILE_A << 2
FILE_D = FILE_A << 3
FILE_E = FILE_A << 4
FILE_F = FILE_A << 5
FILE_G = FILE_A << 6
FILE_H = FILE_A << 7

RANK_1 = 0x00000000000000FF
RANK_2 = RANK_1 << 8
RANK_3 = RANK_1 << 16
RANK_4 = RANK_1 << 24
RANK_5 = RANK_1 << 32
RANK_6 = RANK_1 << 40
RANK_7 = RANK_1 << 48
RANK_8 = RANK_1 << 56

class Bitboard:
    @staticmethod
    def set_bit(bitboard: int, square: int) -> int:
        """Set a bit at the bottom at the given square index (0-63)"""
        return bitboard | (1 << square)

    @staticmethod
    def clear_bit(bitboard: int, square: int) -> int:
        """Clears bit at a given square index (0-63)"""
        return bitboard & ~(1 << square)

    @staticmethod
    def get_bit(bitboard: int, square: int) -> int:
        """Return 1 if the bit is set, 0 otherwise"""
        return (bitboard >> square) & 1

    @staticmethod
    def toggle_bit(bitboard: int, square: int) -> int:
        """Toggle a bit for a given square index (0-63)"""
        return bitboard ^ (1 << square)

    @staticmethod
    def pop_lsb(bitboard: int) -> tuple[int, int]:
        """
        Removes the Least Significant Bit (LSB) and returns
        (lsb_index, new_bitboard). Essential for iterating
        over set bits.
        """
        if bitboard == 0:
            return -1, 0
        lsb_index = (bitboard & -bitboard).bit_length() - 1
        new_bitboard = bitboard & (bitboard - 1)
        return lsb_index, new_bitboard

    @staticmethod
    def print_bitboard(bitboard: int) -> None:
        """Prints an 8x8 representative of a single bitboard."""
        print("\n  +-----------------------+ Bitboard Value: " + hex(bitboard))
        for rank in range(7, -1, -1):
            row = [f"{rank + 1} |"]
            for file in range(8):
                square = rank * 8 + file
                bit = (bitboard >> square) & 1
                row.append(" 1" if bit else " .")
            print(" ".join(row))
        print("  +-----------------------+")
        print("     a  b  c  d  e  f  g  h\n")
