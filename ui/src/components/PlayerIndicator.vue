<script lang="ts" setup>
const props = withDefaults(
  defineProps<{
    color: "black" | "white";
    isCurrentColor: boolean;
    direction?: "top" | "bottom";
  }>(),
  {
    direction: "top",
  },
);
</script>

<template>
  <div
    :class="[
      'player-indicator absolute w-fit px-4 py-1 text-base font-mulish font-black uppercase',
      {
        'bg-white text-black': color === 'white',
        'bg-black text-white': color === 'black',
        'top top-0 -translate-y-full ml-3 rounded-t-xl': direction === 'top',
        'bottom not-odd:bottom-0 right-0 translate-y-full  mr-3 rounded-b-xl': direction === 'bottom',
        'current': isCurrentColor
      },
    ]"
  >
    <span class="relative">
    {{ color }}
    </span>
  </div>
</template>

<style scoped>
@reference "tailwindcss";

.player-indicator::before {
  content: "";
  @apply absolute w-full h-full max-h-0 transition-all duration-150;
}

.player-indicator.top::before {
  @apply bottom-0 inset-x-0 bg-linear-to-t from-emerald-500 to-transparent;
}

.player-indicator.bottom::before {
  @apply top-0 inset-x-0 bg-linear-to-b from-emerald-500/70 to-transparent;
}

.player-indicator.current::before {
  @apply max-h-2/3;
}


</style>