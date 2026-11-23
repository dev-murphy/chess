import { defineStore } from "pinia";
import { type SquareInfo, PieceMap, PieceColor, type Piece, type PieceLetter } from "~/types";

export const useAppStore = defineStore("app", {
  state: () => ({
    name: "Chess",
    lightColor: "#EBECD0",
    darkColor: "#779556",
    board: Array.from({ length: 8 }, () =>
      Array(8).fill({
        color: "",
        piece: null,
      }),
    ) as SquareInfo[][],
    selectedSquare: null as [number, number] | null,
    lastBoard: [] as string[]
  }),
  actions: {
    initBoard() {
      for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
          this.board[row][col] = {
            color: (row + col) % 2 === 0 ? this.lightColor : this.darkColor,
            piece: null,
          };
        }
      }
    },
    fen(notation: string) {
      const segments = notation.split(" ");
      let boardState = segments[0];

      let position = 1;
      for (let i = 0; i < boardState.length; i++) {
        if (boardState.charAt(i) == "/") {
          continue;
        }

        if (/\d/.test(boardState.charAt(i))) {
          position += Number(boardState.charAt(i));
        } else {
          const { row, col } = this.positionToCoords(position - 1);
          this.board[row][col] = {
            ...this.board[row][col],
            piece: this.getPiece(boardState.charAt(i) as PieceLetter),
          };
          position++;
        }
      }
    },
    getPiece(pieceLetter: string): Piece {
      const formattedLetter = pieceLetter.toLowerCase() as PieceLetter;
      let defaultOptions = {
        type: PieceMap[formattedLetter],
        color: PieceColor.BLACK,
      };

      if (/[A-Z]/.test(pieceLetter)) {
        defaultOptions = {
          ...defaultOptions,
          color: PieceColor.WHITE,
        };
      }

      return defaultOptions;
    },
    positionToCoords(position: number) {
      return {
        row: Math.floor(position / 8),
        col: position % 8,
      };
    },
    selectPiece(row: number, col: number) {
      if (this.selectedSquare && this.selectedSquare[0] === row && this.selectedSquare[1] === col) {
        this.selectedSquare = null;
        return;
      }
      this.selectedSquare = [row, col];
    },
    setPosition(notation: string) {
      for (const row of this.board) for (const sq of row) sq.piece = null;
      this.fen(notation);
    },
    syncBoard(board: string[]) {
      for (let sq = 0; sq < 64; sq++) {
        if (board[sq] === this.lastBoard[sq]) continue;

        const row = 7 - Math.floor(sq / 8);
        const col = sq % 8;
        this.board[row][col].piece = board[sq] === "." ? null : this.getPiece(board[sq]);
      }
      this.lastBoard = board;
    },
  },
});
