import axios from "axios";
import Vue from "vue";
import { ACCESS_TOKEN } from "../../services/auth";
import router from "../../router/index";

const state = {
  data: {
    title: "",
    description: "",
    url: ""
  }
};

const actions = {
  saveImageToState({ commit }, object) {
    commit("setImageState", object);
  },

  async sendImageObject({ commit }) {
    let response = await axios.post("/images/api/create/", state.data, {
      headers: {
        Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
        "Content-Type": "application/json"
      }
    });
    commit("resetImageState");
    if (response.data === "success") {
      router.push("Home");
    }
  }
};

const mutations = {
  setImageState(state, object) {
    Vue.set(state.data, "title", object.title);
    Vue.set(state.data, "url", object.url);
    Vue.set(state.data, "description", object.description);
  },
  resetImageState(state) {
    Vue.set(state.data, "title", "");
    Vue.set(state.data, "url", "");
    Vue.set(state.data, "description", "");
  }
};

const getters = {
  imageData() {
    return state.data;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
