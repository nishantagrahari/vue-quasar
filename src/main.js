import { createApp } from 'vue';
import { Quasar } from 'quasar';
import quasarUserOptions from './quasar-user-options';
import VueBlocksTree from 'vue3-blocks-tree';
import 'vue3-blocks-tree/dist/vue3-blocks-tree.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import router from './router'; // Import the router
import App from './App.vue';
import "./assets/global.css";

let defaultoptions = { treeName: 'blocks-tree' };

createApp(App)
  .use(Quasar, quasarUserOptions)
  .use(VueBlocksTree, defaultoptions)
  .use(router) // Use the router
  .mount('#app');
