import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from 'vuex-persist'
// import profile from "./modules/profile";
import authentication from "./modules/authentication";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

export default new Vuex.Store({
  strict: true,
  modules: { authentication },
  plugins: [vuexLocal.plugin]
});
