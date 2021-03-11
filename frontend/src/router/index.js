import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import CreateImage from "../views/CreateImage.vue"

import { ACCESS_TOKEN, REFRESH_TOKEN } from '../services/auth';

Vue.use(VueRouter);

const PUBLIC_PATHS = ['/', '/login', '/register'];

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register },



  
  { path: "/images/create", name:"Create Image", component: CreateImage},



  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

const unAuthenticatedAndPrivatePage = (path) => (!PUBLIC_PATHS.includes(path)
    && !(ACCESS_TOKEN in window.localStorage)
    && !(REFRESH_TOKEN in window.localStorage));

router.beforeEach((to, from, next) => {
  if (unAuthenticatedAndPrivatePage(to.path)) {
    next(`/login?next=${to.path}`);
  } else {
    next();
  }
});

export default router;
