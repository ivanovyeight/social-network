<template>
  <v-container class="row my-5 mx-auto">
    <v-card class="col-md-3">
      <v-row class="my-auto mx-auto">
        <v-avatar color="grey" size="64" round>
          <v-img
            src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
            alt="..."
          ></v-img>
        </v-avatar>
        <v-card-title>
          <template v-if="whoami.first_name || whoami.last_name">
            {{ whoami.first_name }}
            {{ whoami.last_name }}
          </template>
          <template v-else>
            {{ whoami.username }}
          </template>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-btn text @click="formIsVisible = !formIsVisible">
          <v-icon>mdi-dots-horizontal</v-icon>
        </v-btn>
      </v-row>

      <template v-if="formIsVisible">
        <form>
          <div class="container">
            <v-text-field
              type="text"
              placeholder="First Name"
              v-model="first_name"
            ></v-text-field>
            <v-text-field
              v-model="last_name"
              type="text"
              placeholder="Last Name"
            ></v-text-field>
            <v-text-field
              v-model="email"
              type="text"
              placeholder="Email"
            ></v-text-field>
            <v-text-field
              type="text"
              v-model="date_of_birth"
              placeholder="Date Of Birth"
            ></v-text-field>
          </div>
        </form>
      </template>
    </v-card>

    <v-card class="mx-auto col-8">
      <v-btn text block muted>Latest Events:</v-btn>
      <!-- <div v-for="action in actions" :key="action.id" class="col-md-12">
              ACTION_PLACEHOLDER
          </div> -->
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      formIsVisible: false,
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
