<script>
import { useDriveStore } from '@/stores/drive';
import DirectoryMain from './DirectoryMain.vue';
import DirectoryNavigation from './DirectoryNavigation.vue';
import DirectoryOrdering from './DirectoryOrdering.vue';
import DrivePreloader from './DrivePreloader.vue';

export default {
  components: {
    DirectoryMain,
    DirectoryNavigation,
    DirectoryOrdering,
    DrivePreloader,
  },
  setup() {
    return {
      driveStore: useDriveStore(),
    };
  },
  data() {
    return {
      orderBy: 'title asc',
    };
  },
  watch: {
    orderBy(orderBy) {
      this.$router.replace({
        path: this.$route.fullPath,
        query: {orderBy},
      });
    },
    'driveStore.activeDirectory'(activeDirectory) {
      document.title = activeDirectory.title;
    },
  },
  mounted() {
    if (this.$route.query.orderBy) {
      this.orderBy = this.$route.query.orderBy;
    }
  },
}
</script>

<template>
  <div class="drive-directory">
    <div
      v-show="driveStore.navItems.length"
      class="directory-header"
    >
      <DirectoryNavigation />
      <DirectoryOrdering v-model:order-by="orderBy" />
    </div>
    <DirectoryMain
      v-if="driveStore.navItems.length"
      :order-by="orderBy"
    />
    <DrivePreloader v-show="driveStore.loading" />
  </div>
</template>

<style scoped>
.drive-directory {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.directory-header {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
