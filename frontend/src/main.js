import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
// import axios from "axios";
// import createAuthRefreshInterceptor from "axios-auth-refresh";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

// const refreshAuthLogic = failedRequest =>
//   axios
//     .post("http://localhost:8000/account/api/token/refresh/", {
//       refresh: store.state.authentication.whoami.refresh_token
//     })
//     .then(tokenRefreshResponse => {
//       let key = "access_token";
//       let value = tokenRefreshResponse.data["access"];
//       store.commit("WHOAMI_UPDATE", { key, value });
//       failedRequest.response.config.headers[
//         "Authorization"
//       ] = `Bearer ${tokenRefreshResponse.data["access"]}`;
//       return Promise.resolve();
//     });

// // Instantiate the interceptor (you can chain it as it returns the axios instance)
// createAuthRefreshInterceptor(axios, refreshAuthLogic);
