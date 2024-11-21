import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "@tabler/core/dist/css/tabler.min.css"
import '@tabler/core/dist/js/tabler.min.js';
import './style/main.css'
import themePlugin from "./plugins/themePlugin";

createApp(App).use(router).use(themePlugin).mount("#app");