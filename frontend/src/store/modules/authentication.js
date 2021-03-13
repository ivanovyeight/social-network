import axios from "axios"

const state = {
  whoami: '',
};

const actions = {
  login({ commit }, { username, password }) {
    let credentials = { username, password }

    axios.create({
      baseURL: "http://localhost:8000",
      timeout: 5000,
      headers: { "Content-Type": "application/json", accept: "application/json" }
    }).post("/account/get-token-for-user/", credentials)
    .then(response => {
      commit("LOGIN", response.data);
    })
  },
  logout({ commit }) {
    commit("LOGOUT");
  }
};

const mutations = {
  LOGIN(state, payload) {
    state.whoami = payload
  },
  LOGOUT(state) {
    state.whoami = ''
  }
};

export default { state, actions, mutations };
