import axios from "axios";

const state = {
  whoami: ""
};

const actions = {
  login({ commit }, { username, password }) {
    let credentials = { username, password };

    axios.post("/account/login/", credentials).then(response => {
      commit("LOGIN", response.data);
    });
  },
  async whoamiUpdate({ commit, state }, { key, value }) {
    let payload = {
      id: state.whoami.id,
      key: key,
      value: value
    };

    let headers = {
      Authorization: `Bearer ${state.whoami.access_token}`
    };
    // console.log(headers);

    await axios.post("http://localhost:8000/account/update/", payload, {
      headers
    });

    commit("WHOAMI_UPDATE", { key, value });
  }
};

const mutations = {
  LOGIN(state, payload) {
    state.whoami = payload;
  },
  LOGOUT(state) {
    state.whoami = "";
  },
  WHOAMI_UPDATE(state, { key, value }) {
    state.whoami[key] = value;
  }
};

export default { state, actions, mutations };
