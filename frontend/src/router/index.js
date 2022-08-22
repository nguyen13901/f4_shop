import { createWebHistory, createRouter } from "vue-router";

import HomePage from "@/components/HomePage.vue"

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
    meta: {
        title: "Home Page",
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;