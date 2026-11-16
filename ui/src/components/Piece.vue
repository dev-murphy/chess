<script lang="ts" setup>
import { getPieceImage } from "~/utils";
import { PieceTheme, type Piece, type Coords} from "~/types";

const props = withDefaults(
  defineProps<{ piece: Piece; theme?: PieceTheme; isDragging: Piece | null }>(),
  {
    theme: PieceTheme.THEME_1,
  },
);

const emits = defineEmits<{
  (e: "update:isDragging", val: Piece | null): void;
  (e: "handle-drop", pos: Coords): void;
}>();

const pieceImg = useTemplateRef("pieceImg");
const { top, left } = useElementBounding(pieceImg);
const { x, y } = useDraggable(pieceImg, {
  initialValue: { y: top.value, x: left.value },
  onStart() {
    if (!pieceImg.value) return;
    emits("update:isDragging", props.piece);
    y.value = top.value;
    x.value = left.value;
    pieceImg.value.style.zIndex = "100";
  },
  onEnd(_, event) {
    emits("update:isDragging", null);
    emits("handle-drop", {
      x: event.clientX,
      y: event.clientY
    })
  },
});
</script>

<template>
  <div
    ref="pieceRef"
    :class="[
      'w-full h-full flex items-end justify-center cursor-grab',
      {
        'items-end': theme === PieceTheme.THEME_1,
        'items-center': theme === PieceTheme.THEME_2,
      },
    ]"
  >
    <img
      ref="pieceImg"
      draggable="false"
      :src="getPieceImage(piece, theme)"
      :alt="`${piece.color} ${piece.type}`"
      :class="[
        'relative select-none touch-none',
        {
          'w-16': theme === PieceTheme.THEME_1,
          'w-18': theme === PieceTheme.THEME_2,
        },
      ]"
      :style="
        isDragging === piece
          ? { position: 'fixed', top: `${y}px`, left: `${x}px`, zIndex: '100', pointerEvents: 'none' }
          : {}
      "
    />
  </div>
</template>
