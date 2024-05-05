import { createWebHistory, createRouter } from 'vue-router';

import HomeView from '../views/HomeView.vue';
import NotFoundPage from '../views/NotFoundPage.vue';

const routes = [
  { 
    path: "/",
    component: HomeView
  },
  {
    path: "/about",
    name: "about-page",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/pomodoro",
    name: "pomodoro-page",
    component: () => import("../views/Pomodoro.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    component: NotFoundPage,
    name: "not-found-page",
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;