import { createApp } from 'vue'
import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import "./assets/global.css"


import VueBlocksTree from 'vue3-blocks-tree';
import 'vue3-blocks-tree/dist/vue3-blocks-tree.css';
import 'bootstrap-icons/font/bootstrap-icons.css';


let defaultoptions = {treeName:'blocks-tree'}




createApp(App).use(Quasar, quasarUserOptions).use(VueBlocksTree,defaultoptions).mount('#app')

