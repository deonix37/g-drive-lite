<script>
import { useDriveStore } from '@/stores/drive';

export default {
  setup() {
    return {
      driveStore: useDriveStore(),
    };
  },
  watch: {
    '$route.params.directoryId'(directoryId) {
      const isCurrent = (item) => item.id === directoryId;
      const navItems = this.driveStore.navItems;
      const navIndex = navItems.findIndex(isCurrent);

      if (navIndex === -1) {
        const directory = this.driveStore.driveItems.find(isCurrent);

        if (directory) {
          this.driveStore.navItems.push(directory);
        } else {
          this.driveStore.loadNavItems();
        }
      } else {
        this.driveStore.navItems = navItems.slice(0, navIndex + 1);
      }
    },
  },
  mounted() {
    this.driveStore.loadNavItems();
  },
}
</script>

<template>
  <div class="directory-navigation">
    <router-link
      v-for="(navItem, i) in driveStore.navItems"
      :key="navItem.id"
      :to="`/${navItem.id}`"
      class="nav-item"
      :title="navItem.title"
    >
      <svg
        v-if="i !== 0"
        class="nav-item-separator"
        viewBox="0 0 24 24"
      >
        <polygon points="17.5 5.999 16.793 6.706 22.086 11.999 1 11.999 1 12.999 22.086 12.999 16.792 18.294 17.499 19.001 24 12.499 17.5 5.999"/>
      </svg>
      <div class="text-truncate">
        {{ navItem.title }}
      </div>
    </router-link>
  </div>
</template>

<style scoped>
.directory-navigation {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  overflow-x: auto;
  row-gap: 1rem;
  scrollbar-width: none;
}

.directory-navigation::-webkit-scrollbar {
  display: none;
}

.nav-item {
  position: relative;
  margin-left: 2rem;
  padding: 0.5rem 1rem;
  max-width: 20rem;
  border-radius: 15px;
  background: lavender;
  font-weight: 500;
}

.nav-item:first-child {
  margin-left: 0;
}

.nav-item:last-child {
  background: whitesmoke;
}

.nav-item-separator {
  --width: 20px;
  position: absolute;
  top: calc(50% - var(--width) / 2);
  left: -1.66rem;
  width: var(--width);
  fill: darkslategray;
}

@media (min-width: 640px) {
  .directory-navigation {
    flex-wrap: wrap;
  }
}
</style>
