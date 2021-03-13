<template>
  <div class="col-md-6 mx-auto">
    <v-form>
      <v-container>
        <v-text-field v-model="email" label="Email" required></v-text-field>
        <v-text-field
          v-model="username"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          required
        ></v-text-field>
      </v-container>
      <v-btn
        dark
        color="grey darken-2"
        block
        x-large
        class="btn-block"
        @click="registerUser"
      >
        Register
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      username: "",
      password: ""
    };
  },
  methods: {
    registerUser() {
      axios
        .post("http://localhost:8000/account/register/", {
          email: this.email,
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: "Login" });
        });
    }
  }
};
</script>
