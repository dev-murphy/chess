import type { PieceColor } from ".";

type PieceSymbol = 'P' | 'N' | 'B' | 'R' | 'Q' | 'K' | 'p' | 'n' | 'b' | 'r' | 'q' | 'k';
type GameStatus = "active" | "checkmate" | "stalemate" | "draw";
type DrawReason = "insufficient_material" | "threefold_repetition" | "fifty_move_rule";
type Coord = [number, number];

export interface ChessGameState {
  turn: PieceColor;
  status: GameStatus;
  draw_reason: DrawReason | null;
  winner: "white" | "black" | null;
  in_check: boolean;
  captured: boolean;
  board: string[];
  side_to_move: string;
  legal_moves: Record<string, Coord[]>;
  captured_pieces: {
    white: PieceSymbol[],
    black: PieceSymbol[]
  }
}

export interface MoveState {
  valid_move: boolean;
  state: ChessGameState;
}

export interface PywebviewChessApi {
  to_json(): Promise<ChessGameState>;
  make_move(from_square: number, to_square: number, promotionType: number): Promise<MoveState>;
  reset_game(): Promise<ChessGameState>;
}

declare global {
  interface Window {
    pywebview?: {
      api: PywebviewChessApi;
    }
  }
}