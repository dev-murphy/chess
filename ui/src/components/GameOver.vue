<script lang="ts" setup>
import type { ChessGameState } from "~/types/api";

const props = defineProps<{
  state: ChessGameState;
}>();

const emit = defineEmits<{
  (e: "new-game"): void;
}>();

const DRAW_REASONS = {
  insufficient_material: "Insufficient material",
  threefold_repetition: "Threefold repetition",
  fifty_move_rule: "50-move rule",
} as const;

const title = computed(() => {
  switch (props.state.status) {
    case "checkmate":
      return "Checkmate";
    case "stalemate":
      return "Stalemate";
    default:
      return "Draw";
  }
});

const subtitle = computed(() => {
  const { status, winner, draw_reason } = props.state;
  if (status === "checkmate" && winner) return `${winner} wins`;
  if (status === "stalemate") return "Draw — no legal moves";
  if (draw_reason) return `Draw by ${DRAW_REASONS[draw_reason].toLowerCase()}`;
  return "";
});
</script>

<template>
  <div
    class="absolute inset-0 z-20 flex items-center justify-center bg-black/50"
    role="dialog"
    aria-modal="true"
    :aria-label="title"
  >
    <div class="flex flex-col items-center gap-2 rounded-xl bg-neutral-900 px-10 py-8 text-white shadow-2xl">
      <h2 class="font-marcellus text-4xl">{{ title }}</h2>
      <p class="font-mulish text-base font-bold uppercase tracking-wide text-neutral-300">
        {{ subtitle }}
      </p>
      <button
        type="button"
        class="mt-4 rounded-lg bg-emerald-600 px-6 py-2 font-mulish font-black uppercase text-white transition-colors hover:bg-emerald-500"
        @click="emit('new-game')"
      >
        New Game
      </button>
    </div>
  </div>
</template>
