<script>
import { useDriveStore } from '@/stores/drive';
import DirectoryFile from './DirectoryFile.vue';
import DirectoryFolder from './DirectoryFolder.vue';
import ImagePopup from './ImagePopup.vue';

export default {
  components: {
    DirectoryFile,
    DirectoryFolder,
    ImagePopup,
  },
  props: {
    orderBy: {
      type: String,
      required: true,
    },
  },
  setup() {
    return {
      driveStore: useDriveStore(),
    };
  },
  data() {
    return {
      openedFile: null,
    };
  },
  computed: {
    triggersReload() {
      return [this.driveStore.activeDirectory, this.orderBy];
    },
  },
  watch: {
    triggersReload: {
      handler() {
        this.driveStore.loadDriveItems({orderBy: this.orderBy});
      },
      immediate: true,
    },
  },
  mounted() {
    window.addEventListener(
      'scroll',
      this.loadNextOnScroll,
      {passive: true}
    );
  },
  unmounted() {
    window.removeEventListener(
      'scroll',
      this.loadNextOnScroll,
      {passive: true}
    );
  },
  methods: {
    loadNextOnScroll() {
      if (this.driveStore.loading || !this.driveStore.pageToken) {
        return;
      }

      const {scrollHeight} = document.documentElement;
      const boundary = scrollHeight - 2 * window.outerHeight;

      if (window.top.scrollY > boundary) {
        this.driveStore.loadNextDriveItems({orderBy: this.orderBy});
      }
    },
  },
}
</script>

<template>
  <div class="directory-main">
    <template v-if="driveStore.driveItems.length">
      <div
        v-show="driveStore.folders.length"
        class="drive-items"
      >
        <DirectoryFolder
          v-for="folder in driveStore.folders"
          :key="folder.id"
          :folder="folder"
        />
      </div>
      <div class="drive-items">
        <DirectoryFile
          v-for="file in driveStore.files"
          :key="file.id"
          :file="file"
          @open-image="file => openedFile = file"
        />
      </div>
      <ImagePopup
        v-if="openedFile"
        v-bind="openedFile"
        referrerpolicy="no-referrer"
        @close="openedFile = null"
      />
    </template>
    <div
      v-else
      class="empty-folder-warning"
    >
      Folder is empty!
    </div>
  </div>
</template>

<style scoped>
.directory-main {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.drive-items {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(10rem, 1fr));
  gap: 1rem;
}

.empty-folder-warning {
  font-size: 2rem;
  letter-spacing: 0.025em;
  text-align: center;
  font-weight: bold;
  color: plum;
  user-select: none;
}

@media (min-width: 640px) {
  .drive-items {
    grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr));
  }
}
</style>
