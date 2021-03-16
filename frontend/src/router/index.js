import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import CreateImage from "../views/CreateImage.vue";
import Profile from "../views/Profile.vue";

Vue.use(VueRouter);

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register },
  { path: "/profile", name: "Profile", component: Profile },
  { path: "/images/create", name: "Create Image", component: CreateImage },
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

const PUBLIC_URLS = ["/", "/login", "/register"];

function accessGranted(path) {
  return (
    (store.state.authentication.whoami.access_token &&
      store.state.authentication.whoami.refresh_token) ||
    PUBLIC_URLS.includes(path)
  );
}

router.beforeEach((to, from, next) => {
  if (accessGranted(to.path)) {
    next();
  } else {
    next("/login");
  }
});

export default router;
