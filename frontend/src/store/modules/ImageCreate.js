import axios from 'axios'
import Vue from 'vue'
import { ACCESS_TOKEN } from '../../services/auth';



const state = {
    data:{
        title: "",
        description: "",
        url: "",
    }
}




const actions = {

    saveImageToState({commit}, object){
        commit('setImageState', object)
    },


    async sendImageObject(){
        await axios.post("/images/api/create/", state.data, {headers: {
            Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
            'Content-Type': 'application/json',
          }})
    }
}

const mutations = {
    setImageState(state, object){
        Vue.set(state.data, "title", object.title)
        Vue.set(state.data, "url", object.url)
        Vue.set(state.data, "description", object.description)

    }

}

const getters = {
    imageData(){
        return state.data
    }

}

export default {
    state,
    actions,
    mutations,
    getters,
}
