import axios from 'axios'
import Vue from 'vue'
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
        await axios.post("/images/api/create/", state)
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
