<template>
  <div class="col-md-6 mx-auto">
    <form>
      <v-text-field
        v-model="username"
        type="text"
        required
        placeholder="Username"
      ></v-text-field>
      <v-text-field
        type="password"
        required
        v-model="password"
        placeholder="Password"
      ></v-text-field>
      <v-btn
        dark
        color="grey darken-2"
        block
        x-large
        class="btn-block"
        @click="handleLogin"
        >Login</v-btn
      >
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: ""
    };
  },
  methods: {
    handleLogin(event) {
      event.preventDefault();
      this.login({ username: this.username, password: this.password }).then(
        this.$router.push("/")
      );
    },
    ...mapActions(["login"])
  }
};
</script>
