import axios from 'axios'
import Vue from 'vue'
import { ACCESS_TOKEN } from '../../services/auth';
import router from '../../router/index'


const state = {
  data: {
    title: "",
    description: "",
    url: ""
  }
};

const actions = {
<<<<<<< HEAD
  saveImageToState({ commit }, object) {
    commit("setImageState", object);
  },
  async sendImageObject(state) {
    let headers = {
      Authorization: `Bearer ${state.whoami.access_token}`
    };

    await axios.post("/images/api/create/", state.data, {
      headers
    });
  }
};

const mutations = {
  setImageState(state, object) {
    Vue.set(state.data, "title", object.title);
    Vue.set(state.data, "url", object.url);
    Vue.set(state.data, "description", object.description);
  }
};
=======

    saveImageToState({commit}, object){
        commit('setImageState', object)
    },


    async sendImageObject({commit}){
        let response = await axios.post("/images/api/create/", state.data, {headers: {
            Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
            'Content-Type': 'application/json',
        }})
        commit('resetImageState')
        if(response.data === 'success'){
            router.push('Home')
        }
    }
}

const mutations = {
    setImageState(state, object){
        Vue.set(state.data, "title", object.title)
        Vue.set(state.data, "url", object.url)
        Vue.set(state.data, "description", object.description)
    },
    resetImageState(state){
        Vue.set(state.data, "title","" )
        Vue.set(state.data, "url", "")
        Vue.set(state.data, "description", "")
    }

}
>>>>>>> fd58a4b44bdfd67f2a54cc19326ced700bb80159

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
