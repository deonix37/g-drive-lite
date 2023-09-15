<script>
export default {
  props: {
    folder: {
      type: Object,
      required: true,
    },
  },
}
</script>

<template>
  <router-link
    :to="`/${folder.id}`"
    class="drive-folder"
    :title="folder.title"
  >
    <div class="drive-item-content">
      <img
        :src="folder.iconLink"
        width="16"
        height="16"
      >
      <span class="text-truncate">{{ folder.title }}</span>
    </div>
  </router-link>
</template>

<style scoped>
.drive-folder {
  border: 1px solid lightsteelblue;
  border-radius: 8px;
  background: lavender;
}

.drive-file-thumbnail {
  object-fit: cover;
  object-position: top;
  max-width: 100%;
  cursor: pointer;
}

.drive-item-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
}
</style>
