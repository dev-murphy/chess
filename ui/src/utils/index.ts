import type { Piece, PieceTheme, Coords } from "~/types";

export function getPieceImage(piece: Piece, theme: PieceTheme) {
  return `${import.meta.env.BASE_URL}pieces/${theme}/${piece.color}/${piece.type}.png`;
}

export function compareSquares(square1: number[], square2: [number, number]) {
  if (square1.length === 0) return false;
  return square1[0] === square2[0] && square1[1] === square2[1];
}

export function boardCoordsFrom(position: Coords, top: number, left: number) {
  let x = Math.floor((position.x - left) / 72);
  let y = Math.floor((position.y - top) / 72);
  return { r: y, c: x };
}

export function moveCoordsFrom(row: number, col: number) {
  return (7 - row) * 8 + col;
}
