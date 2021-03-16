import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

axios.interceptors.response.use(
  function(response) {
    return response;
  },
  function(error) {
    if (error.response.status == 401) {
      // console.log(error.config.headers["Authorization"])
      let failed = error.config;
      axios
        .post("http://localhost:8000/account/api/token/refresh/", {
          refresh: store.state.authentication.whoami.refresh_token
        })
        .then(response => {
          let key = "access_token";
          let value = response.data["access"];
          store.commit("WHOAMI_UPDATE", { key, value });
          failed.headers["Authorization"] = `Bearer ${value}`;
          // console.log(failed.headers["Authorization"])
        });
      return axios(failed);
    } else {
      return Promise.reject(error);
    }
  }
);

// try {
//   axios
//     .post("http://localhost:8000/account/api/token/refresh/", {
//       refresh: store.state.authentication.whoami.refresh_token
//     })
//     .then(response => {
//       let key = "access_token";
//       let value = response.data["access"];

//       store.commit("WHOAMI_UPDATE", { key, value });
//       failed.headers["Authorization"] = value
//       // axios(failed)
//     });
// } catch {
//   store.commit("LOGOUT");
//   router.push("/login");
//   return Promise.reject(error);
// }
//   }
// );

// axios.interceptors.response.use(function(response) {
//     return response;
//   },
//   function(error) {
//     let retry =

//     if (error.response.status == 401) {

//         axios.post("http://localhost:8000/account/api/token/refresh/", {
//           refresh: store.state.authentication.whoami.refresh_token
//         })
//         .then(response => {
//           let key = "access_token";
//           let value = response.data["access"];

//           store.commit("WHOAMI_UPDATE", { key, value });
//           axios(retry)

//           Promise.resolve(true);
//         })
//       })

//       .catch(error => {
//         store.commit("LOGOUT");
//         router.push("/login");
//         Promise.reject(error);
//       });
//     }
// );
