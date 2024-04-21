import { createMemoryHistory, createRouter } from "vue-router";

import HomeView from "./HomeView.vue";
import AboutView from "./AboutView.vue";
import NotFoundPage from "./NotFoundPage.vue";

const routes = [
  { path: "/", component: HomeView },
  { path: "/about", component: AboutView },
  {
    path: "/:pathMatch(.*)*",
    component: NotFoundPage,
    name: "not-found-page",
  },
];

const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
