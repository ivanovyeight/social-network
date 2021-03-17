<template>
  <ValidationObserver ref="form">
    <v-form @submit.prevent="onSubmit">
      <v-container>
        <ValidationProvider
          name="Email"
          rules="email|required"
          v-slot="{ errors }"
        >
          <v-text-field v-model="email" label="Email" required></v-text-field>
          <span class="red--text">{{ errors[0] }}</span>
        </ValidationProvider>

        <ValidationProvider
          name="Username"
          rules="required"
          v-slot="{ errors }"
        >
          <v-text-field
            v-model="username"
            label="Username"
            required
          ></v-text-field>
          <span class="red--text">{{ errors[0] }}</span>
        </ValidationProvider>

        <ValidationProvider
          name="Password"
          rules="required"
          v-slot="{ errors }"
        >
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            required
          ></v-text-field>
          <span class="red--text">{{ errors[0] }}</span>
        </ValidationProvider>
      </v-container>
      <v-btn
        dark
        color="grey darken-2"
        block
        x-large
        class="btn-block"
        type="submit"
      >
        Register
      </v-btn>
    </v-form>
  </ValidationObserver>
</template>

<script>
import axios from "axios";
import { extend, ValidationProvider, ValidationObserver } from "vee-validate";
import { required, email } from "vee-validate/dist/rules";

extend("email", email);
extend("required", required);

export default {
  components: {
    ValidationProvider,
    ValidationObserver
  },
  data() {
    return {
      email: "",
      username: "",
      password: ""
    };
  },
  methods: {
    onSubmit() {
      this.$refs.form.validate().then(success => {
        if (!success) {
          return;
        }

        axios
          .post("http://localhost:8000/account/register/", {
            email: this.email,
            username: this.username,
            password: this.password
          })
          .then(() => {
            this.$router.push({ name: "Login" });
          });

        // Wait until the models are updated in the UI
        this.$nextTick(() => {
          this.$refs.form.reset();
        });
      });
    }
  }
};
</script>
