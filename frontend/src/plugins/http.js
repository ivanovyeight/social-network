import axios from "axios";
import store from "../store";
import createAuthRefreshInterceptor from "axios-auth-refresh";

const http = axios.create({
  baseURL: `http://localhost:8000/`,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Bearer ${store.state.auth.iam.access_token}`
  }
});

const refreshAuthLogic = failedRequest =>
  http
    .post("http://localhost:8000/account/api/token/refresh/", {
      refresh: store.state.auth.iam.refresh_token
    })
    .then(tokenRefreshResponse => {
      let key = "access_token";
      let value = tokenRefreshResponse.data["access"];
      store.commit("IAM_UPDATE", { key, value });
      failedRequest.response.config.headers[
        "Authorization"
      ] = `Bearer ${tokenRefreshResponse.data["access"]}`;

      return Promise.resolve();
    });

createAuthRefreshInterceptor(http, refreshAuthLogic);

export default http;
