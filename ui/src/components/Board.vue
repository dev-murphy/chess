<script lang="ts" setup>
import { PieceTheme, type Piece, type Coords } from "~/types";
import { compareSquares } from "~/utils";
import moveAudioFile from "~/assets/audio/piece-move.mp3";
import captureAudioFile from "~/assets/audio/piece-capture.mp3"

const appStore = useAppStore();

// audio files
const moveSound = new Audio(moveAudioFile);
const captureSound = new Audio(captureAudioFile);

function playMoveSound() {
  moveSound.currentTime = 0;
  moveSound.play().catch(error => {
    console.error('Playback failed: ', error);
  })
}

function playCaptureSound() {
  captureSound.currentTime = 0;
  captureSound.play().catch(error => {
    console.error('Playback failed: ', error);
  })
}

// Dragging controls for pieces
const hoveredSquare = ref<[number, number] | null>(null);
const isDragging = ref<Piece | null>(null);

// Board information
const boardRef = useTemplateRef("boardRef");
const { top, left } = useElementBounding(boardRef);

function getCoordsFromPosition(pos: Coords) {
  let x = Math.floor((pos.x - left.value) / 72);
  let y = Math.floor((pos.y - top.value) / 72);
  return { r: y, c: x };
}

function handleDrop(pos: Coords) {
  const { r, c } = getCoordsFromPosition(pos);
  let row = appStore.selectedSquare[0];
  let col = appStore.selectedSquare[1];

  if (row == undefined || col === undefined) return;
  if (r < 0 || r > 7 || c < 0 || c > 7) return;
  if (r === row - 1 && c === col - 1) return;

  if (appStore.board[r][c].piece !== null) {
    playCaptureSound();
  } else {
    playMoveSound();
  }

  appStore.board[r][c].piece = appStore.board[row - 1][col - 1].piece;
  appStore.board[row - 1][col - 1].piece = null;
  appStore.selectedSquare = [];
}

function handleMouseDown(event: MouseEvent) {
  const { r, c } = getCoordsFromPosition({
    x: event.clientX,
    y: event.clientY,
  });
  hoveredSquare.value = [r, c];
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
                compareSquares(appStore.selectedSquare, [row, col]),
              'ring-6 ring-inset ring-white/90':
                hoveredSquare !== null && isDragging !== null &&
                compareSquares(hoveredSquare, [row-1, col-1])
            },
          ]"
          :style="{
            backgroundColor: appStore.board[row - 1][col - 1].color,
          }"
          @mouseover="handleMouseDown"
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
            @update:is-dragging="
              (val) => {
                isDragging = val;
              }
            "
            @handle-drop="handleDrop"
          />
        </div>
      </div>
    </div>
    Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=60890">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=60890">Pixabay</a>
  </div>
</template>

<style scoped>
@reference "tailwindcss";

.selected::before {
  content: "";
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-yellow-200/75;
}
</style>
