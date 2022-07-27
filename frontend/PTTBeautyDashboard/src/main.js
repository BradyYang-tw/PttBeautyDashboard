import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import "@/plugins/fontawsome";



const app = createApp(App);
app.component("font-awesome-icon", FontAwesomeIcon)
app.use(ElementPlus);
app.use(router);
app.mount("#app");
