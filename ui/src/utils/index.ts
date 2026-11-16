import type { Piece, PieceTheme } from "~/types";

export function getPieceImage(piece: Piece, theme: PieceTheme) {
  return `${import.meta.env.BASE_URL}pieces/${theme}/${piece.color}/${piece.type}.png`;
}

export function compareSquares(square1: number[], square2: [number, number]) {
  if (square1.length === 0) return false;
  return square1[0] === square2[0] && square1[1] === square2[1];
}