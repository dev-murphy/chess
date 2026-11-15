<script lang="ts" setup>
import { PieceTheme, type Piece, type Coords } from "~/types";

const appStore = useAppStore();

// Dragging controls for pieces
const isDragging = ref<Piece|null>(null);

// Board information
const boardRef = useTemplateRef('boardRef')
const { top, left } = useElementBounding(boardRef);

function handleDrop(pos: Coords) {
  const { r, c } =  getCoordsFromPosition(pos);
  let row = appStore.selectedSquare[0];
  let col = appStore.selectedSquare[1];
  
  if (row == undefined || col === undefined) return;
  if (r < 0 || r > 7 || c < 0 || c > 7 ) return;
  if (r === row - 1 && c === col - 1) return;
  
  appStore.board[r][c].piece = appStore.board[row-1][col-1].piece;
  appStore.board[row-1][col-1].piece = null;
  appStore.selectedSquare = [];
}

function getCoordsFromPosition(pos: Coords) {
  let x = Math.floor((pos.x - left.value) / 72);
  let y = Math.floor((pos.y - top.value) / 72);
  return { r: y, c: x };
}

// get opposite color based current square
function getTextColor(row: number, col: number) {
  return appStore.board[row - 1][col - 1].color === appStore.lightColor
    ? appStore.darkColor
    : appStore.lightColor;
}

onMounted(() => {
  appStore.initBoard();
});
</script>

<template>
<div>
  <div ref="boardRef">
    <div v-for="row in appStore.board.length" :key="`row-${row}`" class="flex">
      <div
        v-for="col in appStore.board.length"
        :key="`col-${col}`"
        :class="[
          'relative w-18 h-18',
          {
            selected:
              appStore.selectedSquare[0] == row &&
              appStore.selectedSquare[1] == col,
          },
        ]"
        :style="{
          backgroundColor: appStore.board[row - 1][col - 1].color,
        }"
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
          :piece="appStore.board[row - 1][col - 1].piece"
          :theme="PieceTheme.THEME_1"
          :is-dragging="isDragging"
          @mousedown="appStore.selectPiece(row, col)"
          @update:is-dragging="(val) => { isDragging = val }"
          @handle-drop="handleDrop"
        />
      </div>
    </div>
  </div>

  <!-- Audio for piece move and capture -->
  <audio />
</div>
</template>

<style scoped>
@reference "tailwindcss";

.selected::before {
  content: "";
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-yellow-200/75;
}
</style>
