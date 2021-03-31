import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index";

import CreateImage from "../views/CreateImage.vue";
import ImageDetail from "../views/ImageDetail.vue";
import Profile from "../views/Profile.vue";

import Login from "../views/authentication/Login.vue";
import Register from "../views/authentication/Register.vue";
import Activate from "../views/authentication/Activate.vue";
import Timeline from "../views/Timeline.vue";
import About from "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  { path: "/", name: "Home", component: About },
  { path: "/timeline", name: "Timeline", component: Timeline },
  { path: "/register", name: "Register", component: Register },
  { path: "/activate", name: "Activate", component: Activate },
  { path: "/login", name: "Login", component: Login },
  { path: "/profile", name: "Profile", component: Profile },
  { path: "/images/create", name: "Create Image", component: CreateImage },
  {
    path: "/images/detail/:id/:slug",
    name: "Image Detail",
    component: ImageDetail
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

const PUBLIC_URLS = ["/", "/login", "/register", "/activate"];

function accessGranted(path) {
  return (
    (store.state.auth.iam.access_token && store.state.auth.iam.refresh_token) ||
    PUBLIC_URLS.includes(path)
  );
}

router.beforeEach((to, from, next) => {
  if (accessGranted(to.path)) {
    next();
  } else {
    next(false);
  }
});

export default router;
