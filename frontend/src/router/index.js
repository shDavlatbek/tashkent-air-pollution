import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/HomeComponent.vue";
import Login from "../components/LoginComponent.vue";
import Register from "../components/RegisterComponent.vue";
import AuthenticatedHome from "../views/AuthenticatedHome.vue";

const routes = [
  { path: "/", name: "HomePage", component: Home },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register },
  { path: "/authenticated", name: "AuthenticatedHome", component: AuthenticatedHome },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
