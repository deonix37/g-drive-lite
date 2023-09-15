<script>
export default {
  props: {
    file: {
      type: Object,
      required: true,
    },
  },
  emits: ['openImage'],
  computed: {
    thumbnailUrl() {
      return this.isImage
        ? this.file.thumbnailLink.replace(220, 400)
        : this.file.iconLink.replace(16, 256);
    },
    imageUrl() {
      return this.file.thumbnailLink.replace(220, 2560);
    },
    isImage() {
      return this.file.mimeType.startsWith('image/');
    },
  },
  methods: {
    openFile() {
      if (this.isImage) {
        this.$emit('openImage', {
          src: this.imageUrl,
          alt: this.file.title,
        });
      } else {
        window.open(this.file.webContentLink);
      }
    },
  },
}
</script>

<template>
  <div
    class="drive-file"
    :title="file.title"
  >
    <img
      :src="thumbnailUrl"
      class="drive-file-thumbnail"
      :class="{'drive-file-icon': !isImage}"
      referrerpolicy="no-referrer"
      @click="openFile"
    >
    <div class="drive-item-content">
      <img :src="file.iconLink">
      <span class="text-truncate">{{ file.title }}</span>
    </div>
  </div>
</template>

<style scoped>
.drive-file {
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border: 1px solid darkgray;
  border-radius: 8px;
  background: ghostwhite;
  text-align: center;
}

.drive-file-thumbnail {
  height: 13rem;
  object-fit: cover;
  cursor: pointer;
}

.drive-file-icon {
  padding: 2rem;
  object-fit: contain;
}

.drive-item-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
}
</style>
