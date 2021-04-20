import axios from "axios";

const state = {
  iam: ""
};

const actions = {
  login({ commit }, { username, password }) {
    let credentials = { username, password };

    axios.post("/account/login/", credentials).then(response => {
      commit("LOGIN", response.data);
    });
  },
  async iamUpdate({ commit, state }, { key, value }) {
    let payload = {
      id: state.iam.id,
      key: key,
      value: value
    };

    let headers = {
      Authorization: `Bearer ${state.iam.access_token}`
    };

    await axios.post("http://localhost:8000/account/update/", payload, {
      headers
    });

    commit("IAM_UPDATE", { key, value });
  }
};

const mutations = {
  LOGIN(state, payload) {
    state.iam = payload;
  },
  LOGOUT(state) {
    state.iam = "";
  },
  IAM_UPDATE(state, { key, value }) {
    state.iam[key] = value;
  }
};

export default { state, actions, mutations };
