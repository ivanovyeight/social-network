<template>
  <div>Image title:{{ getImageDetail.title }}</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data: () => ({
    title: ""
  }),
  methods: {
    ...mapActions["getImage"]
  },
  computed: {
    ...mapGetters(["getImageDetail"])
  },
  async created() {
    await this.$store.dispatch("getImage");
    this.title = this.$store.getters.getImageDetail.title;
  }
};
</script>

<style></style>
