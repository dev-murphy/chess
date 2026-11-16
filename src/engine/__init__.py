from bitboard import SQ, RANK_2, RANK_7

class Chess:
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
        self.white_oocupied = 0
        self.black_occupied = 0
        self.all_occupied = 0

        # Reset to starting position
        self.reset_to_starting_position()

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

    def update_occupancies(self):
        self.white_occupied = 0
        white_pieces = [
            self.pieces["P"],
            self.pieces["R"],
            self.pieces["B"],
            self.pieces["N"],
            self.pieces["Q"],
            self.pieces["K"],
        ]
        for b in white_pieces:
            self.white_occupied |= b

        self.black_occupied = 0
        black_pieces = [
            self.pieces["p"],
            self.pieces["r"],
            self.pieces["b"],
            self.pieces["n"],
            self.pieces["q"],
            self.pieces["k"],
        ]
        for b in black_pieces:
            self.black_occupied |= b
