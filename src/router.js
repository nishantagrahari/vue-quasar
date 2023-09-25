import { createRouter, createWebHistory } from 'vue-router';
import Homepage from './components/Layout.vue';
import SignInPage from './components/Signin.vue';

const routes = [
  { path: '/home', component: Homepage},
  { path: '/', component: SignInPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
