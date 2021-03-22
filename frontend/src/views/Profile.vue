<template>
  <v-container class="col-md-6">
    <v-card class="my-2">
      <div class="col-md-4 mx-auto">
        <v-avatar color="grey" size="256" round>
          <v-img
            src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
            alt="..."
          ></v-img>
        </v-avatar>
        <!-- <v-btn text @click="formIsVisible = !formIsVisible">
          <v-icon>mdi-dots-horizontal</v-icon>
        </v-btn> -->
      </div>

      <form>
        <div class="container">
          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                type="text"
                placeholder="First Name"
                v-model="first_name"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="last_name"
                type="text"
                placeholder="Last Name"
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="email"
                type="text"
                placeholder="Email"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                type="text"
                v-model="date_of_birth"
                placeholder="Date Of Birth"
              ></v-text-field>
            </v-col>
          </v-row>
        </div>
      </form>
    </v-card>

    <v-card class="my-2">
      <v-container >
      SUBSCRIPTION_SETTINGS

      </v-container>
    </v-card>


  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      actions: []
    };
  },
  methods: {
    ...mapActions(["whoamiUpdate"])
  },
  computed: {
    ...mapState({
      whoami: state => state.authentication.whoami
    }),
    first_name: {
      get() {
        return this.whoami.first_name;
      },
      set(value) {
        this.whoamiUpdate({ key: "first_name", value });
      }
    },
    last_name: {
      get() {
        return this.whoami.last_name;
      },
      set(value) {
        this.whoamiUpdate({ key: "last_name", value });
      }
    },
    email: {
      get() {
        return this.whoami.email;
      },
      set(value) {
        this.whoamiUpdate({ key: "email", value });
      }
    },
    date_of_birth: {
      get() {
        return this.whoami.date_of_birth;
      },
      set(value) {
        this.whoamiUpdate({ key: "date_of_birth", value });
      }
    }
  }
};
</script>
