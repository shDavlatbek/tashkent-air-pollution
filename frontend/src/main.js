import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "@tabler/core/dist/css/tabler.min.css"
import '@tabler/core/dist/js/tabler.min.js';
import './style/main.css'
import VueApexCharts from "vue3-apexcharts";
import themePlugin from "./plugins/themePlugin";

createApp(App).use(router).use(themePlugin).use(VueApexCharts).mount("#app");