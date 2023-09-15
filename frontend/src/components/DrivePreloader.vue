<template>
  <div class="overlay">
    <div class="preloader" />
  </div>
</template>

<style scoped>
.preloader {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 48px;
  height: 48px;
  border: 5px solid white;
  border-radius: 50%;
  border-bottom-color: cornflowerblue;
  animation: preloader 1s linear infinite;
}

@keyframes preloader {
  0% {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  100% {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
