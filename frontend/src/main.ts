import {createApp} from 'vue'
import App from './App.vue'
import {createPinia} from "pinia";
import {router} from "./router";
import 'bootstrap/dist/css/bootstrap.min.css';
import "@/assets/scss/index.scss"
import VueClickAway from "vue3-click-away";
import Notifications from '@kyvg/vue3-notification'

const app = createApp(App)

app.use(createPinia());
app.use(VueClickAway);
app.use(router);
app.use(Notifications);

app.mount('#app')
