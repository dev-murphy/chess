<script lang="ts" setup>
import { PieceTheme, type Piece, type Coords } from "~/types";
import type { ChessGameState, PywebviewChessApi } from "~/types/api";
import { compareSquares, boardCoordsFrom, moveCoordsFrom } from "~/utils";

import moveAudioFile from "~/assets/audio/piece-move.mp3";
import captureAudioFile from "~/assets/audio/piece-capture.mp3";

const appStore = useAppStore();
const gameState = ref<ChessGameState | null>(null);
let api: PywebviewChessApi | null = null;

// audio files
const moveSound = new Audio(moveAudioFile);
const captureSound = new Audio(captureAudioFile);

function playMoveSound() {
  moveSound.currentTime = 0;
  moveSound.play().catch((error) => {
    console.error("Playback failed: ", error);
  });
}

function playCaptureSound() {
  captureSound.currentTime = 0;
  captureSound.play().catch((error) => {
    console.error("Playback failed: ", error);
  });
}

// Dragging controls for pieces
const hoveredSquare = ref<[number, number] | null>(null);
const isDragging = ref<Piece | null>(null);

// Board information
const boardRef = useTemplateRef("boardRef");
const { top, left } = useElementBounding(boardRef);

// Draw on locally board for must captures
function updateBoardUI(position: Coords) {
  const { selectedSquare, board } = appStore;

  if (selectedSquare === null) return {};
  const { r, c } = boardCoordsFrom(position, top.value, left.value);
  let row = selectedSquare[0];
  let col = selectedSquare[1];

  if ((r === row - 1 && c === col - 1) || !moveExists([7 - r, c])) return {};

  const hasPiece = board[r][c].piece !== null;
  const isCapture = hasPiece || (board[row-1][col-1].piece?.type === "pawn" && c !== col - 1)
  board[r][c].piece = board[row - 1][col - 1].piece;
  board[row - 1][col - 1].piece = null;

  if (isCapture) playCaptureSound();
  else playMoveSound();

  appStore.selectedSquare = null;
  highlightedSquare.value = [];
  if (gameState.value) {
    gameState.value.legal_moves = {};
  }

  return {
    toCoords: [r, c],
    fromCoords: [row-1, col-1]
  }
}

async function handleDrop(pos: Coords) {
  const { toCoords, fromCoords } = updateBoardUI(pos);
  if (!toCoords || !fromCoords) return;

  let to_sq = moveCoordsFrom(toCoords[0],toCoords[1]);
  let from_sq = moveCoordsFrom(fromCoords[0], fromCoords[1]);

  let newState = await api?.make_move(from_sq, to_sq, 3);
  if (newState && newState.valid_move) {
    gameState.value = newState.state;
    appStore.syncBoard(gameState.value.board);
  }
}

function handleMouseOver(event: MouseEvent) {
  const { r, c } = boardCoordsFrom({
    x: event.clientX,
    y: event.clientY,
  }, top.value, left.value);
  hoveredSquare.value = [r, c];
}

// get opposite color based current square
function getTextColor(row: number, col: number) {
  return appStore.board[row - 1][col - 1].color === appStore.lightColor
    ? appStore.darkColor
    : appStore.lightColor;
}

// board things
const highlightedSquare = ref<number[][]>([]);
function getMoveSquares(row: number, col: number) {
  if (!gameState.value) return;
  let key = `${8 - row},${col - 1}`;
  highlightedSquare.value = gameState.value.legal_moves[key];
}

function moveExists(coords: number[]) {
  if (!highlightedSquare.value) return false; 

  return highlightedSquare.value.some(
    (square) =>
      coords.length === square.length &&
      square.every((val, index) => coords[index] == val),
  );
}

function selectPiece(row: number, col: number) {
  appStore.selectPiece(row, col);
  if (appStore.selectedSquare) {
    getMoveSquares(row, col);
  } else {
    highlightedSquare.value = [];
  }
} 

async function drawBoard(api: PywebviewChessApi | null) {
  if (!api) return;
  gameState.value = await api.to_json();
  appStore.syncBoard(gameState.value.board)
}

onMounted(async () => {
  appStore.initBoard();
  api = await usePywebviewApi();
  await drawBoard(api)
});
</script>

<template>
  <div>
    <div ref="boardRef" :class="{'cursor-grabbing': isDragging}">
      <div
        v-for="row in appStore.board.length"
        :key="`row-${row}`"
        class="flex"
      >
        <div
          v-for="col in appStore.board.length"
          :key="`col-${col}`"
          :class="[
            'relative w-18 h-18',
            {
              selected:
                appStore.selectedSquare && compareSquares(appStore.selectedSquare, [row, col]) ||
                moveExists([8 - row, col - 1]),
              hovered:
                hoveredSquare &&
                isDragging &&
                compareSquares(hoveredSquare, [row - 1, col - 1]),
            },
          ]"
          :style="{
            backgroundColor: appStore.board[row - 1][col - 1].color,
          }"
          @mouseover="handleMouseOver"
        >
          <span
            v-if="col === 1"
            class="absolute top-0.5 left-0.75 text-sm font-bold"
            :style="{ color: getTextColor(row, col) }"
            >{{ 8 - row + 1 }}</span
          >

          <span
            v-if="row === 8"
            class="absolute bottom-0.5 right-0.75 text-sm font-bold"
            :style="{ color: getTextColor(row, col) }"
            >{{ "abcdefgh".charAt(col - 1) }}</span
          >

           <Piece
            v-if="appStore.board[row - 1][col - 1].piece !== null"
            :piece="appStore.board[row - 1][col - 1].piece!"
            :theme="PieceTheme.THEME_1"
            :is-dragging="isDragging"
            @update:is-dragging="
              (val) => {
                isDragging = val;
                if (val) {
                  selectPiece(row, col)
                }
              }
            "
            @handle-drop="handleDrop"
          /> 
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@reference "tailwindcss";

.selected::before {
  content: "";
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-yellow-500/20;
}

.hovered::after {
  content: "";
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full ring-6 ring-inset ring-white/75;
}
</style>
