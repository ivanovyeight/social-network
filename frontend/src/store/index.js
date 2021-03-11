import Vue from "vue";
import Vuex from "vuex";
import { loginUser, logoutUser } from '../services/auth';
import ImageCreate from './modules/ImageCreate'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
    accessTokenIsSet: window.localStorage.getItem('access_token')
  },
  mutations: {
    loginSuccess(state, userId) {
      state.user = userId;
      state.isLoggedIn = true;
    },
    logout(state) {
      state.user = null;
      state.isLoggedIn = false;
      state.accessTokenIsSet = window.localStorage.removeItem('access_token')
    },
  },
  actions: {
    login({ commit }, { username, password }) {
      return loginUser(username, password)
        .then(() => {
          commit({ type: 'loginSuccess', username });
          return Promise.resolve();
        }).catch((error) => {
          commit({ type: 'logout' });
          return Promise.reject(error);
        });
    },
    logout({ commit }) {
      logoutUser();
      commit('logout');
    },
  },
  modules: {ImageCreate},
});
