import axios from "axios";
import Vue from "vue";
import router from "../../router/index";

const state = {
  imageData: {
    title: ""
  }
};

const actions = {
  async getImage({ commit }) {
    let response = await axios.get(
      `/images/api/detail/${router.currentRoute.params.id}/${router.currentRoute.params.slug}`
    );
    commit("setState", response.data);
  }
};

const mutations = {
  setState(state, data) {
    Vue.set(state.imageData, "title", data.image.title);
    state.imageData.title = data.image.title;
  },
  resetState() {}
};

const getters = {
  getImageDetail: state => state.imageData
};

export default {
  state,
  actions,
  mutations,
  getters
};
