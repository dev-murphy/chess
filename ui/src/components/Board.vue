<script lang="ts" setup>
import { PieceTheme } from "~/types";

const appStore = useAppStore();

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
    <div v-for="row in appStore.board.length" :key="`row-${row}`" class="flex">
      <div
        v-for="col in appStore.board.length"
        :key="`col-${col}`"
        :class="[
          'relative w-18 aspect-square',
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
          @mousedown="appStore.selectPiece(row, col)"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
@reference "tailwindcss";

.selected::before {
  content: "";
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-yellow-200/75;
}
</style>
