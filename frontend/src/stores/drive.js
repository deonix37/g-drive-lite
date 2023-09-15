import { apiFetch } from '@/assets/api.js';
import { defineStore } from 'pinia';

const MIME_FOLDER = 'application/vnd.google-apps.folder';

export const useDriveStore = defineStore('drive', {
    state: () => ({
        navItems: [],
        driveItems: [],
        pageToken: null,
        loading: false,
    }),
    getters: {
        activeDirectory: (state) => state.navItems.at(-1),
        files: (state) => state.driveItems.filter((item) => {
            return item.mimeType !== MIME_FOLDER;
        }),
        folders: (state) => state.driveItems.filter((item) => {
            return item.mimeType === MIME_FOLDER;
        }),
    },
    actions: {
        async loadNavItems() {
            const directoryId = this.route.params.directoryId || 'root';
            const res = await this.fetch(
                `/directories/${directoryId}/parents`
            );

            this.navItems = await res.json();
        },
        async loadNextDriveItems(params) {
            const driveItems = await this.fetchDriveItems(params, {
                'page-token': this.pageToken,
            });

            this.driveItems.push(...driveItems);
        },
        async loadDriveItems(params) {
            this.driveItems = await this.fetchDriveItems(params);
        },
        async fetchDriveItems(params, headers = {}) {
            const res = await this.fetch(
                `/directories/${this.activeDirectory.id}/file-list`,
                params,
                headers
            );
            this.pageToken = res.headers.get('page-token');

            return await res.json();
        },
        async fetch(path, params, headers) {
            this.loading = true;

            try {
                return await apiFetch(path, params, headers);
            } finally {
                this.loading = false;
            }
        },
    },
});
