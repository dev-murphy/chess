from .bitboard import Bitboard, SQ, RANK_2, RANK_7

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
        self.pieces["p"] = RANK_7
        self.pieces["r"] = (1 << SQ["A8"]) | (1 << SQ["H8"])
        self.pieces["b"] = (1 << SQ["B8"]) | (1 << SQ["G8"])
        self.pieces["n"] = (1 << SQ["C8"]) | (1 << SQ["F8"])
        self.pieces["q"] = 1 << SQ["D8"]
        self.pieces["k"] = 1 << SQ["E8"]

        self.pieces["P"] = RANK_2
        self.pieces["R"] = (1 << SQ["A1"]) | (1 << SQ["H1"])
        self.pieces["B"] = (1 << SQ["B1"]) | (1 << SQ["G1"])
        self.pieces["N"] = (1 << SQ["C1"]) | (1 << SQ["F1"])
        self.pieces["Q"] = 1 << SQ["D1"]
        self.pieces["K"] = 1 << SQ["E1"]

        self.update_occupancies()
        
    def update_occupancies(self):
        self.white_occupied = 0
        
        for b in self.white_pieces():
            self.white_occupied |= b

        self.black_occupied = 0
        for b in self.black_pieces():
            self.black_occupied |= b

        

    def display(self):
        """ Prints the complete chess board with unicode character """
        symbols = {
            (0, 0): "♙", (0, 1): "♘", (0, 2): "♗", (0, 3): "♖", (0, 4): "♕", (0, 5): "♔",
            (1, 0): "♟", (1, 1): "♞", (1, 2): "♝", (1, 3): "♜", (1, 4): "♛", (1, 5): "♚"
        }
        grid = [["." for _ in range(8)] for _ in range(8)]
        for color, pieces in [(0,self.black_pieces()), (1, self.white_pieces())]:
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