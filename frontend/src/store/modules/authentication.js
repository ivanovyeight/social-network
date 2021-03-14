import axios from "axios";

const state = {
  whoami: ""
};

const actions = {
  login({ commit }, { username, password }) {
    let credentials = { username, password };

    axios
      .create({
        baseURL: "http://localhost:8000",
        timeout: 5000,
        headers: {
          "Content-Type": "application/json",
          accept: "application/json"
        }
      })
      .post("/account/get-token/", credentials)
      .then(response => {
        commit("LOGIN", response.data);
      });
  },
  whoamiUpdate({ commit,state }, { key, value }) {
    const sendPatchRequest = async () => {
      try {
        const response = await axios.post(
          "http://localhost:8000/account/update/",
          {
            id: state.whoami.id,
            key: key,
            value: value
          }
        );
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    sendPatchRequest();
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
