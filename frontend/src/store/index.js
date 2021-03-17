import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";
import authentication from "./modules/authentication";
import ImageCreate from "./modules/ImageCreate";
import ImageDetail from "./modules/ImageDetail"

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
});

export default new Vuex.Store({
  strict: true,
  modules: { authentication, ImageCreate, ImageDetail },
  plugins: [vuexLocal.plugin]
});
