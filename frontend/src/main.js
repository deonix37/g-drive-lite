import './assets/main.css';

import { createPinia } from 'pinia';
import { createApp } from 'vue';
import { createRouter, createWebHistory, useRoute } from 'vue-router';
import App from './App.vue';
import DriveDirectory from './components/DriveDirectory.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/:directoryId?/', component: DriveDirectory},
    ],
});

const pinia = createPinia().use(({store}) => {
    store.route = useRoute();
});

createApp(App).use(router).use(pinia).mount('#app');
