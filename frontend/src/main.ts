import {createApp} from 'vue'
import App from './App.vue'
import {createPinia} from "pinia";
import {router} from "./router";
import 'bootstrap/dist/css/bootstrap.min.css';
import "@/assets/scss/index.scss"

const app = createApp(App)

app.use(createPinia());
app.use(router);

app.mount('#app')
