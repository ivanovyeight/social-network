<template>
  <ValidationObserver ref="observer" v-slot="{  }">
    <form>
              <v-img
      :src="url"
      :lazy-src="url"
      max-width="500"
      max-height="300"
      ref="image"
    >
      <template v-slot:placeholder>
        <v-row
          class="fill-height ma-0"
          align="center"
          justify="center"
        >
          <v-progress-circular
            indeterminate
            color="grey lighten-5"
          ></v-progress-circular>
        </v-row>
      </template>
      </v-img>

      <ValidationProvider v-slot="{ }" name="Title" rules="required|max:30">
        <v-text-field
          v-model="title"
          :counter="30"
          label="Title"
          required
        ></v-text-field>
      </ValidationProvider>
        <v-text-field
          v-model="description"
          :counter="150"
          label="Description"

        
        ></v-text-field>
      <v-btn class="mr-4" @click="submit">submit</v-btn>
    </form>
  </ValidationObserver>
</template>


<script>
  import { required, max } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  import {mapGetters, mapActions} from "vuex"

  setInteractionMode('eager')

  extend('required', {
    ...required,
    message: '{_field_} can not be empty',
  })

  extend('max', {
    ...max,
    message: '{_field_} may not be greater than {length} characters',
  })
  export default {
    name: "ImageForm",
    components: {
      ValidationProvider,
      ValidationObserver,
    },
    data: () => ({
      title: '',
      description: "",
      url: '',
    
    }),

    methods: {
      imageValidation(){
        let img = document.createElement('img')
        img.src = this.url
        if (img.width == 0){
          return false;
        }
      },
      submit () {
        this.$refs.observer.validate()
        if (this.imageValidation()===false){
          console.log("false")
          return false
        }
        else{
          let obj = {
            title: this.title,
            url: this.url,
            description: this.description,
        }
        this.saveImageToState(obj)
        this.sendImageObject()

        }

      },
      ...mapActions(["sendImageObject", "saveImageToState"])
    },
    computed: {
      ...mapGetters(["imageData"]),
      
    },
    created(){
      this.title = this.$route.query.title
      this.url = this.$route.query.url
      this.description = ""
      
    }
  }
</script>


<style>
#image{
  margin: auto;
}
</style>

