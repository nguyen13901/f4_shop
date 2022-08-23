import { createWebHistory, createRouter } from "vue-router";

import HomePage from "@/components/HomePage.vue"
import AboutPage from "@/components/AboutPage.vue"
import ContactPage from "@/components/ContactPage.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/about-us",
    name: "AboutUs",
    component: AboutPage,
  },
  {
    path: "/contact",
    name: "Contact",
    component: ContactPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.name;
  next();
});

export default router;