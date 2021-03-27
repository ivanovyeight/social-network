<template>
  <v-app
    id="main"
    :style="{ background: $vuetify.theme.themes[theme].background }"
  >
    <v-app-bar app>
      <div class="row">
        <v-btn text disabled>SOCIAL NETWORK</v-btn>
        <v-spacer></v-spacer>

        <template v-if="!whoami.access_token && !whoami.username">
          <v-btn text class="mx-2" to="/register">Register</v-btn>
          <v-btn text class="mx-2" to="/login">Login</v-btn>
        </template>

        <template v-else>
          <v-btn text class="mx-2" to="/">Timeline</v-btn>
          <v-btn text class="mx-2" to="/profile">Profile</v-btn>
          <v-btn text class="mx-2" to="/about">About</v-btn>
          <v-spacer></v-spacer>
          <v-btn text class="mx-2" v-on:click="handleLogout">Logout</v-btn>
        </template>

        <v-btn text @click="$vuetify.theme.dark = !$vuetify.theme.dark">
          <v-icon v-if="$vuetify.theme.dark">
            mdi-moon-waning-crescent
          </v-icon>
          <v-icon v-else>
            mdi-weather-sunny
          </v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  name: "App",
  computed: {
    ...mapState({
      whoami: state => state.authentication.whoami
    }),
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
  },
  methods: {
    handleLogout(event) {
      event.preventDefault();
      this.$store.commit("LOGOUT");
      if (this.$route.path != "/") {
        this.$router.push("/");
      }
    },
    ...mapActions(["logout"])
  }
};
</script>
