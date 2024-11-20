import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/LoginComponent.vue";
import Register from "../components/RegisterComponent.vue";
import HomeView from "../views/HomeView.vue";

const routes = [
  { path: "/", name: "HomeView", component: HomeView },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
