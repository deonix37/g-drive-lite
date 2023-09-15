<script>
export default {
  inheritAttrs: false,
  emits: ['close'],
}
</script>

<template>
  <div
    class="overlay"
    @click="$emit('close')"
  >
    <img
      v-bind="$attrs"
      class="popup-image"
    >
  </div>
</template>

<style scoped>
.popup-image {
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  padding: 2rem;
  max-width: 100%;
  max-height: 100%;
  filter: drop-shadow(5px 5px 10px #0005);
  user-select: none;
}
</style>
