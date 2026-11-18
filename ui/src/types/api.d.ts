import type { PieceColor } from ".";

type PieceSymbol = 'P' | 'N' | 'B' | 'R' | 'Q' | 'K' | 'p' | 'n' | 'b' | 'r' | 'q' | 'k';
type GameStatus = "active" | "checkmate" | "stalemate";
type Coord = [number, number];

export interface ChessGameState {
  turn: PieceColor;
  status: GameStatus;
  in_check: boolean;
  legal_moves: Record<string, Coord[]>;
  captured_pieces: {
    white: PieceSymbol[],
    black: PieceSymbol[]
  }
}

export interface PywebviewChessApi {
  to_json(): Promise<ChessGameState>; 
}

declare global {
  interface Window {
    pywebview?: {
      api: PywebviewChessApi;
    }
  }
}